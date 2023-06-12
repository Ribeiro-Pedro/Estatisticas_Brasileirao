# Análise de Dados das Equipes do Brasileirão

## Visão Geral

O objetivo deste projeto de análise de dados é coletar informações estatísticas das equipes que disputam a Série A do Campeonato Brasileiro de Futebol Masculino. Para isso, utilizou-se técnicas de web scraping para extrair os dados relevantes do site FPREF, que contém estatísticas detalhadas sobre diversos aspectos do jogo.

As informações coletadas abrangem estatísticas dos times, goleiros, finalizações, passes, chances de gol criadas, defesa, posse de bola e tempo de jogo. Com esses dados, pode-se realizar análises aprofundadas para entender o desempenho das equipes e identificar tendências e padrões ao longo da temporada.

## Ferramentas Utilizadas

Para realizar a coleta de dados, utilizou-se a técnica de web scraping, utilizando bibliotecas de Python, como BeautifulSoup e Requests. Essas bibliotecas nos permitem extrair o conteúdo HTML do site FPREF. Em seguida utilizou-se a biblioteca gspread para fazer a persistência desses dados e utiliza-los posteriormente para análise.

Além disso, para a análise de dados, utilizaram-se as bibliotecas populares de Python, como Pandas, NumPy, Matplotlib e Seaborn. Essas bibliotecas fornecem funcionalidades poderosas para manipulação, visualização e análise de dados, permitindo-nos obter insights valiosos a partir dos dados coletados.

## Fluxo de Trabalho

#### Coleta de Dados:

- Realizou-se o web scraping do site FPREF para obter as estatísticas das equipes da Série A do Campeonato Brasileiro de Futebol Masculino.
- Extraiu-se informações sobre estatísticas dos times, goleiros, finalizações, passes, chances de gol criadas, defesa, posse de bola e tempo de jogo.

Os dados podem ser acessados através desse [link](https://docs.google.com/spreadsheets/d/1nVyKyf4dVwrCleXtGz3gH7b6Hvs08pLsDr_ENfwL4LM/edit?usp=sharing)

#### Limpeza e Preparação dos Dados:

- Realizou-se a limpeza dos dados coletados, tratando eventuais valores ausentes, inconsistências ou erros.
- Realizou-se a transformação e formatação dos dados para uma planilha do google sheets.
