import sqlite3

connection = sqlite3.connect("zarma.db")
cursor = connection.cursor()

stmt_create_users_table = "CREATE TABLE IF NOT EXISTS users( \
                            id INTEGER, \
                            name VARCHAR(50), \
                            age INTEGER, \
                            PRIMARY KEY (id) \
                            );"
cursor.execute(stmt_create_users_table)
connection.commit()

stmt_insert_users = 'INSERT INTO users (name, age) \
                     VALUES("Ivan", "10"), ("Boris", "55"), ("Georgiy", "30"), ("Pavel", "31");'
cursor.execute(stmt_insert_users)
connection.commit()

stmt_select_users_older_30 = ("SELECT name, age FROM users \
                               WHERE age > 30")
users = cursor.execute(stmt_select_users_older_30).fetchall()
print(users)

cursor.execute("DROP TABLE users;")
connection.commit()
