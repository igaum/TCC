import pandas as pd
from dataclass import Provas


# separa uma base de dados em teste e treinamento
def separador(base, tamanho_teste):
    db_teste = open("teste.csv", "w", encoding="latin 1")  # cria a DB de testes
    db_treinamento = open("treinamento.csv", "w", encoding="latin 1")  # cria a DB de treinamento

    primeira_linha = base.readline()
    db_teste.write(primeira_linha)
    db_treinamento.write(primeira_linha)

    i = 0

    for linha in base:
        i += 1
        if i < tamanho_teste:
            db_teste.write(linha)
        else:
            db_treinamento.write(linha)

    base.close()
    db_teste.close()
    db_treinamento.close()


# verifica se os códigos das provas estão consistentes e se batem com os cadernos de provas
def verificaCodsDeProvas(db_teste):
    for ind in db_teste.index:

        naturez = db_teste['CO_PROVA_CN'][ind]
        matemat = db_teste['CO_PROVA_MT'][ind]
        humanas = db_teste['CO_PROVA_CH'][ind]
        codigos = db_teste['CO_PROVA_LC'][ind]

        if db_teste['NU_ANO'][ind] == 2018:
            if Provas.cods_naturez_2018.index(naturez) != Provas.cods_matemat_2018.index(matemat):
                print("inconsistência na prova de exatas")
                print("combinação: ", naturez, ", ", matemat)

            if Provas.cods_humanas_2018.index(humanas) != Provas.cods_codigos_2018.index(codigos):
                print("inconsistência na prova de humanas")
                print("combinação: ", humanas, ", ", codigos)

        elif db_teste['NU_ANO'][ind] == 2019:
            if Provas.cods_naturez_2019.index(naturez) != Provas.cods_matemat_2019.index(matemat):
                print("inconsistência na prova de exatas")
                print("combinação: ", naturez, ", ", matemat)

            if Provas.cods_humanas_2019.index(humanas) != Provas.cods_codigos_2019.index(codigos):
                print("inconsistência na prova de humanas")
                print("combinação: ", humanas, ", ", codigos)
        else:
            print("Ano incorreto")


# utiliza as respostas dadas pelos alunos, os gabaritos e os indicativos das disciplinas
# para calcular as notas de cada aluno em cada disciplina, e no final salva em uma nova DB
def CalculaNotas(db_teste):
    # Definição das colunas da base de dados final
    db_final = pd.DataFrame(columns=['TP_SEXO', 'TP_ST_CONCLUSAO', 'TP_ESCOLA', 'NU_IDADE', 'TP_ESTADO_CIVIL',
                                     'TP_ANO_CONCLUIU', 'TP_DEPENDENCIA_ADM_ESC', 'Q005', 'Q006', 'Q024', 'Q025',
                                     'C', 'Q', 'B', 'M', 'G', 'H', 'S', 'F', 'P', 'L'])

    for ind in db_teste.index:

        # armazena os dados do aluno que serão inclusos da BD final + as notas que serão calculadas a seguir
        aluno = {'TP_SEXO': db_teste['TP_SEXO'][ind],
                 'TP_ST_CONCLUSAO': db_teste['TP_ST_CONCLUSAO'][ind],
                 'TP_ESCOLA': db_teste['TP_ESCOLA'][ind],
                 'NU_IDADE': db_teste['NU_IDADE'][ind],
                 'TP_ESTADO_CIVIL': db_teste['TP_ESTADO_CIVIL'][ind],
                 'TP_ANO_CONCLUIU': db_teste['TP_ANO_CONCLUIU'][ind],
                 'TP_DEPENDENCIA_ADM_ESC': db_teste['TP_DEPENDENCIA_ADM_ESC'][ind],
                 'Q005': db_teste['Q005'][ind],
                 'Q006': db_teste['Q006'][ind],
                 'Q024': db_teste['Q024'][ind],
                 'Q025': db_teste['Q025'][ind],
                 'C': 0, 'Q': 0, 'B': 0, 'M': 0, 'G': 0, 'H': 0, 'S': 0, 'F': 0, 'P': 0, 'L': 0}

        # IDs de prova
        cod_naturez = db_teste['CO_PROVA_CN'][ind]
        cod_humanas = db_teste['CO_PROVA_CH'][ind]

        # Respostas dadas pelo aluno
        res_naturez = db_teste['TX_RESPOSTAS_CN'][ind]
        res_matemat = db_teste['TX_RESPOSTAS_MT'][ind]
        res_humanas = db_teste['TX_RESPOSTAS_CH'][ind]
        res_codigos = db_teste['TX_RESPOSTAS_LC'][ind]

        # gabaritos das provas feitas pelo aluno
        gab_naturez = db_teste['TX_GABARITO_CN'][ind]
        gab_matemat = db_teste['TX_GABARITO_MT'][ind]
        gab_humanas = db_teste['TX_GABARITO_CH'][ind]
        gab_codigos = db_teste['TX_GABARITO_LC'][ind]

        # lingua estrangeira selecionada e ano de realização da prova
        lingua_est = db_teste['TP_LINGUA'][ind]
        ano_inscricao = db_teste['NU_ANO'][ind]

        # passa por todas as questões das 4 provas, verificando se a resposta do aluno está correta e se estiver,
        # verifica a qual disciplina ela pertence e adiciona um ponto a essa disciplina em 'notas[]'
        for questao in range(45):

            if ano_inscricao == 2018:
                if res_naturez[questao] == gab_naturez[questao]:
                    aluno[Provas.disc_naturez_2018[cod_naturez][questao]] += 1
                if res_matemat[questao] == gab_matemat[questao]:
                    aluno['M'] += 1
                if res_humanas[questao] == gab_humanas[questao]:
                    aluno[Provas.disc_humanas_2018[cod_humanas][questao]] += 1

            else:
                if res_naturez[questao] == gab_naturez[questao]:
                    aluno[Provas.disc_naturez_2019[cod_naturez][questao]] += 1
                if res_matemat[questao] == gab_matemat[questao]:
                    aluno['M'] += 1
                if res_humanas[questao] == gab_humanas[questao]:
                    aluno[Provas.disc_humanas_2019[cod_humanas][questao]] += 1

            if questao < 5:  # as 5 primeiras questões da prova de linguagem são de lingua estrangeira
                if lingua_est == 0:  # Inglês
                    if res_codigos[questao] == gab_codigos[questao]:
                        aluno['L'] += 1
                else:  # Espanhol
                    if res_codigos[questao] == gab_codigos[questao + 5]:  # o gabarito de espanhol comaça na q. 6
                        aluno['L'] += 1

            else:  # restante da prova de linguagem
                if res_codigos[questao] == gab_codigos[questao + 5]:
                    aluno['P'] += 1

        # inclui o aluno na database
        db_final = db_final.append(aluno, ignore_index=True)

    db_final.to_csv("Base final.csv", sep=";", encoding="latin 1", index=False)


