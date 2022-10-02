import os

def menu():
    
    print("Bem-Vindo ao Gerenciador de Arquivos Txt!")
    print("Digite a opção desejada")
    print("1 - Criar um arquivo ")
    print("2 - Escrever no arquivo ")
    print("3 - Exluir um arquivo ")
    print("4 - Visualizar um arquivo ")
    print("5 - Sair do programa ")
    opcao = int(input())

    return opcao

def aceitarEntrada(nome):
    #verifica se o usuário digitou o nome sem a extensão
    nomeSplit = nome.split('.')
    while(len(nomeSplit) != 1):
        nome = input("Digite o nome do arquivo sem extensão: ")
        nomeSplit = nome.split('.')
    return nome

def criarArquivo():
    nome = input("Digite o nome do arquivo sem extensão: ")
    nome = aceitarEntrada(nome)

    arq = open(nome + '.txt', 'w+')

    if(os.path.exists(nome + '.txt')):
        print("Arquivo criado com sucesso!")
    arq.close()

def escolherArquivo(): #Lista todos os arquivos .txt do diretório
    #pega todos os arquivos do diretório que está este arquivo
    dir = os.listdir('.\\')
    print("Arquivos")
    #pegar somente os arquivos com extensão .txt
    for arqTxt in dir:
        if arqTxt.endswith('.txt'):
            print(arqTxt)

def escreverArquivo():  
    escolherArquivo()
    nome = input("Digite o nome do arquivo que você deseja escrever sem extensão: ")
    nome = aceitarEntrada(nome)
    
    if(not os.path.exists(nome + '.txt')):
        print("Arquivo não existe")
    else:
        
        arq = open(nome + '.txt', 'a+')
    
        if arq.mode == 'a+':
            conteudo = input("\nDigite o conteúdo que vai ser inserido no arquivo e enter para confirmar\n")
            arq.write(conteudo+'\r')
        arq.close()

def excluirArquivo():
    escolherArquivo()
    nome = input("Digite o nome do arquivo para excluir sem extensão: ")
    nome = aceitarEntrada(nome)

    if(not os.path.exists(nome + '.txt')):
        print("Erro ao excluir arquivo")
    else:
        os.remove(nome + '.txt')
        print("Arquivo excluído com sucesso")

def visualizarArquivo():
    escolherArquivo()
    nome = input("Digite o nome do arquivo para visualizar sem extensão: ")
    nome = aceitarEntrada(nome)


    if(not os.path.exists(nome+'.txt')):
        print("Arquivo não existe")
    else:
        arq = open(nome+'.txt', 'r')
        print("<Conteúdo do arquivo>")
        print(arq.read())
        arq.close()

def main():
    opcao = 0
    while(opcao != 5):
        print()
        opcao = menu()

        if opcao == 1:
            criarArquivo()
        
        elif opcao == 2:
            escreverArquivo()
        
        elif opcao == 3:
            excluirArquivo()
        
        elif opcao == 4:
            visualizarArquivo()

main()
