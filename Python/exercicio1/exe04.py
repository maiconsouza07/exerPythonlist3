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