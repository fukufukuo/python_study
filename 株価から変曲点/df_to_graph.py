# 【前ファイル】read_stock_data.py
# 【後ファイル】csv_seikei.py

#read_stock.pyで読み込んだファイルをグラフ化する

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# データ読み込み
data = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data.csv")

# いったんノリで書いてみる
# plt.plot(data)
# もちろんだめ

# pd.dataframeから、plot()メソッドを呼び出すと描画できるらしい。
# そもそもdataってどんなtype何だろうか、確認。
print(type(data)) #<class 'pandas.core.frame.DataFrame'>

# てことは、これでいける？
data.plot()
plt.show()
# なんか出てきたけど、どこのグラフを描いているのか不明。
#後で理解するために、このグラフを保存しておく。
#data.plot()
#plt.savefig("C:\Python_study\株価から変曲点/first-figure.jpg")

#前日比と貸借倍率の列のみグラフ化されている・・なぜ？
#他の列はすべてセルの表示形式が通貨になっている。全部標準にしないといけない。
#やることが増えてきているので、いったんここでこのファイルは終わり。まずcsvの整形をする