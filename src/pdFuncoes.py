import pandas as pd


# Exibe todas as linhas e colunas no print() se modo == True
# Usar quando não for exibir milhões de dados, pois consome muita RAM
def exibir_max_linhas_e_colunas(modo):
    if modo:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_seq_items', None)
    else:
        pd.set_option('display.max_columns', 10)
        pd.set_option('display.max_rows', 10)


# deleta linhas onde o valor da coluna informada é nulo
def deleta_nulos(dataframe, coluna):
    indexes = dataframe[pd.isnull(dataframe[coluna])].index
    dataframe.drop(indexes, inplace=True)


def print_nulos(dataframe):
    print(dataframe.isna().sum())
