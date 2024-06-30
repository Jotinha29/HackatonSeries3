import pandas as pd
from sqlalchemy import create_engine
import pymysql

db_user = 'seu_usuario'
db_password = 'sua_senha'
db_host = 'localhost'
db_port = '3306'
db_name = 'legislativo'

def criar_banco_de_dados():
    connection = pymysql.connect(user=db_user, password=db_password, host=db_host, port=int(db_port))
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.close()
    connection.close()

criar_banco_de_dados()

db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)

def salvar_dados_no_banco(df, tabela_nome):
    try:
        df.to_sql(tabela_nome, con=engine, if_exists='replace', index=False)
        print(f"Dados salvos com sucesso na tabela {tabela_nome}.")
    except Exception as e:
        print(f"Erro ao salvar dados na tabela {tabela_nome}: {e}")
