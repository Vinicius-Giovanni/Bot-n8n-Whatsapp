# Junta Bitcoin + Commodities em um único DataFrame e imprime (uma vez).

import pandas as pd
from GetCommodities import get_commodities_df
from GetBitcoin import get_bitcoin_df

if __name__ == "__main__":
    # Coleta
    v_bitcoin = get_bitcoin_df()
    v_commodities = get_commodities_df()

    # Concatena tudo
    df = pd.concat([v_bitcoin, v_commodities], ignore_index=True)

    # Imprime
    print(df)