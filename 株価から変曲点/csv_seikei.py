# 【前ファイル】df_to_graph.py
# 【後ファイル】

# csvを処理しやすくするために、データを数字にする
# 列名を英数字にする

import pandas as pd

# 変換前のcsv読み込み
df = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data.csv")

# 始値のtypeを確認
print(df["始値"].dtype)

# astype()メソッドを用いて、obj→intに変更
df["始値_1"] = df["始値"].astype(int) # エラー吐く・・・

# 列名が追加されたことを確認
print(df[0:0])