import sqlite3

conn=sqlite3.connect('info.db')

#command="CREATE TABLE employees(empCode INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, phone INTEGER , email TEXT, salary INTEGER, company_name TEXT )"
#conn.execute(command)
#print("created")

#command="INSERT INTO employees VALUES(5,'divya',987678987,'divya@gmail.com',56345,'Accenture')"
#conn.execute(command)
#conn.commit()
'''
command="SELECT *FROM EMPLOYEES"
result=conn.execute(command)
conn.commit()
for row in result:
  print(row)
'''

def view():
    command = "SELECT *FROM employees"
    c = conn.cursor()
    c.execute(command)
    r = c.fetchall()
    for i in r:
        print(i)

def search():
    command = "SELECT *FROM employees WHERE name='renita'"
    c = conn.cursor()
    c.execute(command)
    r = c.fetchall()
    for i in r:
        print(i)

def update():
    command = "UPDATE employees set phone=8769876435 where empCode=3 "
    conn.execute(command)
    conn.commit()
    result = conn.execute("SELECT *FROM employees")
    for row in result:
        print(row)

def delete():
    command = "DELETE FROM employees where empCode=3"
    conn.execute(command)
    conn.commit()
    result = conn.execute("SELECT *FROM employees")
    for row in result:
        print(row)

def range():
    command = "SELECT *FROM employees where salary>50000"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)

def count():
    command = "SELECT COUNT(*) FROM employees"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)

def asce():
    command = "SELECT *FROM employees WHERE SALARY>20000 AND SALARY<60000 ORDER BY name ASC"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)

def less_than_avg():
    command = "SELECT *FROM employees WHERE salary<(select AVG(salary) FROM employees)"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)


def management():
    print("Choose 1 option: ")
    print("1 ADD ")
    print("2 VIEW ")
    print("3 SEARCH")
    print("4 UPDATE ")
    print("5 DELETE")
    print("6 Display employees whose salary is greater than 50000")
    print("7 COUNT")
    print("8 Employees in ascending order with salary range 20000 to 60000")
    print("9 Salary less than the average salary of employees")

    ch=int(input("enter your choice= "))
    if ch==1:
        add()
    elif ch==2:
        view()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        range()
    elif ch==7:
        count()
    elif ch==8:
        asce()
    elif ch==9:
        less_than_avg()
    else:
        print("invalid choice")
        management()

management()


