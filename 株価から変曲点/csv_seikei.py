# 【前ファイル】df_to_graph.py
# 【後ファイル】df_to_graph2.py

# csvを処理しやすくするために、データを数値にする
# 列名を英数字にする

import pandas as pd

# 変換前のcsv読み込み
# df = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data.csv")

# 始値のtypeを確認
# print(df["始値"].dtype)

# astype()メソッドを用いて、obj→intに変更
# df["始値_1"] = df["始値"].astype(int) # エラー吐く・・・

# 列名が追加されたことを確認
# print(df[0:0])

#2022/06/28 read_csv()時点で桁区切り文字を指定できるという情報を入手。試してみる
#thousandsパラメーターで桁区切り文字を指定してread_csv()
df = pd.read_csv("C:\Python_study\株価から変曲点\shokki_stock_data.csv", thousands=',')

# 始値のtypeを確認
# print(df["始値"].dtype) #float64になっている！！

#次に列名を変更
print(df.iat[0,1]) #8120.0

# 列名は変えられなさそうだけど、練習として要素の書き換えをやってみる
#print(df.head(3))
#df.iat[0,1] = 3084
#print(df.head(3)) # 書き変わっている！

# いったん現在の列名を確認
print(df.columns)

#始値をstart_valueに変更
df.rename(columns={'始値':'start_value'})
#確認
print(df.columns) # 変わっていない
# 新しいdfを指定してあげないといけない
df_new = df.rename(columns={'始値':'start_value'})
#確認
print(df_new.columns)
# まとめて変更
df_new = df.rename(columns={'日付':'date', '始値':'start_value','高値':'high_value', '安値': 'low_value', '終値': 'end_value', '前日比':'cmp_ytd',
'出来高':'volume', '売買代金':'baibai_daikin', '貸株残高':'kashikabu_zandaka', '融資残高':'yuushi_zandaka', '貸借倍率':'taishaku_bairitu', 
'逆日歩':'gyaku_nippo', '特別空売り料':'tokukara' })
#確認
print(df_new.columns)
print(df_new.head())
#csvとして保存
df_new.to_csv("C:\Python_study\株価から変曲点\shokki_stock_data_renamed.csv") 

#ok!
