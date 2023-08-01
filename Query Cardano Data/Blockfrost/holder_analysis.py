import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import read_csv
from token_info import asset_info
from project_data import project_wallets

# Token information to be queried and analyzed
policy_id = "da8c30857834c6ae7203935b89278c532b3995245295456f993e1d24"
asset_name = "4c51"
token_name = bytearray.fromhex(asset_name).decode()

df_holder = read_csv(token_name+"_holders.csv")

# Remove wallets associated with project (ie non-protocol user wallets)
project_wallets = [
    "addr1xxawr298yy36qrqw6yqc9v2qvgfddwjpqkgnfkt2rvq3u3f74zdzpgetwrygga9mlz44dc5tfrd82m0vxpfjmkpsf9ts06jfwd",
    "addr1x85etkeguzkemwfxtjtnl3ysp8fdmrjcdhsyp645y8ghwt4fp42lutam2alc7dzukvxgkxq0wd4aphv4zwczey39dysqy6rd7d",
    "addr1xxhrfw3fxavu9mzvh9ag8aja7uvhz70zqpf8m24gxash02s84wdjchweuj84lmg028rqft97snacuhs4cmvu9ywyhzcs3rxckm",
    "addr1x8q76ctyve23u8h5sux3npxwwlnedpxlz3ft89vlshhs5val9ytme40nlqwch8gxnrsk3cvt69qn8xuqsd2fuv7fgghqjct4kw",
]

df_project = df_holder.query("address in @project_wallets")
df_holder = df_holder.query("address not in @project_wallets")

print(f'The below wallets and amounts are tied to project wallets for {token_name} protocol')
print(df_project)

df_info = asset_info(policy_id, asset_name)
decimal = df_info['metadata.decimals'].iloc[0]
print(decimal)
total_supply = int(df_info['quantity'].iloc[0]) / 10**decimal
print(total_supply)

# Distribution of the token holders
df_holder['pct_supply'] = (df_holder['quantity']) / total_supply * 100
df_project['pct_supply'] = (df_project['quantity']) / total_supply * 100
project_supply = df_project['pct_supply'].sum()
project_total = project_supply * total_supply / 100
holder_supply = df_holder['pct_supply'].sum() 
holder_total = holder_supply * total_supply / 100
df_holder = df_holder.sort_values(by='quantity', ascending=False).reset_index(drop=True)
df_holder['cumulative_sum'] = df_holder['quantity'].cumsum()
user_total = df_holder['cumulative_sum'].max()
df_holder['pct_total_for_users'] = df_holder['quantity'] / user_total
df_holder['user_cumulative_sum'] = df_holder['pct_total_for_users'].cumsum()
print(f'The {token_name} project controls {project_supply}% of the total supply of minted tokens equivalent to {project_total} {token_name}')
print(f'The {token_name} protocol users controls {holder_supply}% of the total supply of minted tokens equivalent to {holder_total} {token_name}')

print(df_holder.head(25))

def cumulative_plot(df):
    plt.plot(df_holder.index, df_holder['cumulative_sum'])
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.title('Cumulative Sum Plot')
    plt.grid(True)
    plt.show()

cumulative_plot(df_holder)