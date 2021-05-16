import os
import sqlite3

from config import DB_PATH
dirname = os.path.dirname(__file__)
connection = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite3.Row


def get_db_connection():
    """Returns:
        Connection for the database.
    """

    return connection
