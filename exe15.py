# 15. Faça um programa que calcule a 
# tabuada de um número digitado pelo usuário;


numero = int(input('Digite um numero para fazer a sua tabuada: '))

for multiplicador in range(1,11):
    print(f'{numero} x {multiplicador} = {numero * multiplicador}')