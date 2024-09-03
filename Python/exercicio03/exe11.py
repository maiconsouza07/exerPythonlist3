notas = []
for i in range(5):
    nota = float(input(f"Insira a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Média das notas:", media)

notas_ordenadas = sorted(notas)
print("Notas em ordem crescente:", notas_ordenadas)
