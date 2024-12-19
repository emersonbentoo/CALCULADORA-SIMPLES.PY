print ("Bem vindo a calculadora Python\n"+"="*40)
while True:
    try:
        a = float(input("Digite um valor:"))
        b = float (input("Digite o segundo valor:"))
        while True:
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
                if b != 0:
                    t = (a/b)
                print(f"Total da divisao é {t}")
                print("Erro: Divisao por zero nao é permitido!")
            elif o == 5:
                print("Obrigado, Volte sempre! ")
                exit()
            else:
                print("operação invalida!.\nRepita a operação desejada")
    except ValueError:
        print("Operação invalida!, por favor insira apenas numeros validos")