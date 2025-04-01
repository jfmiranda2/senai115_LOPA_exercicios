# 17. Faça um programa que receba dois valores, sendo que o primeiro 
# deve ser menor que o segundo. O programa deve apresentar todos os 
# números ímpares contidos nesta sequência. (Modulo %. Exemplo: 7%2 = 1)


#Preso em um for enquanto não houver um break
while True:
    nr_inicio = int(input('Digite o numero inicio: '))
    nr_fim  = int(input('Digite o numero fim: '))
    if nr_fim > nr_inicio:
        break
    else:
        print('Error: Numero inicial maior que o final')

# if nr_inicio > nr_fim:
#     buffer = nr_fim
#     nr_fim = nr_inicio
#     nr_inicio = buffer

# 3 / 5 / 7 / 9

for numero in range(nr_inicio, nr_fim+1):
    resto = numero%2 #recebe o resto da divisão por 2
    if(resto == 1):
        print(numero)#imprimir apenas numero ímpar