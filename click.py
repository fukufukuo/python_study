import click

@click.command() #修飾した関数はclickのコマンドとなる
@click.option('--count:,' default = 1, help='Number of greetings.') #変数countを設定
def hello(count):
  for x in 
  click.echo('Hello click!')

if __name__ == '__main__': #このファイルがスクリプトとして実行された時
  hello() 
