dados = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    print('-=' * 40)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
for i, d in enumerate(dados):
    print(f'>>>> Na posição {i}, temos o aluno {d[0]}, que teve sua média {d[2]}.')
while True:
    notas = int(input('Quer ver as notas de qual aluno? [Digite 999 para finalizar o programa]: '))
    if notas == 999:
        print('FINALIZANDO...')
        break
    if notas <= len(dados) - 1:
        print(f'Notas de {dados[notas][0]} são {dados[notas][2]}')
print('Volte Sempre!')
