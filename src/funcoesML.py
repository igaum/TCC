import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# realiza:
# - a separação de variaveis dependentes e independentes,
# - cria um modelo Random Forest,
# - o fit() nesse modelo com os dados de treinamento,
# - gera previsões e calcula métricas com base nessas previsões
def Calcula_metricas_random_forest(df_teste, df_treinamento, cod_materia='0'):

    # pega as colunas das variaveis independentes
    X_teste = df_teste.iloc[:, :-10]
    X_treinamento = df_treinamento.iloc[:, :-10]

    # cria o modelo de regressão e realiza o fit
    regressor = RandomForestRegressor()

    # se materia = 0, o Random Forest irá prever todas as matérias em uma única execução
    if cod_materia == '0':
        Y_teste = df_teste.iloc[:, 11:]
        Y_treinamento = df_treinamento.iloc[:, 11:]

        regressor.fit(X_treinamento, Y_treinamento)

    # se não, o teste será realizado somente com a matéria informada
    else:
        Y_teste = df_teste[cod_materia].to_frame()
        Y_treinamento = df_treinamento[cod_materia].to_frame()

        regressor.fit(X_treinamento, Y_treinamento.values.ravel())

    # realiza as previsões
    previsoes = regressor.predict(X_teste)

    # decide o nome do arquivo para salvar as previsões. Se for matéria única, salva com o nome da matéria
    if cod_materia == '0':
        nome_arquivo = "previsoes.csv"
        colunas = ['C', 'Q', 'B', 'M', 'G', 'H', 'S', 'F', 'P', 'L']
    else:
        nome_arquivo = "previsoes " + cod_materia + ".csv"
        colunas = [cod_materia]

    # salva as previsões
    res_previsoes = pd.DataFrame(previsoes, columns=colunas).to_csv(nome_arquivo, index=False)

    # imprime as métricas MSE e MAE
    print("MSE: ", mean_squared_error(Y_teste, previsoes))
    print("MAE: ", mean_absolute_error(Y_teste, previsoes))


def Previsao_uma_materia_por_vez(df_teste, df_treinamento):
    materias = ['C', 'Q', 'B', 'M', 'G', 'H', 'S', 'F', 'P', 'L']

    for materia in materias:
        print("Métricas da materia ", materia, ": ")
        Calcula_metricas_random_forest(df_teste, df_treinamento, cod_materia=materia)
        print("\n")
