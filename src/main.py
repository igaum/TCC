import time  # para retornar o tempo de execução no final do programa
import pandas as pd
from funcoesML import Calcula_metricas_random_forest, Previsao_uma_materia_por_vez
import pdFuncoes
import funcoesDatabase

tempo_inicio = time.time()

# df_teste = pd.read_csv("teste.csv", sep=";", encoding="latin 1")
# df_treinamento = pd.read_csv("treinamento.csv", sep=";", encoding="latin 1")

# Previsao_uma_materia_por_vez(df_teste, df_treinamento)
# Calcula_metricas_random_forest(df_teste, df_treinamento)


print("\n--- execução realizada em %.7s segundos ---"
      % (time.time() - tempo_inicio))
