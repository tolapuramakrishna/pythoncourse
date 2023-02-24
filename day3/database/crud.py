'''
We are connrcting to sqllite3 db to perform crud
1.code first - create db,create table, perform crud

'''
import sqlite3
from employee import Employee as e

def connectDb():
    global conn
    conn = sqlite3.connect('employee.db')
    global cursor
    cursor = conn.cursor()
    print('connected to Db')

def create_table():
    try:
        query = 'CREATE TABLE emps(first text,last text, pay integer)'
        cursor.execute(query)
        print("emps table created in Db")
    except Exception as ex:
        print(ex)

def insertEmp(emp):
    try:
        query = 'INSERT INTO emps (first,last,pay) VALUES(?,?,?)'
        values  = (emp.first,emp.last,emp.pay)
        cursor.execute(query,values)
        cursor.execute('commit')
        print("record inserted")
    except Exception as ex:
        print(ex)

def getEmps():
    query = 'Select * from emps' #add where 
    cursor.execute(query)
    return cursor.fetchall()

def remove_emp(emp):
    cursor.execute('DELETE from emps where :last=last',{'last':emp.last})
    cursor.execute('commit')
    print('record Deleted with ',emp)

if __name__ == '__main__':
    print("welcome db world")
    connectDb()
    #create_table()
    emp1 = e('Murthy','Sr',5000)
    emp2 = e('Abc','def',6000)
    # insertEmp(emp1)
    # insertEmp(emp2)
    data = getEmps()
    # remove_emp(data[0])
    remove_emp(e('Abc','def',6000))
    data = getEmps()
    print(data)
    cursor.close()
    conn.close()
    print('Db conn closed')