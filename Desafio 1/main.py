from read_data import coletar_dados_camara, coletar_dados_senado
from data_to_DB import gerar_sql

def main():
    df_camara = coletar_dados_camara()
    df_senado = coletar_dados_senado()
    
    gerar_sql(df_camara, 'proposicoes_camara.sql', 'proposicoes_camara')
    gerar_sql(df_senado, 'proposicoes_senado.sql', 'proposicoes_senado')

if __name__ == "__main__":
    main()
