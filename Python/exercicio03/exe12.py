tarefas = []

while True:
    print("\n1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Visualizar Lista de Tarefas")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    
    elif opcao == '2':
        tarefa = input("Digite a tarefa que deseja remover: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada na lista.")
    
    elif opcao == '3':
        tarefas.sort()  
        print("Lista de Tarefas:")
        for t in tarefas:
            print(t)
    
    elif opcao == '4':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida, por favor tente novamente.")
