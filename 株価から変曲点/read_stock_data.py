#【前ファイル】なし
#【後ファイル】df_to_graph.py
# shokki_stock.csvをndarrayとして読み込むまでを自力でやってみる

import numpy as np
import openpyxl as op

# op.load_workbook("C:\Python_study\株価から変曲点\shokki_stock_data.csv")
# ↑のようにすると、csvはエクセルじゃないので読み込まれない。
# csvを読み込むには、csvあるいはpandasをimportして読み込む。
# 今やりたいのはデータ解析なので、今回はpandasを利用して読み込む。

import pandas as pd

data = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data.csv")
print(data)
# ok!