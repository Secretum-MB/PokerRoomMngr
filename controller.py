import database


database.db_cursor.execute('INSERT INTO Artist (name) VALUES (?)', ('Mathias', ))

print(database.db_cursor.fetchone())