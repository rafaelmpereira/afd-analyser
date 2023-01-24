def toCpf(cpf):
    return('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]))

def toCnpj(cnpj):
    return('{}.{}.{}/{}-{}'.format(cnpj[:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:]))

def dadosEmpresa(vetor):
    emprAlt = 0
    responsaveis = []
    cnpjs = []
    empresas = []
    for linha in vetor:
        if linha[9] == "2":
            if responsaveis.count(linha[37:48]) == 0:
                responsaveis.append(linha[37:48])
            if cnpjs.count(linha[49:63]) == 0:
                cnpjs.append(linha[49:63])
            if empresas.count(linha[77:227]) == 0:
                empresas.append(linha[77:227])
            emprAlt += 1
    print("\nUltimo NSR:", vetor[-3][0:9])    
    print("Responsaveis ja cadastrados:")
    for resp in responsaveis:
        print(toCpf(resp))
    print("CNPJs ja cadastrados:")
    for cnpj in cnpjs:
        print(toCnpj(cnpj))
    print("Empresas ja cadastradas:")
    for empr in empresas:
        print(empr)
    print("Alterações de dados da Empresa:", emprAlt)    

def dadosArquivo(vetor):
    regPonto = 0
    funcInc = 0
    funcAlt = 0
    funcExc = 0
    batidaApp = 0
    batidaWeb = 0
    batidaDesk = 0
    batidaEletr = 0
    batidaOutro = 0
    fusoSP = 0
    fusoMT = 0
    
    print("\nUltimo NSR:", vetor[-3][0:9])
    for linha in vetor:
        if linha[9] == "7":
            disp = ""
            if linha[70:72] == "01":
                disp = "App mobile"
                batidaApp += 1
            elif linha[70:72] == "02":
                disp = "Navegador web"
                batidaWeb += 1
            elif linha[70:72] == "03":
                disp = "App desktop"
                batidaDesk += 1
            elif linha[70:72] == "04":
                disp = "Dispositivo eletronico"
                batidaEletr += 1
            else:
                disp = "Outro dispositivo"
                batidaOutro += 1
            if linha[30:32] == "03":
                fusoSP += 1
            elif linha[30:32] == "04":
                fusoMT += 1
            regPonto += 1

        if linha[9] == "5":
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

    print("Inclusoes de empregados:", funcInc)
    print("Alteracoes de empregados:", funcAlt)
    print("Exclusoes de empregados:", funcExc)
    print("Registros de ponto: ",regPonto)
    print("Registros via App: ",batidaApp)
    print("Registros via Batida Online: ",batidaWeb)
    print("Registros via Aplicacao Desktop: ",batidaDesk)
    print("Registros via Dispositivo Eletronico: ",batidaEletr)
    print("Registros via Outro Dispositivo: ",batidaOutro)
    print("FUSO SP:", fusoSP)
    print("FUSO MT:", fusoMT)





    
def buscaSujeira():
    print("sujeira")
    
    """
         'q','w','e','r','t','y','u','i','o','p','a','s',
              'd','f','g','h','j','k','l','z','x','c','v','b',
              'n','m','1','2','3','4','5','6','7','8','9','0',
              '.',',',';',' ',':','-','+','=','?','/','Q','W',
              'E','R','T','Y','U','I','O','P','A','S','D',
              'F','G','H','J','K','L','Z','X','C','V','B',
              'N','M']
    """



