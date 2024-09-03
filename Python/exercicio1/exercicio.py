
#1
nome = "Rafael"
print("Bom dia " + nome)

#2
x = "gdsdAS dDdfdsDGs"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())


#3

x = "Rafael Mesquita"
sem_espacos = ''.join(x.split())
print(sem_espacos)

#4

def adicionar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("Não é possível dividir por zero.")
    return num1 / num2

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

try:

    soma = adicionar(valor1, valor2)
    subtracao = subtrair(valor1, valor2)
    multiplicacao = multiplicar(valor1, valor2)
    divisao = dividir(valor1, valor2)

    print(f"A soma de {valor1} e {valor2} é {soma}.")
    print(f"A subtração de {valor1} e {valor2} é {subtracao}.")
    print(f"A multiplicação de {valor1} e {valor2} é {multiplicacao}.")
    print(f"A divisão de {valor1} por {valor2} é {divisao:.2f}.")  # Limita a dois dígitos decimais
except ValueError as e:
    
    print(e)
    
#5

numeros = list(range(1000))

soma = sum(numeros)

quantidade = len(numeros)

media = soma / quantidade

print(f"A média dos valores de 0 a 999 é {media:.2f}.")

#6

frase = input("Digite uma frase: ")

palavras = frase.split()

numero_de_palavras = len(palavras)

palavras_invertidas = palavras[::-1]

frase_invertida = ' '.join(palavras_invertidas)

print(f"A frase possui {numero_de_palavras} palavras.")
print(f"A frase com as palavras invertidas é: \"{frase_invertida}\"")

#7

def main():
    while True:
        
        numero = float(input("Digite um número (ou 0 para sair): "))
        
        if numero == 0:
            print("Você digitou zero. Programa encerrado.")
            break
        
        elif numero > 0:
            print(f"O número {numero} é positivo.")
        else:
            print(f"O número {numero} é negativo.")

if __name__ == "__main__":
    main()
 
 #8
 
 def main():
    
    alunos_lista = []
    alunos_set = set()
    
    while True:
        
        print("\nGerenciamento de Alunos")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Verificar existência de aluno")
        print("4. Listar alunos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            nome = input("Digite o nome do aluno para adicionar: ").strip()
            if nome not in alunos_set:
                alunos_lista.append(nome)
                alunos_set.add(nome)
                print(f"Aluno {nome} adicionado com sucesso.")
            else:
                print(f"Aluno {nome} já está na lista.")
                
        elif opcao == '2':
            nome = input("Digite o nome do aluno para remover: ").strip()
            if nome in alunos_set:
                alunos_lista.remove(nome)
                alunos_set.remove(nome)
                print(f"Aluno {nome} removido com sucesso.")
            else:
                print(f"Aluno {nome} não encontrado na lista.")
                
        elif opcao == '3':
            nome = input("Digite o nome do aluno para verificar: ").strip()
            if nome in alunos_set:
                print(f"Aluno {nome} está na lista.")
            else:
                print(f"Aluno {nome} não está na lista.")
                
        elif opcao == '4':
            if alunos_lista:
                print("Lista de alunos:")
                for aluno in alunos_lista:
                    print(f"- {aluno}")
            else:
                print("A lista de alunos está vazia.")
                
        elif opcao == '5':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__": main()

 