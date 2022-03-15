import  sqlite3

con=sqlite3.connect('student.db')



sqlite_query='''CREATE TABLE stud_marks(
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                marks INTEGER NOT NULL'''

con.execute(sqlite_query)
print("table created")

sqlite_insert_query='''INSERT INTO stud_marks
                        VALUES (1000,'SHREYA',98)'''

cursor.execute(sqlite_insert_query)

print("record inserted")

con.commit()
con.close()