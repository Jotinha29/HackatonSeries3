import os


def verificar_e_criar_diretorio(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"Diretório criado: {caminho}")
    else:
        print(f"Diretório já existe: {caminho}")
