from blockfrost import BlockFrostApi, ApiError, ApiUrls
import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

load_dotenv()
api_key = os.getenv("BLOCKFROST_API_TOKEN")
api = BlockFrostApi(project_id=api_key)

# LQ token information
policy_id = "da8c30857834c6ae7203935b89278c532b3995245295456f993e1d24"
asset_name = "4c51"

token_name = bytearray.fromhex(asset_name).decode()

page = 1
count = 100
df_asset_tx = pd.DataFrame()

while True:
    data = api.asset_transactions(asset=policy_id + asset_name, page=page, return_type="pandas")
    df_asset_tx = pd.concat([data,df_asset_tx])
    if len(data) < 100:
#    if page > 3:
        break
    page += 1

def write_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

write_csv(df_asset_tx, token_name+"_tx_data.csv")
