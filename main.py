import sqlite3

database = 'movie.db'

connection = sqlite3.connect(database)
cursor = connection.cursor()


cursor.execute(
    '''
    SELECT * FROM movies
    WHERE title LIKE 'Harry Potter%';
'''
)
result = cursor.fetchall()
connection.close()

# Вывод результатов
for row in result:
    print(row)