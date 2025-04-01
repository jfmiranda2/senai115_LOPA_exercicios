# 19. Faça um programa que receba duas notas de seis alunos. 
# Calcule e mostre:
# - A média aritmética das duas notas de cada aluno; e
# - A mensagem que está na tabela a seguir:
#       Média Aritmética | Mensagem
#       Até 3            | Reprovado
#       Entre 3 e 7      | Exame
#       De 7 para cima   | Aprovado
# - O total de alunos aprovados;
# - O total de alunos de exame;
# - O total de alunos reprovados;
# - A média da classe.
#

#=====================================================================

qtd_Alunos = 3 #escopo global
conta_Aluno = 0
qtd_aluno_reprovado = 0
qtd_aluno_aprovado = 0
qtd_aluno_exame = 0
soma_medias = 0

def status_aluno(n1, n2):
    mensagem = 'oi' #escopo local
    global  qtd_aluno_reprovado, qtd_aluno_exame, qtd_aluno_aprovado
    media_aluno = (nota_um + nota_dois)/2
    if media_aluno < 3:
        qtd_aluno_reprovado += 1
        return 'reprovado', media_aluno
    elif media_aluno >= 3 and media_aluno < 7:
        qtd_aluno_exame += 1
        return 'exame', media_aluno
    else:
        qtd_aluno_aprovado += 1
        return 'aprovado', media_aluno

while conta_Aluno < qtd_Alunos:
    nota_um = int(input('Insira a primeira nota: '))
    nota_dois = int(input('Insira a segunda nota: '))
    
    status, media_aluno = status_aluno(nota_um, nota_dois)
    soma_medias = soma_medias + media_aluno
    print(soma_medias)
    print(f'O aluno esta {status}')
    conta_Aluno = conta_Aluno + 1

print('Alunos aprovados:', qtd_aluno_aprovado)
print('Alunos reprovados', qtd_aluno_reprovado)
print('Aluno exame', qtd_aluno_exame)
print('Media geral', soma_medias/qtd_Alunos)