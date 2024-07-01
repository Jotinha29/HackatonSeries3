import pandas as pd


def coletar_dados_senado(req):
    url_senado = "https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "sigla": "PL",
        "ano": 2023,
        "itens": 1,  # Limitando a 10 itens por página
        "ordenarPor": "id"
    }
    all_proposicoes_senado = []
    max_paginas = 10

    try:
        for pagina in range(1, max_paginas + 1):
            params["pagina"] = pagina
            try:
                response_senado = req.get(url_senado, headers=headers, params=params)
                response_senado.raise_for_status()  # Lança exceção se a resposta não for bem-sucedida
            except req.exceptions.HTTPError as http_err:
                print(f'Erro HTTP ao acessar a API do Senado Federal na página {pagina}: {http_err}')
                continue
            except req.exceptions.RequestException as req_err:
                print(f'Erro ao fazer a requisição para a API do Senado Federal na página {pagina}: {req_err}')
                continue

            try:
                data_senado = response_senado.json()
            except ValueError as json_err:
                print(f'Erro ao analisar o JSON da resposta na página {pagina}: {json_err}')
                continue

            if response_senado.status_code == 200 and "Materias" in data_senado.get('PesquisaBasicaMateria', {}):

                proposicoes_senado = [
                    proposicao for proposicao in data_senado['PesquisaBasicaMateria']['Materias']['Materia']
                    if proposicao['Sigla'] == 'PL'
                ]
                all_proposicoes_senado.extend(proposicoes_senado)
            else:
                break

    except Exception as err:
        print(f'Erro inesperado ao acessar a API do Senado Federal: {err}')

    df_senado = pd.DataFrame(all_proposicoes_senado)
    return df_senado
