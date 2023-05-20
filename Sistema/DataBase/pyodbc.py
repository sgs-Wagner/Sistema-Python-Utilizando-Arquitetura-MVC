import pypyodbc

class DatabaseConnection:
    def __init__(self):
        self.connection_string = "Driver={SQL Server};Server=DESKTOP-LJNPA74\MSSQLSERVER02;Database=GerenciadorTarefasDB;Trusted_Connection=yes;"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pypyodbc.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            print("Connected to the database.")
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Disconnected from the database.")


if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.connect()
    db_connection.disconnect()