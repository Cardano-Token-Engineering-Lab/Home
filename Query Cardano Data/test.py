import koios_api as koi
import json
import itertools
import pandas as pd
import openpyxl

# print(koi.get_tip())

policy_id = "a04ce7a52545e5e33c2867e148898d9e667a69602285f6a1298f9d68"


# Generate token metadata dataframe from asset policy info
def policy_info(pol_id):
    asset_policy_info = koi.get_policy_asset_info(pol_id)
    df_policy_info = pd.DataFrame.from_dict(asset_policy_info)
    return df_policy_info


def metadata(df_policy_info):
    df_reg_metadata = df_policy_info["token_registry_metadata"].to_frame()
    df_metadata = df_reg_metadata.explode("token_registry_metadata").reset_index(
        drop=True
    )
    df_metadata = df_metadata.join(
        pd.json_normalize(df_reg_metadata.pop("token_registry_metadata"))
    )
    df_metadata = df_metadata.iloc[0]
    return df_metadata


# Extract metadata key info
def metadata_pull(pol_id, df_metadata):
    df = policy_info(pol_id)
    total_supply = pd.to_numeric(df["total_supply"])
    token_name = df_metadata["name"]
    token_ticker = df_metadata["ticker"]
    token_decimals = df_metadata["decimals"]
    return total_supply, token_name, token_ticker, token_decimals


# Generate Token holder addresses and quantities from policy ID
def holders(df_policy_info, pol_id, name, decimals):
    asset_address_list = koi.get_asset_address_list(pol_id)
    df_holders = pd.DataFrame.from_dict(asset_address_list)
    df_holders["Name"] = name
    df_holders["quantity"] = pd.to_numeric(df_holders["quantity"]) / (
        10**token_decimals
    )
    df_holders = df_holders.sort_values(by="quantity", ascending=False)
    total_circ_supply = df_holders["quantity"].sum()
    total_supply = pd.to_numeric(df_policy_info["total_supply"]) / (
        10**token_decimals
    )
    print("Total Circulating Supply = ", total_circ_supply)
    pct_circ = total_circ_supply / total_supply
    print("Pct of Tokens in circulation = ", pct_circ)
    print(df_holders.head(20))
    return df_holders


def xls_writer(df):
    df.to_excel("token holders data.xlsx")


df_policy_info = policy_info(policy_id)

df_metadata = metadata(df_policy_info)

total_supply, token_name, token_ticker, token_decimals = metadata_pull(
    policy_id, df_metadata
)

df_holders = holders(df_policy_info, policy_id, token_name, token_decimals)

xls_writer(df_holders)
