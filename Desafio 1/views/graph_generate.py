import pygal
from pygal.style import Style
import os
from utils.directory_creator import verificar_e_criar_diretorio


def gerar_graficos(df, x_col, y_col, title, filename):
    try:
        # Verificar e criar diretório se necessário
        diretorio = os.path.dirname(filename)
        verificar_e_criar_diretorio(diretorio)

        custom_style = Style(
            background='white',
            plot_background='white',
            foreground='#53E89B',
            foreground_strong='#05334A',
            foreground_subtle='#630C0D',
            opacity='.6',
            opacity_hover='.9',
            transition='400ms ease-in',
            colors=('#E80080', '#404040', '#9BC850', '#FF6E4A', '#6ECB63')
        )

        bar_chart = pygal.Bar(style=custom_style)
        bar_chart.title = title

        # Contagem de valores com base nos eixos fornecidos
        data_count = df.groupby(x_col)[y_col].count().sort_index()

        bar_chart.add(y_col, data_count.values)
        bar_chart.x_labels = data_count.index

        bar_chart.render_to_file(filename)

        print(f"Gráfico salvo com sucesso em {filename}")
    except Exception as e:
        print(f"Erro ao gerar gráfico: {e}")
