# importacao/analise de arquivo afd

# input("insira o nome .txt do arquivo AFD: ")

def toCpf(cpf):
    return('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]))

def toCnpj(cnpj):
    return('{}.{}.{}/{}-{}'.format(cnpj[:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:]))

"""
# Portaria 671
Registro na posição 10:
    1 - cabeçalho
    2 - inclusão ou alteração da ID da empresa
    3 - registro REP-C e REP-A
    4 - ajuste do relógio
    5 - inclusão, alt ou excl de emprgado no REP
    6 - eventos sensíveis do REP
    7 - registro REP-P

"""

file = open('afd3.txt', 'r')
linhas = file.readlines()
busca = ["ARTUR"]
vetorBusca = []
"""
         'q','w','e','r','t','y','u','i','o','p','a','s',
              'd','f','g','h','j','k','l','z','x','c','v','b',
              'n','m','1','2','3','4','5','6','7','8','9','0',
              '.',',',';',' ',':','-','+','=','?','/','Q','W',
              'E','R','T','Y','U','I','O','P','A','S','D',
              'F','G','H','J','K','L','Z','X','C','V','B',
              'N','M']
"""
#arquivo = input("Digite o nome do arquivo: ")
#termo = input("Digite o termo a buscar: ")

# contadores
contLinha = 1
regPonto = 0
emprAlt = 0
funcInc = 0
funcAlt = 0
funcExc = 0
contLinhaBusca = 0
batidaApp = 0
batidaWeb = 0
fusoSP = 0
fusoMT = 0


# corre no arquivo
for linha in linhas:
    print("----")
    # cabecalho
    if linha[9] == "1":
        print("# cabecalho")#, linha[9], linha)
        print("CNPJ: ", toCnpj(linha[11:25]))
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
        emprAlt += 1

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
        alteracao = ""
        if linha[34] == "I":
            alteracao = "Inclusao"
            funcInc += 1
        elif linha[34] == "A":
            alteracao = "Alteracao"
            funcAlt += 1
        else:
            alteracao = "Exclusao"
            funcExc += 1
        print("operacao: ", alteracao)
        print("CPF do empregado: ", linha[36:47])
        print("Nome do empregado: ", linha[47:99])
        print("CPF do responsavel: ", toCpf(linha[103:114]))
        print("data de gravacao: ", linha[10:34])

    # reg ponto no _REP-P_
    if linha[9] == "7":
        print("# Registro de ponto ")#, linha[9], linha)
        print("NSR: ", linha[0:9])
        print("CPF do empregado: ", linha[35:46])
        disp = ""
        if linha[70:72] == "01":
            disp = "App mobile"
            batidaApp += 1
        elif linha[70:72] == "02":
            disp = "Navegador web"
            batidaWeb += 1
        elif linha[70:72] == "03":
            disp = "App desktop"
        elif linha[70:72] == "04":
            disp = "Dispositivo eletronico"
        else:
            disp = "Outro dispositivo"
        if linha[30:32] == "03":
            fusoSP += 1
        elif linha[30:32] == "04":
            fusoMT += 1
        print("Dispositivo:",disp)
        print("data de registro: ", linha[10:34])
        regPonto += 1






    # busca por termo
    if busca[0] in linha:
        contLinhaBusca = contLinha
        vetorBusca.append(contLinha)

        #print(c)
    contLinha += 1

print("\n\nRESUMO:")
print("Alteracoes de dados da empresa:", emprAlt)
print("Inclusoes de empregados:", funcInc)
print("Alteracoes de empregados:", funcAlt)
print("Exclusoes de empregados:", funcExc)
print("Registros de ponto: ",regPonto)
print("Registros via App: ",batidaApp)
print("Registros via Batida Online: ",batidaWeb)
print("FUSO SP:", fusoSP)
print("FUSO MT:", fusoMT)
if len(vetorBusca) > 0:
    print("Palavra ",busca," encontrada na(s) linha(s) abaixo:")
    for ln in vetorBusca:
        print("Linha", ln)
