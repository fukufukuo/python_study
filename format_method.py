import cmd

name = 'ふくお'
print('私の名前は{}です'.format(name))

year = 1995
month = 9
day = 18
print('彼女の誕生日は{0}年{2}月{1}日です'.format(year, month, day))
#{}内の数字は、formatメソッド内のタプルのインデックスを示す {}内を空にしたら、引数で指定した順番に入っていく