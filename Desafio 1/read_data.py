import requests
import pandas as pd

def coletar_dados_camara():
    url_camara = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    params = {
        "siglaTipo": "PL",
        "ano": 2023,
        "itens": 100,
        "ordenarPor": "id"
    }
    all_proposicoes_camara = []
    pagina = 1

    while True:
        params["pagina"] = pagina
        response_camara = requests.get(url_camara, params=params)
        data_camara = response_camara.json()

        if response_camara.status_code == 200 and data_camara['dados']:
            proposicoes_camara = data_camara['dados']
            all_proposicoes_camara.extend(proposicoes_camara)
            pagina += 1
        else:
            break

    df_camara = pd.DataFrame(all_proposicoes_camara)
    return df_camara

def coletar_dados_senado():
    url_senado = "https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista"
    params = {
        "sigla": "PL",
        "ano": 2023,
        "itens": 100,
        "ordenarPor": "id"
    }
    all_proposicoes_senado = []
    pagina = 1

    while True:
        params["pagina"] = pagina
        response_senado = requests.get(url_senado, params=params)
        data_senado = response_senado.json()

        if "Materia" in data_senado['ListaMaterias']:
            proposicoes_senado = data_senado['ListaMaterias']['Materia']
            all_proposicoes_senado.extend(proposicoes_senado)
            pagina += 1
        else:
            break

    df_senado = pd.DataFrame(all_proposicoes_senado)
    return df_senado
