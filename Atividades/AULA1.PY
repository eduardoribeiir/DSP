def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade (baixa, média, alta): ").lower()
    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{descricao} | {prioridade}\n")
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("Tarefas:")
                for i, tarefa in enumerate(tarefas):
                    descricao, prioridade = tarefa.strip().split(" | ")
                    print(f"{i + 1}. {descricao} - Prioridade: {prioridade}")
    except FileNotFoundError:
        print("O arquivo tarefas.txt ainda não existe.")

def buscar_tarefas():
    palavra_chave = input("Digite a palavra-chave para buscar: ")
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()
            for i, tarefa in enumerate(tarefas):
                descricao, prioridade = tarefa.strip().split(" | ")
                if palavra_chave.lower() in descricao.lower():
                    print(f"{i + 1}. {descricao} - Prioridade: {prioridade}")
    except FileNotFoundError:
        print("O arquivo tarefas.txt ainda não existe.")

def remover_tarefa():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        visualizar_tarefas()
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if 0 <= numero_tarefa < len(tarefas):
            del tarefas[numero_tarefa]
            with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(tarefas)
            print("Tarefa removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except FileNotFoundError:
        print("O arquivo tarefas.txt ainda não existe.")
    except ValueError:
        print("Número de tarefa inválido.")

while True:
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Buscar tarefas")
    print("4. Remover tarefa")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        visualizar_tarefas()
    elif opcao == "3":
        buscar_tarefas()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")