import pandas as pd
##simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
##print(simpsons[1])
df_permier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

df_permier21.rename(columns={'FTHG':'HG','FTAG':'AG'}, inplace=True)
print(df_permier21)