print ("Bem vindo a calculadora Python\n"+"="*40)
while True:
    try:
        a = int (input("Digite um valor:"))
        b = int (input("Digite o segundo valor:"))
        o = int (input("Aperte:\n1 SOMAR\n2 SUBTRAIR\n3 MULTIPLICAR\n4 DIVIDIR\n5 SAIR\n"+"-"*50 +'\n'))
        if o == 1:
            t = (a+b)
            print (f"Total da Soma é {t}")
        elif o == 2:
            t = (a-b)
            print(f"Total da Subtração é {t}")
        elif o == 3:
            t = (a*b)
            print(f"valor da multiplicação é {t}")
        elif o == 4:
            
            t = (a/b)
            print(f"Total da divisao é {t}")
        elif o == 5:
            print("Obrigado, Volte sempre! ")
            break
        else:
            print("operação invalida! tente novamente.")
    except ValueError:
            print("Operação invalida!, por favor insira apenas numeros validos")