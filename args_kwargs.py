def print_hikisuu(*args, **kwargs):
  print('args:{}'.format(args)) #変数じゃなくて引数でもformatメソッドは使用できる
  print('kwargs:', kwargs) #kwargsは辞書形式なので、formatメソッドは利用できない
  return None

print_hikisuu('test')
print_hikisuu(fav='nuphy air 75', want='nuphy halo 65')