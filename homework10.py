import sqlite3
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    price REAL
)
""")

books = [
    ("Harry Potter", "J.K. Rowling", 1997, 20.5),
    ("The Hobbit", "J.R.R. Tplkien", 1965, 25.99),
    ("Dune", "Frank Herbert", 1965, 25.99),
    ("Rosapalatselsa", "Bor Hes", 1960, 10.90)
 ]

cursor.executemany("""
INSERT INTO books (title, author, year, price)
VALUES (?, ?, ?, ?)
""", books)

cursor.execute("""
UPDATE books 
SET price = 30.0
WHERE title = 'Dune'
""")

cursor.execute("""
DELETE FROM books 
WHERE title = 'The Hobbit'
""")

connection.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()