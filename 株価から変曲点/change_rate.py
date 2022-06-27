# 【前ファイル】 df_to_graph2.py
# 【後ファイル】

# 高値の変化率を計算し、その結果を表示する列をdataframeに追加する

import pandas as pd

# csv読み込み
df = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data_renamed.csv")

# 空の列を追加
df['change_rate'] = df['start_value']*0

# 確認
print(df.head())