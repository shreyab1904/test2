import sqlite3

conn=sqlite3.connect('emp1.db')

#command="CREATE TABLE employee (empCode INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, phone INTEGER , email TEXT, salary INTEGER, company_name TEXT )"
#conn.execute(command)
##print("created")

#command="INSERT INTO employee VALUES(10,'prajkta',76423656,'prajkta@gmail.com',45788,'Persistent')"
#conn.execute(command)
#conn.commit()
#print("inserted")

'''
command="SELECT *FROM EMPLOYEE"
result=conn.execute(command)
conn.commit()
for row in result:
  empCode,name,phone,email,salary,company_name=row
  print(row)
'''
def add():
    #name=input("Enter employee name:")
    empCode=input("enter employee id")
    name=input("Enter Employee")
    phone=input("enter phone")
    email=input("enter email")
    salary=input("enter salary")
    company_name=input("enter company name")
    data=(empCode,name,phone,email,salary,company_name)

    command="INSERT INTO employee VALUES(?,?,?,?,?,?)"
    c=conn.cursor()
    c.execute(command,data)
    conn.commit()
    print("Employee added successfully")
    r = c.fetchall()
    for i in r:
        print(i)
    conn.close()


def view():
    command = "SELECT *FROM employee"
    c = conn.cursor()
    c.execute(command)
    r = c.fetchall()
    for i in r:
        print(i)


def search():
    command="SELECT *FROM employee WHERE name='hritik'"
    c = conn.cursor()
    c.execute(command)
    r = c.fetchall()
    for i in r:
        print(i)


def update():
    command = "UPDATE employee set phone=88053695 where empCode=3 "
    conn.execute(command)
    conn.commit()
    result = conn.execute("SELECT *FROM employee")
    for row in result:
        print(row)


def delete():
    command = "DELETE FROM employee where empCode=10"
    conn.execute(command)
    conn.commit()
    result = conn.execute("SELECT *FROM employee")
    for row in result:
        print(row)


def salary_range():
    command="SELECT *FROM employee where salary>50000"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)


def count():
    command="SELECT COUNT(*) FROM employee"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)


def ascending():
    command="SELECT *FROM employee WHERE SALARY>20000 AND SALARY<55000 ORDER BY name ASC"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)


def less_than_avg():
    command="SELECT *FROM employee WHERE salary<(select AVG(salary) FROM employee)"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    result = c.fetchall()
    for row in result:
        print(row)


def menu():
    print("Choose 1 option: ")
    print("1 ADD employees")
    print("2 VIEW employees")
    print("3 SEARCH an employee")
    print("4 UPDATE employee")
    print("5 DELETE an employee")
    print("6 Display employees whose salary is greater than 50000")
    print("7 COUNT of total employees")
    print("8 Employees in ascending order with salary range 20000 to 45000")
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
        salary_range()
    elif ch==7:
        count()
    elif ch==8:
        ascending()
    elif ch==9:
        less_than_avg()
    else:
        print("invalid choice")
        menu()

menu()