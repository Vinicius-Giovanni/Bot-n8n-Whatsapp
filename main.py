import pandas as pd
import requests
from datetime import datetime

# URL para requisitar o valor do bitcoin atual
url = "https://api.coinbase.com/v2/prices/spot"

# Requisição GET da API
response = requests.get(url)
data = response.json()

# Extração de dados da API
preco = float(data['data']['amount'])
ativo = data['data']['base']
moeda = data['data']['currency']
horario_de_coleta = datetime.now()

print(f'{preco}\n{ativo}\n{moeda}\n{horario_de_coleta}')

df = pd.Dataframe([{
    'preco' : preco,
    'ativo' : ativo,
    'moeda' : moeda,
    'horario_de_coleta' : horario_de_coleta,
}])


df.to_csv('preco_bitcoin.csv', mode='a', header=False, index=False)
"""
mode = a ou w(padrão)
a = append
- adiciona os dados no final do arquivo
- não apaga o que já existe

w = write
- cria o arquivo do zero
- se já existir, apaga tudo e sobrescreve
"""

"""
header = True(padrão) ou False
True - escreve o cabeçalho a cada atualização
False - não escreve o cabeçalho
"""

"""
index = False ou True(padrão)
True - Salva o índice como coluna no arquivo
False - não salva o índice
"""

01:12:07
