from db_connection import get_db_connection

class MatchHistoryRepository:
    def __init__(self):
        self._connection = get_db_connection()
    
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM match_history')
        all_scores = cursor.fetchall()
        return all_scores

    def add_score(self, player1, player2, result):
        cursor = self._connection.cursor()
        command = 'INSERT INTO match_history (player1, player2, result) VALUES (?, ?, ?)'
        cursor.execute(command, [player1, player2, result])
        self._connection.commit()