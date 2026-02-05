"""
Requisição dos valores de commodities pela biblioteca yfinance

Observação: yfinance é uma biblioteca que faz webscraping do site yahoo yfinance, por isso é uma forma diferente
de fazer requisição
"""

import yfinance as yf
from datetime import datetime
import pandas as pd

def get_commodities_df():

    symbols = ['GC=F','CL=F', 'SI=F']
    dfs = []
    for sym in symbols:
        df = yf.Ticker(sym).history(period='1d', interval='1m')[['Close']].tail(1) # Ticker é o nome do ativo na bolsa
        """
        Os dados da biblioteca yfinance já vem em dataframe, por já importar o pandas e o requests
        history = retorna o historico do ativo puxado
        period = filtra o periódo = dia atual
        interval = filtra o intervalo de mudanças no preço
        [['close']] = Pega o último periódo do intervalo
        tail.(1) pega o ultimo valor de fechamento
        """

        #print(df.tail(1)) # Pega o primeiro valor do fechamento do ativo

        df = df.rename(columns={'Close': 'preco'})
        df['ativo'] = sym
        df['horario_de_coleta'] = datetime.now()
        df['moeda'] = 'USD'

        df = df[['ativo','preco','moeda','horario_de_coleta']]
        dfs.append(df) # Adiciono no dfs o df atual

    return pd.concat(dfs, ignore_index=True) # concateno todo o dfs em um único df