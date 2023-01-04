# importacao/analise de arquivo afd

arq = input("insira o nome .txt do arquivo AFD: ")

file = open(arq, 'r')
linhas = file.readlines()
busca = ["palavra"]
vetorBusca = []

# corre no arquivo
for linha in linhas:
    print("----")
    # cabecalho
    if linha[9] == "1":
        print("# cabecalho")#, linha[9], linha)
        print("CNPJ: ", linha[11:25])
        print("Empresa: ", linha[39:188])
        print("Data de geracao: ", linha[226:250])
        
    # incl ou alteracao
    if linha[9] == "2":
        print("# incl. ou alteracao")#, linha[9], linha)
        print("NSR: ", linha[0:9])
        print("CPF do Responsavel: ", linha[34:48])
        print("CNPJ: ", linha[49:63])
        print("Empresa: ", linha[77:227])
        print("data de gravacao: ", linha[10:34])

    # ajuste do relogio
    if linha[9] == "4":
        print("# ajuste do relogio")#, linha[9], linha)
        print("NSR: ", linha[0:9])
        print("CPF do responsavel: ", linha[58:69])
        print("Data antes: ", linha[10:34])
        print("Data apos:  ", linha[34:58])

    # incl ou alteracao empregado
    if linha[9] == "5":
        print("# incl ou alt. empregado ")#, linha[9], linha)
        print("NSR: ", linha[0:9])
        if linha[34] == "I":
            print("Inclusao")
        elif linha[34] == "A":
            print("Alteracao")
        else:
            print("Exclusao")
        print("CPF do empregado: ", linha[36:47])
        print("Nome do empregado: ", linha[47:99])
        print("CPF do responsavel: ", linha[103:114])
        print("data de gravacao: ", linha[10:34])

    # reg ponto no _REP-P_
    if linha[9] == "7":
        print("# Registro de ponto ")#, linha[9], linha)
        print("NSR: ", linha[0:9])
        print("CPF do empregado: ", linha[35:46])
        print("data de registro: ", linha[10:34])

