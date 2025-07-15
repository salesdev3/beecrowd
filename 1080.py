maior = None
posicao = 0
for i in range(1,101):
    valor = int(input(''))
    if maior is None or valor > maior:
        maior = valor
        posicao = i
print(maior)
print(posicao)
