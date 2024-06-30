from read_data import coletar_dados_camara, coletar_dados_senado
from data_to_DB import salvar_dados_no_banco

def main():
    # Coletando dados da Câmara dos Deputados
    df_camara = coletar_dados_camara()
    # Coletando dados do Senado Federal
    df_senado = coletar_dados_senado()
    
    # Salvando dados no banco de dados
    salvar_dados_no_banco(df_camara, 'proposicoes_camara')
    salvar_dados_no_banco(df_senado, 'proposicoes_senado')

if __name__ == "__main__":
    main()
