num_lista = []

for i in range(1, 11):
    numero = int(input("Digite um número: "))
    print(f"{numero} x {i} = {numero * i}")
    num_lista.append(numero)

print(";".join(str(num_lista)))

num_list = []
soma = 0

sequencia = int(input("Digite um número para a sequência: "))
for num in range(sequencia):
    numeros_digitados = int(input("Digite os números a serem somados: "))
    soma += numeros_digitados
    num_list.append(numeros_digitados)

print(" + ".join(str(n) for n in num_list) + f" = {soma}")
print(f"A soma dos números é: {soma}")