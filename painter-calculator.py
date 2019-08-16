medida = input(' tu fez a medida em CENTIMETROS ou em METROS? ')

if medida == 'centimetros':
     altura = float(input('insra a altura em centimetros: '))
     largura = float(input('insira a larura em centimetros: '))

     altura_metros = f'0,{altura}'
     largura_metros = f'0,{largura}'

     M2 = altura * largura
     print(f'o resultado é {M2} m2')


elif medida == 'metros':
    altura = float(input('insra a altura em metros: '))
    largura = float(input('insira a larura em metros: '))

    M2 = altura * largura

    print(f'o resultado é {M2} m2')


else:
    print('escreva em letras minusculas e sem ascentro por favore')

