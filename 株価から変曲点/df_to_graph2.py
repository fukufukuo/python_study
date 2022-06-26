# 【前ファイル】csv_seikei.py
# 【後ファイル】

#たくさんのデータが含まれているcsvから、高値のデータのみグラフ化する

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#csv_seikei.pyで整形したcsvを読み込む
df = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data_renamed.csv")

#いったんそのままグラフ化
#df.plot() #plot()自体はpandasのモジュール。返ってくるのはmatplotlibのオブジェクト。 
#plt.show() #こっちはmatplotlibのモジュール  #全ての列がプロットされる

#x軸に日付、y軸を高値としてplot
df.plot(x='date', y='high_value')
plt.show() #できてはいるけど、日付が降順になっているのがイケてない

#日付が昇順になるように並び替える
df_sorted = df.sort_values(by='date')
print(df_sorted.head())

df_sorted.plot(x='date', y='high_value')
plt.show()

#ok!
