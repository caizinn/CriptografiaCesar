alfabeto = 'abcdefghijklmnopqrstuvwxyz'
rot = 3

def encriptar(mensagem):
    m = ''

    for letra in mensagem:
        if letra in alfabeto:
            letra_index = alfabeto.index(letra)
            m += alfabeto[(letra_index + rot) % len(alfabeto)]
        else:
            m += letra
    return m

def encriptarArquivo(caminho):
    m = ''
    arquivo = open(caminho, "r")
    linha = arquivo.read()
    for letra in linha:
        if letra in alfabeto:
            letra_index = alfabeto.index(letra)
            m += alfabeto[(letra_index + rot) % len(alfabeto)]
        else:
            m += letra
    
    arquivo.close()
    return m
    
def decriptar(mensagem):
    m = ''

    for letra in mensagem:
        if letra in alfabeto:
            letra_index = alfabeto.index(letra)
            m += alfabeto[(letra_index - rot) % len(alfabeto)]
        else:
            m += letra
    return m

def decriptarArquivo(caminho):
    m = ''
    arquivo = open(caminho, "r")
    linha = arquivo.read()
    for letra in linha:
        if letra in alfabeto:
            letra_index = alfabeto.index(letra)
            m += alfabeto[(letra_index - rot) % len(alfabeto)]
        else:
            m += letra
    
    arquivo.close()
    return m


sair = -1; 
while sair != 0:
    print("Cifra de Cesar")
    print("============MENU===========")
    print("1 - Encriptar")
    print("2 - Descriptar")
    print("3 - Sair")
    print("===========================")
   
    comando = int(input("Digite o comando que deseja utilizar: "))

    if comando == 1:
        print("\n==========ESCOLHA UMA OPÇÃO=================")
        print("1 - Criptografar direto no sistema: ")
        print("2 - criptografar utilizando um arquivo existente: ")
        print("3 - criptografar criando um arquivo: ")
        print("============================================")
        op = int(input("Digite a opção para criptografar: "))

        if op == 1: 
            mensagem = input("Digite a mensagem que deseja encriptar: ")
            mensagem_encriptada = encriptar(mensagem)
            mensagem_encriptada = mensagem_encriptada.lower()        
            print("A mensagem encriptada: ", mensagem_encriptada)
        elif op == 2:
            caminho = str(input("Digite o caminho do seu arquivo: "))        
           
            mensagem_encriptada = encriptarArquivo(caminho)
            mensagem_encriptada = mensagem_encriptada.lower()   
            arquivo = open(caminho, "w")
            arquivo.write(mensagem_encriptada)
            arquivo.close()
            print("Mensagem criptografada com sucesso!")
            
        elif op == 3:
            nome = input("Digite o nome do arquivo  que você quer criar: ")
            arquivo = open(nome, "w")
            mensagem = input("Digite a mensagem: ")
            mensagem_encriptada = encriptar(mensagem)
            mensagem_encriptada = mensagem_encriptada.lower() 
            arquivo.write(mensagem_encriptada)
            arquivo.close()
            print("Mensagem criptografada com sucesso!")

        else:
            print(op," <- opção inválida! ")
        
    elif comando == 2:
        print("\n==========ESCOLHA UMA OPÇÃO=================")
        print("1 - Descriptografar mensagem no sistema")
        print("2 - Descriptografar mensagem utilizando arquivo existente")  
        print("============================================")

        op = int(input("Digite a opção para criptografar: "))

        if op == 1:
            mensagem = input("Digite a mensagem que deseja decriptar: ")
            mensagem_decriptada = decriptar(mensagem)
            mensagem_decriptada = mensagem_decriptada.lower()
            print("A mensagem decriptada: ", mensagem_decriptada)

        elif op == 2:
            caminho = str(input("Digite o caminho do seu arquivo: "))
            mensagem_decriptada = decriptarArquivo(caminho)
            mensagem_decriptada = mensagem_decriptada.lower()
            arquivo = open(caminho, "w")
            arquivo.write(mensagem_decriptada)   
            arquivo.close()
            print("Mensagem foi descriptografada com sucesso!")
        else:
            print(op, " <- opção inválida! ")

    elif comando == 3:
        print("Volte sempre!!!")
        sair = 0; 

    else:
        print(comando, ' -> Não é um comando válido')