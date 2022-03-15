import  sqlite3

con=sqlite3.connect('student.db')

cursor=con.cursor()

sqlite_select_query='''SELECT *FROM stud_marks'''

cursor.execute(sqlite_select_query)

records=cursor.fetchall()

print(records)

for row in records:
    print('id= ',row[0])
    print('name= ',row[1])
    print('marks: ',row[2])