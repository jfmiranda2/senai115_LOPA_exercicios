# 16. Faça um programa que calcula a tabuada dos números 2 a 9;

for numero in range(2,10):
    print('==============================================================')
    for multiplicador in range(1,11):
        print(f'{numero} x {multiplicador} = {numero * multiplicador}')