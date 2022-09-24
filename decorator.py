#デコレータを使わずに関数の内容を修正
def print_passage(func): # 関数を引数に受け取る関数内関数 #ここでのfuncはadd_calcに相当
  def passage(*args, **kwargs):
    print('計算を開始します')
    result = func(*args, *kwargs)
    print('計算が終了しました。結果を表示します。')
    return result
  return passage

def add_calc(a,b):
  return a + b

f = print_passage(add_calc) #print_passageはオブジェクトpassageを返す
r = f(5,10) #passageは可変長引数を受け取れる
print(r) #add_cals()に、文章を表示させる機能を追加した

#デコレータを使って関数の内容を修正
def print_passage(func): # 関数を引数に受け取る関数内関数 #ここでのfuncはadd_calcに相当
  def passage(*args, **kwargs):
    print('計算を開始します')
    result = func(*args, *kwargs)
    print('計算が終了しました。結果を表示します。')
    return result
  return passage # passage()を定義しないと、print部分が出力されない。passage()の定義部分で定義したことを丸っと出力したいから、passage()を定義している

@print_passage #デコレートしたい関数の上に@でデコレート関数名を書くだけでいい
def add_calc(a,b):
  return a + b

r = add_calc(10,100) #呼び出し時も、元の関数を呼び出すように書けばいい
print(r)