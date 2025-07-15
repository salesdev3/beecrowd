N = int(input(''))
valor_original = N
cedulas = [100, 50, 20, 10, 5, 2, 1]
print(valor_original)
for cedula in cedulas:
    quantidade = N // cedula
    print(f'{quantidade} nota(s) de R$ {cedula},00')
    N %= cedula
