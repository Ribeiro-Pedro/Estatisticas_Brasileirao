import pandas as pd

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError

import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Definição das permissões necessárias para acesso às planilhas do Google
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

json_path = r'C:\Users\pedro\Projetos_Python\Projetos\Portifolio\web_scraping_fut\Estatisticas_Brasileirao\data collection\gbq.json'

# Carregar as credenciais a partir do arquivo JSON 'gbq.json' e definir as permissões
<<<<<<< HEAD
<<<<<<< HEAD
credentials = Credentials.from_service_account_file(json_path, scopes=scopes)
=======
credentials = Credentials.from_service_account_file('gbq.json', scopes=scopes)
>>>>>>> parent of 22f8144 (agosto)
=======
credentials = Credentials.from_service_account_file('gbq.json', scopes=scopes)
>>>>>>> parent of 22f8144 (agosto)

# Autorizar o acesso às planilhas do Google usando as credenciais
gc = gspread.authorize(credentials)

# Autenticação no Google Drive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Abrir uma planilha do Google
gs = gc.open_by_key('1nVyKyf4dVwrCleXtGz3gH7b6Hvs08pLsDr_ENfwL4LM')

# URL da página a ser acessada
url = "https://fbref.com/en/comps/24/Serie-A-Stats"

# Cabeçalhos HTTP para simular um navegador
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

try:
    # Abrir a URL e obter o conteúdo HTML da página
    response = urlopen(url)
    html = response.read()
    
except HTTPError as e:
    # Lidar com erros HTTP, caso ocorram
    print(e.status, e.reason)
    
except URLError as e:
    # Lidar com erros de URL, caso ocorram
    print(e.reason)

# Função para tratar o HTML removendo espaços extras e quebras de linha
def trata_html(input):
    html = input.decode('utf-8')
    return " ".join(html.split()).replace('> <','><')

# Tratar o HTML obtido
html = trata_html(html)

# Criar um objeto BeautifulSoup a partir do HTML tratado
soup = BeautifulSoup(html, 'html.parser')

# Dicionário que mapeia o nome da página na planilha com o ID da tabela no HTML
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

# Iterar sobre as páginas e IDs das tabelas no dicionário
for pagina, id in dict_tables.items():
  # Encontrar a tabela no HTML usando o ID
  soup_tabela = soup.find('table', id = id).find_all('tbody')
  
  lista_equipes = []
  # Iterar sobre as linhas da tabela
  for equipe in soup_tabela[0].find_all('tr'):
    dict_equipe = {}
    # Obter o nome da equipe a partir da coluna 'th' e seu valor correspondente
    dict_equipe[equipe.find('th').get('data-stat')] = equipe.find('th').getText()
    # Iterar sobre as colunas de informações da equipe
    for info in equipe.find_all('td'):
        # Obter o nome da coluna a partir do atributo 'data-stat' e seu valor correspondente
        dict_equipe[info.get('data-stat')] = info.getText()
    
    lista_equipes.append(dict_equipe)

  # Converter a lista de dicionários em um DataFrame usando pandas
  df = pd.DataFrame(lista_equipes)

  # Obter a planilha correspondente à página
  pagina = gs.worksheet(pagina)
  # Limpar o conteúdo da planilha
  pagina.clear()
  # Preencher a planilha com os dados do DataFrame, incluindo o cabeçalho das colunas
  set_with_dataframe(
    worksheet=pagina, 
    dataframe=df,
    include_index=False,
    include_column_header=True,
    resize=True)

  # Imprimir a mensagem de atualização da tabela
  print(f"Tabela {pagina} atualizada.")