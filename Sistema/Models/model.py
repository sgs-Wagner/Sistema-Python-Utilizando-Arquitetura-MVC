import pypyodbc

class Tarefa: #dto
    def __init__(self, titulo, descricao, concluida):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida



class GerenciadorTarefas:#DAO
    def __init__(self):
        self.connection_string = "Driver={SQL Server};Server=DESKTOP-LJNPA74\MSSQLSERVER02;Database=GerenciadorTarefasDB;Trusted_Connection=yes;"

    def conectar(self):
        return pypyodbc.connect(self.connection_string)

    def criar_tarefa(self, tarefa):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            sql = "INSERT INTO Tarefa (Titulo, Descricao, Concluida) VALUES (?, ?, ?)"
            values = (tarefa.titulo, tarefa.descricao, tarefa.concluida)
            cursor.execute(sql, values)
            connection.commit()

            cursor.close()
            connection.close()
            return True

        except pypyodbc.Error as e:
            print("Erro ao criar tarefa:", e)
            return False

    def buscar_tarefa(self, id_tarefa):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            sql = "SELECT * FROM Tarefa WHERE Id = ?"
            cursor.execute(sql, (id_tarefa,))
            row = cursor.fetchone()
            #print(row)
            if row:
                return row

            cursor.close()
            connection.close()

        except pypyodbc.Error as e:
            print("Erro ao buscar tarefa:", e)

        return None

    def atualizar_tarefa(self, id_tarefa, tarefa): # stand by - ta errado
        #print(id_tarefa, tarefa.titulo, tarefa.descricao, tarefa.concluida)
        try:
            connection = self.conectar()
            cursor = connection.cursor()
            print('entrei no try')
            sql = "UPDATE Tarefa SET Titulo = ?, Descricao = ?, Concluida = ? WHERE Id = ?"
            values = (tarefa.titulo, tarefa.descricao, tarefa.concluida, id_tarefa)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True

        except pypyodbc.Error as e:
            print("Erro ao atualizar tarefa:", e)
            return False

    def excluir_tarefa(self, id_tarefa):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            sql = "DELETE FROM Tarefa WHERE Id = ?"
            cursor.execute(sql, (id_tarefa,))
            connection.commit()

            cursor.close()
            connection.close()
            return True

        except pypyodbc.Error as e:
            print("Erro ao excluir tarefa:", e)
            return False

