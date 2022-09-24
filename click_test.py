import click

@click.command() #修飾した関数はclickのコマンドとなる
def hello():
  click.echo('Hello click!')

if __name__ == '__main__': #このファイルがスクリプトとして実行された時
  hello() 
