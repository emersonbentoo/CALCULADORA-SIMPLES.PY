print (" Bem vindo a calculadora Python")

print ('Digite um numero da operação: ')
a = int (input())
print ('Digite o segundo numero da operação:')
b = int (input())
print("Aperte\n1 SOMAR\n2 SUBTRAIR\n3 MULTIPLICAR\n4 DIVIDIR\n = = = = =")
o = int(input())
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
    print(f"Total da divisao é{t}")
