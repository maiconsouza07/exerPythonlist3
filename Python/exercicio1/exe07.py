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