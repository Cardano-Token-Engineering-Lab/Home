import pandas as pd
from token_info import asset_info
from helper_functions import read_csv, write_csv, get_api_token

# Load Blockfrost API key
api = get_api_token()

# Token information to be queried analyzed
policy_id = "da8c30857834c6ae7203935b89278c532b3995245295456f993e1d24"
asset_name = "4c51"
token_name = bytearray.fromhex(asset_name).decode()

def query_holders(policy_id, asset_name, page):
    df = pd.DataFrame()
    df_info = asset_info(policy_id,asset_name)
    while True:
        data = api.asset_addresses(asset=policy_id + asset_name, page=page, return_type="pandas")
        df = pd.concat([data,df])

        if len(data) < 100:
            break
        page += 1

    decimal = df_info['metadata.decimals'].iloc[0]
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["quantity"] = df["quantity"] / (10**decimal)
    return df

# Pull in data if needing to query use first statement or if available locally use second line
df_asset_addy = query_holders(policy_id, asset_name, 1)
# df_asset_addy = read_csv(token_name + "_holders.csv")

# Run if needing to save data locally
write_csv(df_asset_addy, token_name + "_holders.csv")
