import mysql.connector
conn = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='1234',
    # db='python15',
    db='sakila'
)

print(conn)

mycursor = conn.cursor()
# print(mycursor)
# mycursor.execute('create table student (name VARCHAR(255), age INTEGER(2));')

# user = ('Bob', 30)
# sql_formula = f'INSERT INTO student (name, age) VALUES ("{user[0]}", {user[1]})'
# mycursor.execute(sql_formula)
#
# user = ('Mary', 18)
# sql_formula = f'INSERT INTO student (name, age) VALUES ("{user[0]}", {user[1]})'
# mycursor.execute(sql_formula)

# sql_formula = f'INSERT INTO student (name, age) VALUES (%s, %s)'
# user = ('Sarah', 31)
# mycursor.execute(sql_formula, user)
#
# users = [('Johny', 32), ('Max', 50),('Samantha', 15)]
# mycursor.executemany(sql_formula, users)

# conn.commit()


mycursor.execute('select * from actor')
result = mycursor.fetchall()
print(result)