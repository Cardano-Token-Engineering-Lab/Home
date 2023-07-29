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


def asset_info(policy_id, asset_name):
    df = api.asset(asset=policy_id + asset_name, return_type="pandas")
    return df

def tokens_in_policy(policy_id):
    df = api.assets_policy(policy_id, return_type="pandas")
    policy_token_count = len(df.index)
    print(
        f"The total number of tokens under the selected policy is/are: {policy_token_count}"
    )
    return df

df_info = asset_info(policy_id,asset_name)

df_tokens_in_policy = tokens_in_policy(policy_id)

dataframes_dict = {'Asset Info': df_info, 'Tokens In Policy': df_tokens_in_policy}

def create_xlsx(dataframes_dict, output_filename):
    workbook = Workbook()
    for sheet_name, df in dataframes_dict.items():
        sheet = workbook.create_sheet(title=sheet_name)
        for row in dataframe_to_rows(df, index=False, header=True):
            sheet.append(row)

    # Remove the default empty sheet created by openpyxl
    workbook.remove(workbook['Sheet'])

    # Save the workbook to the specified output filename
    workbook.save(output_filename)

create_xlsx(dataframes_dict, token_name+".xlsx")
