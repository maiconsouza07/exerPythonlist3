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

if __name__ == "__main__":
    main()