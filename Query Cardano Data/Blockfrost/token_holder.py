from blockfrost import BlockFrostApi, ApiError, ApiUrls
import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
api_key = os.getenv("BLOCKFROST_API_TOKEN")
api = BlockFrostApi(project_id=api_key)

# LQ token information
policy_id = "da8c30857834c6ae7203935b89278c532b3995245295456f993e1d24"
asset_name = "4c51"

token_name = bytearray.fromhex(asset_name).decode()
page = 1
count = 100
asset_address = []

while True:
    data = api.asset_addresses(asset=policy_id + asset_name, page=page)
    asset_address.extend(data)

    if len(data) < 100:
        break
    page += 1

data_dict = {
    "address": [obj.address for obj in asset_address],
    "quantity": [obj.quantity for obj in asset_address],
}

df_lq_addy = pd.DataFrame(data_dict)

# Decimals for LQ token is 6
df_lq_addy["quantity"] = pd.to_numeric(df_lq_addy["quantity"], errors="coerce")
df_lq_addy["quantity"] = df_lq_addy["quantity"] / 10**6

print(df_lq_addy.head(10))


def xls_writer(df, token_name):
    filename = token_name + "_token_holders_data.xlsx"
    df.to_excel(filename)


xls_writer(df_lq_addy, token_name)
