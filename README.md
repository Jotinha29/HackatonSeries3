# Script Python para Coleta de Dados Legislativos, Geração de SQL e Geração de Gráficos 🐍📊

## Visão Geral
Este script Python foi desenvolvido para coletar dados de duas APIs legislativas brasileiras (Câmara dos Deputados e Senado Federal), gerar arquivos SQL a partir dos dados coletados e criar representações gráficas utilizando Pygal.

## Componentes

1. **Funções de Coleta de Dados**
   - **`coletar_dados_camara(req)`**: Obtém dados de proposições legislativas da API da Câmara dos Deputados (`https://dadosabertos.camara.leg.br/api/v2/proposicoes`). Filtra proposições do tipo "PL" para o ano de 2023.
   - **`coletar_dados_senado(req)`**: Recupera dados de proposições legislativas da API do Senado Federal (`https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista`). Também filtra proposições do tipo "PL" para o ano de 2023.

2. **Geração de SQL**
   - **`gerar_sql(df, file_path, table_name)`**: Gera arquivos SQL a partir dos DataFrames obtidos das APIs legislativas. Converte as linhas do DataFrame em declarações SQL INSERT e salva nos arquivos especificados (`proposicoes_camara.sql` e `proposicoes_senado.sql`).

3. **Geração de Gráficos**
   - **`gerar_graficos(df, x_col, y_col, title, filename)`**: Utiliza Pygal para criar gráficos de barras baseados nos dados extraídos das APIs legislativas. A função aceita DataFrames (`df`) e parâmetros (`x_col`, `y_col`, `title`, `filename`) para gerar arquivos SVG representando o número de proposições legislativas por ano para ambas as câmaras (Câmara dos Deputados e Senado Federal).

4. **Execução Principal (`main()` function)**
   - Inicializa uma sessão `requests.Session()` para gerenciar requisições HTTP.
   - Chama `coletar_dados_camara()` e `coletar_dados_senado()` para buscar dados nas respectivas APIs.
   - Exibe os DataFrames coletados (`df_camara` e `df_senado`) no console.
   - Chama `gerar_sql()` para gerar arquivos SQL (`proposicoes_camara.sql` e `proposicoes_senado.sql`).
   - Chama `gerar_graficos()` para criar arquivos SVG (`proposicoes_por_ano_camara.svg` e `proposicoes_por_ano_senado.svg`) representando o número de proposições por ano.

5. **Tratamento de Erros**
   - Implementa tratamento básico de erros usando blocos try-except para capturar e imprimir exceções que possam ocorrer durante a coleta de dados, geração de SQL ou geração de gráficos.

6. **Utilitário de Criação de Diretórios**
   - **`verificar_e_criar_diretorio(caminho)`**: Função utilitária para verificar se um diretório existe no caminho especificado. Se não existir, cria o diretório.

## Requisitos
- Python 3.x
- Pandas (`pip install pandas`)
- Pygal (`pip install pygal`)

## Uso
1. Certifique-se de que o Python e as bibliotecas necessárias estão instalados.
2. Execute o script (`python nome_do_script.py`).
3. O script irá buscar dados nas APIs, gerar arquivos SQL e criar arquivos SVG para visualizações nos diretórios especificados.

## Observações
- Ajuste os caminhos (`file_path`, `filename`) de acordo com a estrutura e permissões do seu diretório.
- Personalize os parâmetros da função `gerar_graficos()` (`x_col`, `y_col`, `title`, `filename`) conforme as necessidades específicas de visualização do seu projeto.

Este README fornece uma visão geral do script Python para coleta de dados legislativos, geração de arquivos SQL e criação de representações gráficas. Ajuste e expanda as funcionalidades conforme os requisitos do seu projeto.
