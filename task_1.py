from connect import con as c

def insert():
    name = input("Enter name   -")
    id =   int(input("Enter ID -"))
    salary = int(input("Enter salary -"))
    script= f"INSERT INTO employee_data(id,name,salary) VALUES ({id},'{name}',{salary})"
    cursor = c.cursor()
    cursor.execute(script)
    c.commit()
    cursor.close()
    c.close()
    print("DATA INSERTED SUCCESFULLY")

# insert()    

def update():
    name = input("Enter name   -")
    id =   int(input("Enter ID -"))
    salary = int(input("Enter salary -"))
    script= f"UPDATE employee_data SET id={id},name='{name}',salary={salary} WHERE id={id}"
    cursor = c.cursor()
    cursor.execute(script)
    c.commit()
    cursor.close()
    c.close()
    print("DATA UPDATED SUCCESFULLY")

def delete():
    id =   int(input("Enter ID -"))
    script= f"DELETE FROM employee_data WHERE id={id}"
    cursor = c.cursor()
    cursor.execute(script)
    c.commit()
    cursor.close()
    c.close()
    print("DATA DELETED SUCCESFULLY")    

def fetch_1():
    id = int(input('ENTER ROLL NO - '))
    script = f"SELECT id,name,salary FROM employee_data WHERE id = {id}"
    cursor = c.cursor()
    cursor.execute(script)
    result = cursor.fetchone()
    print(result) #print complete tuple
    print(f"ROLL NO - {result[0]}") #print value of 0th index from tuple
    print(f"NAME    - {result[1]}") #print value of 1th index from tuple
    print(f"CITY    - {result[2]}") #print value of 2th index from tuple
    print(f"MARKS   - {result[3]}") #print value of 3th index from tuple
    cursor.close()
    c.close()
    
def fetch_all():
    script = f'SELECT id,name,salary FROM employee_data'
    cursor = c.cursor()
    cursor.execute(script)
    result = cursor.fetchall()    
    # Print value by value from the tuple
    print(result)
    print("________________________")
    for row in result:
        print(f'id      - {row[0]}')
        print(f'NAME    - {row[1]}')
        print(f'SALARY  - {row[2]}')
        print('========================')
    print("________________________")  
    
def entry():
    print("ENTER THE CHOISE OF COMMAND \n ENTER 1 For entering new data \n ENTER 2 for UPADTE THE DATA \n ENTER 3 for DELETE THE DATA \n ENTER 4 for view the perticular data \n ENTER 5 for view table")
    val = int(input("ENTER THE COMMAND"))

    match val:
            case 1:
                insert()
            case 2:
                update()
            case 3:
                delete() 
            case 4:
                fetch_1()
            case 5:
                fetch_all()
            case _:
                print("``````````````````````````````````````````````````````````````````````````````````")
                print("INVALID INPUT RETRY")
                entry()

entry()                

          

            
