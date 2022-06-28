# 【前ファイル】 df_to_graph2.py
# 【後ファイル】

# 高値の変化率を計算し、その結果を表示する列をdataframeに追加する

import pandas as pd

# csv読み込み
csv_path = "C:\Python_study\株価から変曲点\shokki_stock_data_renamed.csv"
df = pd.read_csv(csv_path)

# いったん確認
print(df.head())

# 差分計算列を追加
# diff()で、一行前の値との差分を計算できる
df['high_sabun'] = df['high_value'].diff()

# 列が追加されているか確認
print(df.head())

# 変化率計算列を追加
# pct_change()で、一行前の値に対しての変化率を計算できる
df['high_change_rate'] = df['high_value'].pct_change()

# 列が追加されているか確認
print(df.head())

