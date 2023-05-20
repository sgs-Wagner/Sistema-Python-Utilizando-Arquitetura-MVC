from Models.model import Tarefa, GerenciadorTarefas


class TarefaController:
    def __init__(self):
        self.gerenciador_tarefas = GerenciadorTarefas()

    def adicionar_tarefa(self, titulo, descricao, concluida):
        tarefa = Tarefa(titulo, descricao, concluida)
        self.gerenciador_tarefas.criar_tarefa(tarefa)
        return "tarefa adicionada com sucesso"

    def buscar_tarefa(self, id_tarefa):
        tarefa = self.gerenciador_tarefas.buscar_tarefa(id_tarefa)
        return tarefa

    def atualizar_tarefa(self, id, titulo, descricao, concluida):
        tarefa = Tarefa(titulo, descricao, concluida)

        sucesso = self.gerenciador_tarefas.atualizar_tarefa(id, tarefa)

        if sucesso:
            print("Tarefa atualizada com sucesso!")
        else:
            print("Erro ao atualizar tarefa.")



    def excluir_tareda(self, id_tarefa):
        return self.gerenciador_tarefas.excluir_tarefa(id_tarefa)




