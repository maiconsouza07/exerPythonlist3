numeros_str = input("Insira uma lista de números separados por espaços: ")

numeros = list(map(int, numeros_str.split()))

menor_valor = min(numeros)
maior_valor = max(numeros)
soma = sum(numeros)

print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
print("Soma dos números:", soma)

numeros_ordenados = sorted(numeros, reverse=True)
print("Lista em ordem decrescente:", numeros_ordenados)
