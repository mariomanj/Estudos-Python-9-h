# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcular a media artimetica
media = (n1 + n2) / 2.0

if media >= 7:
    print('Sua media foi maior ou igual a 7')
elif media >= 5:
    print('Voce esta de recuperação!!')
else:
    print('Você esta reprovado!!')

print('Sua media foi {}'.format(media))
