aluno = str(input('Por favor, informe o nome do aluno '))
n1 = float(input('Por favor, informe a primeira nota: '))
n2 = float(input('Po favor, informe a segunda nota: '))
media = (n1 + n2) / 2
if media > 7.0:
    print('O aluno \33[1;35m{}\33[m está APROVADO! média final: {:.1f} '.format(aluno, media))
elif media >= 5.0 and media <= 6.9:
    print('O aluno \33[1;35m{}\33[m está de RECUPERAÇÃO média final: {:.1f}'.format(aluno, media))
else:
    print('O aluno \33[1;35m{}\33[m infelizmente está REPROVADO média final: {:.1f}'.format(aluno, media))