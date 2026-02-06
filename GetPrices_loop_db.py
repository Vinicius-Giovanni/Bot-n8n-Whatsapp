# A cada 60s: Junta Bitcoin + Commodities e salva no banco de dados relacional postgress da supabase.

import time
import pandas as pd
from sqlalchemy import create_engine # Biblioteca para trabalhar com objetos no banco de dados
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")


print("USER:", USER)
print("PASSWORD:", PASSWORD)
print("HOST:", HOST)
print("PORT:", PORT)
print("DBNAME:", DBNAME)


# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    while True:
        # Coleta
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()

        # Concatena dataframes
        df = pd.concat([df_btc, df_comm], ignore_index=True)

        # Salva no banco (append)
        df.to_sql("cotacoes",engine,if_exists='append', index=True)

        print("Cotações inseridas no banco de dados")

        # Espera próximo ciclo
        time.sleep(60)

"""
Erro:
DNS resolve o domínio
Supabase responde
Não acha a rota para conectar ao banco, devido a rede corporativa não suportar IPv6 para saída
psycopg2 tenta usar IPv6 -> falha na conexão

Teste rodado:
slookup db.dslrertwrdnoeemjoofd.supabase.co

Retorno do teste:
Servidor:  berlin1.dc.nova
Address:  10.128.8.75

Nome:    db.dslrertwrdnoeemjoofd.supabase.co
Address:  2600:1f13:838:6e0a:8a3a:8e98:f8db:8f47

IPv6 = Nºs hexadecimais
IPv4 = Nºs de 0 - 255 separados em 4 blocos
"""