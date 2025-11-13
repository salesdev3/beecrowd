numero = int(input())

for i in range(numero):
    valor1, valor2, valor3 = map(float, input().split())
    media = (valor1 + valor2 + valor3) / 3
    print(f'{media:.1f}')
