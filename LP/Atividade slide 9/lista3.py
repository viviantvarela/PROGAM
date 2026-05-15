# Questão 1 - Números de 1 a 100 (Crescente)

for i in range(1, 101):
    print(i)

# Questão 2 - Números de 1 a 100 (Decrescente)

for i in range(100, 0, -1):
    print(i)

# Questão 3 - Determinação de intervalo

inicio = int(input('Digite o início do intervalo:'))
fim = int(input('Digite o fim do intervalo:'))
if inicio > fim:
    inicio, fim = fim, inicio
soma_intervalo = 0
for i in range(inicio, fim + 1):
    print(i)
    soma_intervalo += i 

print('A soma do intervalo é:', soma_intervalo)

# Questão 4 - Somátorio de Números

soma_10 = 0
for _ in range(10):
	numero = float(input("Digite um número: "))
	soma_10 += numero

print("Somatório dos 10 números:", soma_10)

# Questão 5 - Somátorio de Números Menores que 10

soma_menores_10 = 0
for _ in range(5):
    valor = float(input("Digite 5 valores: "))
    if valor < 10:
        soma_menores_10 += valor
        
print("A soma dos valores é", soma_menores_10)
     
# Questão 6 - Somátorio de Números >= 10 e < 20

soma_10_20 = 0
for _ in range(5):
    valor = float(input("Digite 5 valores:"))
    if 10 <= valor < 20:
        soma_10_20 += valor

print('A soma dos valores é:', soma_10_20)

# Questão 7- Somátorio de Números Pares

soma_pares = 0
for _ in range(5):
    valor = int(input('Digite 5 valores pares:'))
    if valor % 2 == 0:
        soma_pares += valor

print('A soma das partes é:', soma_pares)
        
# Questão 8 - Somátorio de Números Pares
soma_pares = 0
soma_impares = 0
for _ in range(10):
    numeros: int(input('Digite 10 números:'))
    if numeros % 2 == 0:







 
    

