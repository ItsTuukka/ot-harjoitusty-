from db_connection import get_db_connection


class MatchHistoryRepository:

    """Class for the match history database.

    Attributes:
        connection: Connection to the sql database.
    """

    def __init__(self):
        """Constructor for the class.
        """

        self._connection = get_db_connection()

    def find_all(self):
        """Finds all the matches from the database.
        """

        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM match_history')
        all_scores = cursor.fetchall()
        return all_scores

    def add_score(self, player1, player2, result):
        """Adds a match to the database

        Args: 
            player1: Username for player1.
            player2. Username for player2.
            result: Result of the game.
        """

        cursor = self._connection.cursor()
        command = 'INSERT INTO match_history (player1, player2, result) VALUES (?, ?, ?)'
        cursor.execute(command, [player1, player2, result])
        self._connection.commit()
