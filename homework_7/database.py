import sqlite3

def create_table(conn):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS books(
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    ''')

def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute('''
    INSERT INTO books
    values(?, ?, ?, ?, ?, ?)
    ''', (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_table(conn)
    insert_books(conn,"mdada", "mafda", 1393, 'mdada', 200, 39)
    insert_books(conn,"madda", "maada", 1993, 'mada', 200, 39)
    conn.commit()
    conn.close()