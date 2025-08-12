precos = {
    1: 4.00,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.50
}

codigo, quantidade = map(int, input().split())

if codigo in precos:
    total = precos[codigo] * quantidade
    print(f"Total: R$ {total:.2f}")
 