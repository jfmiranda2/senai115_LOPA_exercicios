# 14. Faça um programa que leia uma palavra qualquer e a 
# imprima 10 vezes;


palavra  = input('Digite uma palavra para ela ser impressa 10 vezes: ')

for index in range(1,11):
    print(f'{index} - {palavra}')