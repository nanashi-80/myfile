import mysql.connector as c

def connect():
    con = c.connect(
    host='localhost',
    database='clims',
    user = 'root',
    password='Haris@123')
    return con