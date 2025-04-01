# 18. Faça um programa que receba 10 números e apresente a soma 
# dos números pares e dos números ímpares;

lista_numeros = [0,1,2,3,4,5,6,7,8,9]
lista_numeros_dois = []

#Loop para recber os valores
for index in range(10):
    print(index)
    numero = int(input('Inisra um número: '))
    lista_numeros[index] = numero
    lista_numeros_dois.append(numero)

soma_par = 0
soma_impar = 0

#Loop para apresentar os valores
for item in lista_numeros_dois:
    resto = item%2
    if(resto == 0):
        soma_par = soma_par + item
    else:
        soma_impar = soma_impar + item

print(f'Soma dos numeros pares: {soma_par}')
print(f'Soma dos numeros impares {soma_impar}')
