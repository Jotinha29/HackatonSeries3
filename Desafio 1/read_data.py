import requests
import pandas as pd

def coletar_dados_camara():
    url_camara = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    params = {
        "siglaTipo": "PL",
        "ano": 2023,
        "itens": 10,  # Limitando a 10 itens por página
        "ordenarPor": "id"
    }
    all_proposicoes_camara = []
    max_paginas = 10

    try:
        for pagina in range(1, max_paginas + 1):
            params["pagina"] = pagina
            response_camara = requests.get(url_camara, params=params)
            response_camara.raise_for_status()  # Lança exceção se a resposta não for bem-sucedida

            data_camara = response_camara.json()
            
            if response_camara.status_code == 200 and data_camara.get('dados'):
                proposicoes_camara = [proposicao for proposicao in data_camara['dados'] if proposicao['siglaTipo'] == 'PL']
                all_proposicoes_camara.extend(proposicoes_camara)
            else:
                break

    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP ao acessar a API da Câmara dos Deputados: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro ao fazer a requisição para a API da Câmara dos Deputados: {req_err}')
    except Exception as err:
        print(f'Erro inesperado ao acessar a API da Câmara dos Deputados: {err}')

    df_camara = pd.DataFrame(all_proposicoes_camara)
    return df_camara

def coletar_dados_senado():
    url_senado = "https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista"
    params = {
        "sigla": "PL",
        "ano": 2023,
        "itens": 10,  # Limitando a 10 itens por página
        "ordenarPor": "id"
    }
    all_proposicoes_senado = []
    max_paginas = 10

    try:
        for pagina in range(1, max_paginas + 1):
            params["pagina"] = pagina
            response_senado = requests.get(url_senado, params=params)
            response_senado.raise_for_status()  # Lança exceção se a resposta não for bem-sucedida

            data_senado = response_senado.json()
            
            if response_senado.status_code == 200 and "Materia" in data_senado.get('PesquisaBasicaMateria', {}):
                proposicoes_senado = [proposicao for proposicao in data_senado['PesquisaBasicaMateria']['Materia'] if proposicao['Sigla'] == 'PL']
                all_proposicoes_senado.extend(proposicoes_senado)
            else:
                break

    except requests.exceptions.HTTPError as http_err:
        print(f'Erro HTTP ao acessar a API do Senado Federal: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Erro ao fazer a requisição para a API do Senado Federal: {req_err}')
    except Exception as err:
        print(f'Erro inesperado ao acessar a API do Senado Federal: {err}')

    df_senado = pd.DataFrame(all_proposicoes_senado)
    return df_senado
