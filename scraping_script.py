import pandas as pd

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError

import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('gbq.json', scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# open a google sheet
gs = gc.open_by_key('1nVyKyf4dVwrCleXtGz3gH7b6Hvs08pLsDr_ENfwL4LM')

url = "https://fbref.com/en/comps/24/Serie-A-Stats"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

try:
    response = urlopen(url)
    html = response.read()
    
except HTTPError as e:
    print(e.status, e.reason)
    
except URLError as e:
    print(e.reason)

def trata_html(input):
    html = input.decode('utf-8')
    return " ".join(html.split()).replace('> <','><')

html = trata_html(html)
soup = BeautifulSoup(html, 'html.parser')

dict_tables = {
  "Classificação": "results2023241_overall",
  "Estats Time" :  "stats_squads_standard_for",
  "Goleiros" : "stats_squads_keeper_for",
  "Goleiros adv" : "stats_squads_keeper_adv_for",
  "Finalizações" : "stats_squads_shooting_for",
  "Passes" : "stats_squads_passing_for",
  "Passes Tipo" : "stats_squads_passing_types_for",
  "Chances Criadas" : "stats_squads_gca_for",
  "Defesa" : "stats_squads_defense_for",
  "Posse de Bola" : "stats_squads_possession_for",
  "Tempo de Jogo" : "stats_squads_playing_time_for",
  "Diversos" : "stats_squads_misc_for"
}

for pagina, id in dict_tables.items():
  soup_tabela = soup.find('table', id = id).find_all('tbody')
  
  lista_equipes = []
  for equipe in soup_tabela[0].find_all('tr'):
    dict_equipe = {}
    dict_equipe[equipe.find('th').get('data-stat')] = equipe.find('th').getText()
    for info in equipe.find_all('td'):
        dict_equipe[info.get('data-stat')] = info.getText()
    
    lista_equipes.append(dict_equipe)

  df = pd.DataFrame(lista_equipes)

  pagina = gs.worksheet(pagina)
  pagina.clear()
  set_with_dataframe(
    worksheet=pagina, 
    dataframe=df,
    include_index=False,
    include_column_header=True,
    resize=True)

  print(f"Tabela {pagina} atualizada.")