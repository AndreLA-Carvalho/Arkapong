import sqlite3
from datetime import datetime

class DBProxy:
    def __init__(self, db_name="asset/ranking.db"):
        self.db_name = db_name
        self.create_table()

    def _conect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        connection = self._conect()
        cursor = connection.cursor()
        
        # Tabela de ranking com nickname, pontos e data/hora
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nickname TEXT NOT NULL,
                pontos INTEGER NOT NULL,
                data_hora TEXT NOT NULL
            )
        """)
        
        connection.commit()
        connection.close()

    def save_score(self, nickname: str, pontos: int):
        connection = self._conect()
        cursor = connection.cursor()
        
        # Pega a data e hora exata do momento do salvamento
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        cursor.execute("""
            INSERT INTO ranking (nickname, pontos, data_hora)
            VALUES (?, ?, ?)
        """, (nickname.upper(), pontos, data_atual))
        
        connection.commit()
        connection.close()

    def get_top10(self):
        connection = self._conect()
        cursor = connection.cursor()
        
        # Seleciona nick, pontos e data ordenando pelos maiores pontos e limitando a 10 resultados
        cursor.execute("""
            SELECT nickname, pontos, data_hora 
            FROM ranking 
            ORDER BY pontos DESC 
            LIMIT 10
        """)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados