from db_connection import get_db_connection

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        CREATE TABLE match_history (
            player1 TEXT,
            player2 TEXT,
            result INTEGER
        );
    )

    connection.commit()


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        DROP TABLE IF EXISTS match_history;
    )
    connection.commit()


def initialize():
    """Initializes the database by creating empty tables.
    Can be used to reset the database also.
    """
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize()