import doctest
import sqlite3
conn=sqlite3.connect('test.db')
print("opened successfully")

command='''insert into  todo values(3,'work','21/2/21','done')'''
conn.execute(command)
conn.commit()
print(conn.total_changes)
'''
for row in result:
    print(row)             #output in tuple format
    id,task,date,status=row    #for removing tuple
    print(id,task,date,status)
'''
'''
#fetchone() it return in tuple format

r=result.fetchone()
print(r)
'''
#fetchall() return in the format of list



