'''Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais.'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
 
if n1 > n2:
    print("O maior número é: ", n1)
if n1 < n2:
    print("O menor número é: ", n1)
elif n1 == n2:
    print("Os números são iguais")