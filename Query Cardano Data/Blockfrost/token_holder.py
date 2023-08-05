import pandas as pd
from token_info import asset_info
from helper_functions import read_csv, write_csv, get_api_token
from project_data import asset_name, policy_id, token_name

# Load Blockfrost API key
api = get_api_token()

asset_name = asset_name
policy_id = policy_id

# Query the current token holding addresses
def query_holders(policy_id, asset_name, page):
    df = pd.DataFrame()
    df_info = asset_info(policy_id,asset_name)
    while True:
        data = api.asset_addresses(asset=policy_id + asset_name, page=page, return_type="pandas")
        df = pd.concat([data,df])

        if len(data) < 100:
            break
        page += 1
        print(f'Total number of API calls used: {page}')

    decimal = df_info['metadata.decimals'].iloc[0]
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["quantity"] = df["quantity"] / (10**decimal)
    return df

# Pull in data if needing to query use first statement or if available locally use second line
df_asset_addy = query_holders(policy_id, asset_name, 1)
# df_asset_addy = read_csv(token_name + "_holders.csv")

# Run if needing to save data locally
write_csv(df_asset_addy, token_name + "_holders.csv")
