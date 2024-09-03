# 1

def somar_dois_numeros(num1, num2):
    return num1 + num2

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = somar_dois_numeros(numero1, numero2)

print(f"A soma de {numero1} e {numero2} é {resultado}.")

# 2

def somar_digitos(numero):
    if numero < 0 or numero >= 100:
        raise ValueError("O número deve ser menor que 100 e não pode ser negativo.")
    
    soma = (numero // 10) + (numero % 10)
    return soma

numero = int(input("Digite um número menor que 100: "))

try:
    
    resultado = somar_digitos(numero)
    
    print(f"A soma dos dígitos do número {numero} é {resultado}.")
    
except ValueError as e:

    print(e)
