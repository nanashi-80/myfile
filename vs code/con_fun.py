import connet as c

def table_2():
    script= f"select*from con_2"
    connection = c.connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(script)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def table_1():
    script= f"select*from conatractor_1"
    connection = c.connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(script)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

