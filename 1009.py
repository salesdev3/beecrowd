nome = str(input())
salario = float(input())
vendas = float(input())

comissao = 15/100 * vendas

print(f"TOTAL = R$ {(salario + comissao):.2f}")
