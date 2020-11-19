from dataclasses import dataclass


@dataclass
# dados sobre as provas e disciplinas
class Provas:
    # conjunto de códigos identificadores de cada caderno de prova em cada área
    # os codigos estão posicionados nas listas de modo onde cada posição representa um caderno de provas
    # por exemplo, cods_humanas_2018[2] e cods_codigos_2018[2] se referem a provas que existem no mesmo caderno
    cods_matemat_2018 = [459.0, 460.0, 462.0, 461.0, 466.0, 470.0, 499.0, 500.0, 501.0, 502.0]
    cods_naturez_2018 = [447.0, 448.0, 449.0, 450.0, 463.0, 467.0, 487.0, 488.0, 489.0, 490.0]
    cods_humanas_2018 = [451.0, 452.0, 453.0, 454.0, 464.0, 468.0, 491.0, 492.0, 493.0, 494.0]
    cods_codigos_2018 = [455.0, 456.0, 458.0, 457.0, 465.0, 469.0, 495.0, 496.0, 497.0, 498.0]

    cods_matemat_2019 = [515.0, 516.0, 518.0, 517.0, 522.0, 526.0, 555.0, 556.0, 557.0, 558.0]
    cods_naturez_2019 = [503.0, 504.0, 505.0, 506.0, 519.0, 523.0, 543.0, 544.0, 545.0, 546.0]
    cods_humanas_2019 = [507.0, 508.0, 509.0, 510.0, 520.0, 524.0, 547.0, 548.0, 549.0, 550.0, 564.0]
    cods_codigos_2019 = [511.0, 512.0, 514.0, 513.0, 521.0, 525.0, 551.0, 552.0, 553.0, 554.0, 565.0]

    # dicionários com vetores que armazenam as disciplinas de cada questão de cada prova, exceto:
    # matemática, pois é uma prova única
    # códigos e linguagens, pois a lingua estraigeira é definida e sempre são as 5 primeiras, o resto é Portugues
    disc_naturez_2018 = {447.0: 'QQQBQBQBQBBQCCQBBCQBBCBQCQBQBCBCBQCQBCCQCQBCQ',
                         448.0: 'BCBQBCQCQQQBCQBCQQCCQBQBBQCCQBBCBCQBQCQBCQCQQ',
                         449.0: 'CQCBCQBCQQBQBBBQCCQQBCQBBCQQCCBCCQQCQQQQBCBQB',
                         450.0: 'QBCQQCQQBCBCQQCCQQBCBCQBQBBCQBBQCCQBCBQBQQCQC',
                         463.0: 'BCBQBCQCQQQBCQBCQQCCQBCBBQCCQBBCBCQBCCQBCQCQQ',
                         467.0: 'BCBQBCQCQQQBCQBCQQCCQBQBBQCCQBBCBCQBQCQBCQCQQ',
                         487.0: 'BCBCCQQCBQBQBCBQCCQQCQCQBQCQQQBCBQQCCCBCQBBQQ',
                         488.0: 'CQQCBQQQBCBCCQBBQQQQBQCQCQCBCBQQCCQBQBCCCBBQC',
                         489.0: 'CQBBQQBQBCCCBQCQCQCQQQBCBQQBQCCQBQBCBCBQCCQQC',
                         490.0: 'QQCQBBCCBQCQCQCQBQCBCBQQQQCQBQCQQCBQCBQBCBCBC'}

    disc_humanas_2018 = {451.0: 'GSSFHFFGHHGHHHSHSGHGFGHHSHGGHSHGSFSSGFHHGSGGF',
                         452.0: 'GHGHGSFSSGFGSSFHHHSHFFGHSGHGGFHHGSGHSSHSHGHHG',
                         453.0: 'HHGHSHGGHSSHFFGGFGHGSFSSGSSFSHHSGGFHHGSGFHGGH',
                         454.0: 'GGFHHGSGFGSFSSGHSHHSHGSHHSHSGSGHGHHHGHFFGGHFF',
                         464.0: 'GSSFHFFGHHGHHHSHSGHGFGHHSHGGHSHGSFSSGFHHGSGGF',
                         468.0: 'GSSFHFFGHHGHHHSHSGHGFGHHSHGGHSHGSFSSGFHHGSGGF',
                         491.0: 'FGHHGGHGGSHSHSHFHHGGSSSSHFGFSFSSHFGSSFGGGGGGF',
                         492.0: 'GGSGGGSGFGHHHSHSSSSHSSHFGSGFGSHFSGSGHFHHFGHSS',
                         493.0: 'SGGSGFGGSFGHSSSSHFGSHFFHHSHHFHHHSHSFGSHGGFGHG',
                         494.0: 'GSGFHFHFGGGSGSSSHGSHFSSSHFHSHSFGSSSGGFGSGFGSH'}

    disc_naturez_2019 = {503.0: 'QCBCQBBBBBBCQQQCBQCBCQQBQBCQCQCQBQBCBQQQCCBQC',
                         504.0: 'CBQQCBCQQCQBBBBBCQQBQBCQQQCBQCBCQCQBQBBBQCQQC',
                         505.0: 'BBQCQQCQBCQBCBQCQQCQBCQQQCBCQBQCBCQQBQBBBBQCB',
                         506.0: 'BBBBCQQCBCBQQQCBCQBQCBCQQBQBCQQQCBBQCCQQCQBQB',
                         519.0: 'BBQCQQCQBCQBCBQCQBCQBCQBQCBCQBQCBCQQBCBBBBQCB',
                         523.0: 'BBQCQQCQBCQBCBQCQQCQBCQQQCBCQBQCBCQQBQBBBBQCB',
                         543.0: 'CBQQQBQBBCQBCBBQCBCQBQQBCQBCQCBQQQQBBQBBBCQBB',
                         544.0: 'BCQBBBQBBBBQBQQBQQBCBCQBQQCBBQCCBCQBQBBQQBCBQ',
                         545.0: 'CBBQBQQQBCBCQQBCBQQBBCQBBQBBBQQBBCQBBQQBQCBQC',
                         546.0: 'CQBBQCCQQBQBCQBBBQQBBQBBQBBCBQQQBQBQQQBCBCBCB'}

    disc_humanas_2019 = {507.0: 'GGGGSFHSHHGGFGHSSHFFSFHSFSFSFGHGFHHHHSHHHSGGS',
                         508.0: 'GFHGHSFHGHGSHFSHGGFGFSHSFFHHHSGGGGGFGSFSHFSFH',
                         509.0: 'FSFGFFSHFSFHSHSFHHSSGGGGFGSFGHGHGHGGFGFSHGFHH',
                         510.0: 'GGHFGFSFHSSHSFHGSFGHGHHSGGSGGFGFSFGGFFHHGHGGF',
                         520.0: 'SFHGHSFHGHGSHGHHGGFGFSFHFHHHHSGGSGGFGSFFHFSFG',
                         524.0: 'SFHGHSFHGHGSHGHHGGFGFSFHFHHHHSGGSGGFGSFFHFSFG',
                         547.0: 'FSHSHHFFHHFSGHGSFGGHHSSHHSSFGSHGGSSFFFGSGGGGF',
                         548.0: 'GGGGFFFFGSSGGSHSFGSSHHSGHHSGSFGGHHSFGSHFFFFHS',
                         549.0: 'GHGHHSHSFGSHHSFFHSHSFGHHFFGGGFFFFGGSGGSHFFHSH',
                         550.0: 'FSFGSSGSHFFGSSGGGFGHSFFGGHHFFFFHSSSHSSHHSGGFG',
                         564.0: 'FFHSHHFFHSFGGHGSFGGHHSFHHSSFGFSGGSHFFHGSGGGGF'}
