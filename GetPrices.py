import pandas as pd
import time
from GetCommodities import get_commodities_df
from GetBitcoin import get_bitcoin_df

v_bitcoin = get_bitcoin_df()
v_commodities = get_commodities_df()

print(v_bitcoin)
print(v_commodities)