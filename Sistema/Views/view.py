from Controllers.controller import TarefaController

class TarefaView:
    def __init__(self):
        self.controller = TarefaController()

    def menu_principal(self):
        while True:
            print("===== MENU PRINCIPAL =====")
            print("1. Adicionar Tarefa")
            print("2. Atualizar Tarefas")
            print("3 - Buscar Tarefa")
            print("4 - Excluir Tarefa")
            print("0. Sair")
            print("==========================")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                titulo = input("Digite o título da tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")
                concluida = input("Digite o status: ")
                print(self.controller.adicionar_tarefa(titulo, descricao, concluida))
            elif opcao == "2":
                tarefa_id = input("Digite o id da tarefa: ")
                tarefa_titulo = input("Digite o Titulo da tarefa: ")
                tarefa_descricao = input("Digite a descrição da tarefa: ")

                tarefa_concluida = input("Digite o status da tarefa 1 = Concluida / 2 = Nao conluida: ")
                if tarefa_concluida == 1:
                    tarefa_concluida = True
                elif tarefa_concluida == 0:
                    tarefa_concluida = False

                self.controller.atualizar_tarefa(tarefa_id, tarefa_titulo, tarefa_descricao, tarefa_concluida)

            elif opcao == "3":
                id_tarefa = input("Digite o id da tarefa: ")
                print(self.controller.buscar_tarefa(id_tarefa))

            elif opcao == "4":
                id_tarefa = input("Digite o id da tarefa a ser excluida: ")
                print(self.controller.excluir_tareda(id_tarefa))

            elif opcao == "0":
                break
            else:
                print("Opção inválida. Digite novamente.")

            print()  # linha em branco para melhorar a legibilidade

