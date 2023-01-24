# Main loop
from functions import *

def contRegistros():
    print(toCpf("1234567819"))
    print(toCnpj("134553234567819"))

#arquivo = input("Digite o nome do arquivo: ")

file = open('afd3.txt', 'r')
vetor = file.readlines()

while True:
    opcao = input("\nDigite a opcao: ")
    if opcao == "1":
        contRegistros(vetor)
    elif opcao == "2":
        dadosEmpresa(vetor)
    elif opcao == "3":
        buscaSujeira(vetor)
    elif opcao == "4":
        dadosArquivo(vetor)


        
    elif opcao == "0":
        print("\n=====\nFim do programa.")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")


