# 作成日 2022-06-29

import pandas as pd


# 変数設定
read_folder = R"C:\Python_study\複数csvをひとつのexcelにまとめる\data"
read_file_list = ['shokki_stock_data_1', 'shokki_stock_data_2', 'shokki_stock_data_3']
output_path = R"C:\Python_study\複数csvをひとつのexcelにまとめる\output\output.xlsx"

# ループさせながら読み込む
for name in read_file_list:
  read_path = read_folder + '\\' + name + '.csv'
  df = pd.read_csv(read_path)

  # outputのエクセルに新規シートを作成し、dfを貼り付ける
  # ExcelWriter()を使う
  # エクセルファイルを新規作成する場合と、既存のエクセルに新規シートを追加する場合で書き方が違う(mode='a')ので、
  # 今回はあらかじめエクセルファイルを作成し、既存のエクセルに新規シートを追加する方針で行く。
  with pd.ExcelWriter(output_path, mode='a') as writer :
    df.to_excel(writer, sheet_name=name)

# 一発でできちゃった。ループ文一発で書けると気持ちいい。