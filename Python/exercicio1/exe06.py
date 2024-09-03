frase = input("Digite uma frase: ")

palavras = frase.split()

numero_de_palavras = len(palavras)

palavras_invertidas = palavras[::-1]

frase_invertida = ' '.join(palavras_invertidas)

print(f"A frase possui {numero_de_palavras} palavras.")
print(f"A frase com as palavras invertidas é: \"{frase_invertida}\"")