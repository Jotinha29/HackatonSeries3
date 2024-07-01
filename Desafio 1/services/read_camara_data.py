import pandas as pd


def coletar_dados_camara(req):
    url_camara = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    headers = {
        "Accept": "application/json"
    }
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
            try:
                response_camara = req.get(url_camara, headers=headers, params=params)
                response_camara.raise_for_status()  # Lança exceção se a resposta não for bem-sucedida
            except req.exceptions.HTTPError as http_err:
                print(f'Erro HTTP ao acessar a API da Câmara dos Deputados na página {pagina}: {http_err}')
                continue
            except req.exceptions.RequestException as req_err:
                print(f'Erro ao fazer a requisição para a API da Câmara dos Deputados na página {pagina}: {req_err}')
                continue

            try:
                data_camara = response_camara.json()
            except ValueError as json_err:
                print(f'Erro ao analisar o JSON da resposta na página {pagina}: {json_err}')
                continue

            if response_camara.status_code == 200 and data_camara.get('dados'):
                proposicoes_camara = [proposicao for proposicao in data_camara['dados'] if
                                      proposicao['siglaTipo'] == 'PL']
                all_proposicoes_camara.extend(proposicoes_camara)
            else:
                break

    except Exception as err:
        print(f'Erro inesperado ao acessar a API da Câmara dos Deputados: {err}')

    df_camara = pd.DataFrame(all_proposicoes_camara)
    return df_camara
