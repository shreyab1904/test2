import sqlite3
conn=sqlite3.connect('cust.db')
#print("opened")

#command="CREATE TABLE customer_details (id INTEGER PRIMARY KEY,name TEXT NOT NULL, city TEXT NOT NULL, tickets INTEGER)"
#conn.execute(command)
#print("created")

#command="INSERT INTO customer_details VALUES(10,'divya','Jalgaon',3)"
#conn.execute(command)
#conn.commit()
#print("inserted")

#command="SELECT *FROM customer_details"
#result=conn.execute(command)
#for row in result:
    #id,name,city,ticket=row
    #print(row)



def view():
    command="SELECT *FROM customer_details"
    c=conn.cursor()
    c.execute(command)
    r=c.fetchall()
    for i in r:
        print(i)
    menu()

def city_wise():
    command="SELECT city,name FROM customer_details ORDER BY city ASC"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    r = c.fetchall()
    for i in r:
        print(i)

def desc():
    command="SELECT *FROM customer_details ORDER BY id DESC"
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    r = c.fetchall()
    for i in r:
        print(i)

def update():
    command="UPDATE customer_details set city='Ratnagiri' where id=2"
    conn.execute(command)
    conn.commit()
    result=conn.execute("SELECT *FROM customer_details")
    for row in result:
        print(row)

def delete():
    command="DELETE FROM customer_details where id=4"
    conn.execute(command)
    conn.commit()
    result = conn.execute("SELECT *FROM customer_details")
    for row in result:
        print(row)

def search():
    command="SELECT *FROM customer_details where name='%s'"%name.get()
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    r = c.fetchall()
    for i in r:
        print(i)

def menu():
    print("Choose 1 option: ")
    print("1 View Customers")
    print("2 Total count of ticket")
    print("3 City wise ticket sold")
    print("4 Descending order")
    print("5 Update customer")
    print("6 Delete customer")

    ch=int(input("enter your choice= "))
    if ch==1:
        view()
    elif ch==2:
        total_count()
    elif ch==3:
        city_wise()
    elif ch==4:
        desc()
    elif ch==5:
        update()
    elif ch==6:
        delete()
    elif ch==7:
        search()
    else:
        print("invalid choice")
        menu()

menu()


#conn.commit()
conn.close()