# como o Sklearn não aceita strings, o que é string deve ser convertido para int ou float
def TranformaString(base):
    db_final = pd.DataFrame(columns=['TP_SEXO', 'TP_ST_CONCLUSAO', 'TP_ESCOLA', 'NU_IDADE', 'TP_ESTADO_CIVIL',
                                     'TP_ANO_CONCLUIU', 'TP_DEPENDENCIA_ADM_ESC', 'Q005', 'Q006', 'Q024', 'Q025',
                                     'C', 'Q', 'B', 'M', 'G', 'H', 'S', 'F', 'P', 'L'])

    for ind in base.index:

        # armazena os dados do aluno que serão inclusos da BD final, inicializando com 0 o que será convertido
        aluno = {'TP_SEXO': 0, 'Q006': 0, 'Q024': 0, 'Q025': 0,
                 'TP_ST_CONCLUSAO': base['TP_ST_CONCLUSAO'][ind],
                 'TP_ESCOLA': base['TP_ESCOLA'][ind],
                 'NU_IDADE': base['NU_IDADE'][ind],
                 'TP_ESTADO_CIVIL': base['TP_ESTADO_CIVIL'][ind],
                 'TP_ANO_CONCLUIU': base['TP_ANO_CONCLUIU'][ind],
                 'TP_DEPENDENCIA_ADM_ESC': base['TP_DEPENDENCIA_ADM_ESC'][ind],
                 'Q005': base['Q005'][ind],
                 'C': base['C'][ind], 'Q': base['Q'][ind],
                 'B': base['B'][ind], 'M': base['M'][ind], 'G': base['G'][ind],
                 'H': base['H'][ind], 'S': base['S'][ind], 'F': base['F'][ind],
                 'P': base['P'][ind], 'L': base['L'][ind]}

        # 'TP_SEXO' e 'Q025' sao binários, então a verificação será somente um IF
        if base['TP_SEXO'][ind] == 'F':
            aluno['TP_SEXO'] = 1

        if base['Q025'][ind] == 'B':
            aluno['Q025'] = 1

        # 'Q024' e 'Q006' são de multipla escolha, então será atribuído um número para cada escolha
        q24 = ['A', 'B', 'C', 'D', 'E']
        aluno['Q024'] = q24.index(base['Q024'][ind])

        q06 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
        aluno['Q006'] = q06.index(base['Q006'][ind])

        # inclui o aluno na database
        db_final = db_final.append(aluno, ignore_index=True)

    db_final.to_csv("Base convertida.csv", sep=";", encoding="latin 1", index=False)
