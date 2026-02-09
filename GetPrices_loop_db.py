import os
import pandas as pd
import time 
from dotenv import load_dotenv
from sqlalchemy import create_engine

from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

load_dotenv()
# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port") 
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
engine = create_engine(DATABASE_URL)

SLEEP_SECONDS = 60

if __name__ == '__main__':
    while True:
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()

        df = pd.concat([df_btc, df_comm], ignore_index=True)

        df.to_sql('cotacoes', engine, if_exists="append", index=False)

        print('Cotações inseridas com sucesso!')

        time.sleep(SLEEP_SECONDS)