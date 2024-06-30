import pandas as pd

def gerar_sql(df, arquivo_sql, tabela_nome):
    try:
        with open(arquivo_sql, 'w') as f:
            for index, row in df.iterrows():
                values = ', '.join([f"'{str(value)}'" for value in row.values])
                sql = f"INSERT INTO {tabela_nome} ({', '.join(df.columns)}) VALUES ({values});\n"
                f.write(sql)
        print(f"Arquivo SQL gerado com sucesso: {arquivo_sql}")
    except Exception as e:
        print(f"Erro ao gerar arquivo SQL: {e}")
