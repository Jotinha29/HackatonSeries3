import requests

# services imports
from services.read_camara_data import coletar_dados_camara
from services.read_senado_data import coletar_dados_senado

# data imports
from data.sql_generator import gerar_sql

# views imports
from views.graph_generate import gerar_graficos

import pandas as pd


def main():
    try:
        with requests.Session() as session:
            df_camara = coletar_dados_camara(session)
            df_senado = coletar_dados_senado(session)

            # Configurar pandas para mostrar o DataFrame completo
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', None)

            print("DF CAMARA - ", df_camara)
            print("DF SENADO - ", df_senado)

            gerar_sql(df_camara, 'data/camaraDB/proposicoes_camara.sql', 'proposicoes_camara')
            gerar_sql(df_senado, 'data/senadoDB/proposicoes_senado.sql', 'proposicoes_senado')

            # TODO: Quais eixos deve-se gerar o grafico?
            # Colunas do DF CAMARA -> uri/siglaTipo/codTipo/numero/ano
            # Colunas do DF SENADO -> Codigo/IdentificacaoProcesso/DescricaoIdentificacao/Sigla/Numero/Ano

            # Gerar gráficos
            gerar_graficos(df_camara, 'ano', 'siglaTipo', 'Proposições por Ano (Câmara)',
                           'views/graphs/camaraGraph/proposicoes_por_ano_camara.svg')
            gerar_graficos(df_senado, 'Ano', 'Sigla', 'Proposições por Ano (Senado)', 'views/graphs/senadoGraph/proposicoes_por_ano_senado.svg')


    except requests.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
