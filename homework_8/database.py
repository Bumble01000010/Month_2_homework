import sqlite3

def create_table(conn):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    values(?, ?, ?, ?, ?, ?)
    ''', (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )

def get_books_by_author(conn, author):
    result = conn.execute('''
        SELECT * FROM books WHERE author = ?
        ''', (author,)).fetchall()

    if result:
        print(f'Книги за авторством {author}:')
        for book in result:
            print(f'{book[1]}')
    else:
        print(f'Книг за авторством {author} нет')

    return result

def delete_book_by_id(conn, id):
    result = conn.execute('''
        DELETE FROM books WHERE id = ?
        ''', (id,))

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_table(conn)
    insert_books(conn,"To Kill a Mockingbird", "Harper Lee", 1960, "Classic Fiction", 281, 5)
    insert_books(conn,"1984", "George Orwell", 1949, "Dystopian", 328, 4)
    insert_books(conn,"The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic Literature", 180, 3)
    insert_books(conn,"The Hobbit", "J.R.R. Tolkien", 1937, "High Fantasy", 310, 8)
    insert_books(conn,"Pride and Prejudice", "Jane Austen", 1813, "Romantic Fiction", 279, 6)
    insert_books(conn,"Frankenstein", "Mary Shelley", 1818, "Gothic Horror", 280, 2)
    insert_books(conn,"The Catcher in the Rye", "J.D. Salinger", 1951, "Coming-of-age", 234, 4)
    insert_books(conn,"Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological Fiction", 545, 3)
    insert_books(conn,"Dune", "Frank Herbert", 1965, "Science Fiction", 617, 7)
    insert_books(conn,"The Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy", 309, 10)
    get_books_by_author(conn, "Mary Shelley")
    get_books_by_author(conn, "Tarrantino")
    delete_book_by_id(conn, 2)
    conn.commit()
    conn.close()