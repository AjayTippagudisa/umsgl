import mysql.connector
conn =mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='188A1a0339@'
)

cur = conn.cursor()

class updated:
    
    def update_department(x,column1,newvalue,column2,oldvalue):
        cur.execute(f"update department set {column1}='{newvalue}' where {column2}={oldvalue}")
        conn.commit()
        
        
    def update_course(x,column1,newvalue,column2,oldvalue):
        cur.execute(f"update course set {column1}='{newvalue}' where {column2}={oldvalue}")
        conn.commit()
        
    
        
        
    def update_student(x,column_1,new_value,column_2,old_value):
        cur.execute(f"update student set {column_1} = '{new_value}' where {column_2} = {old_value}")
        conn.commit()
        
        
    def update_faculty(x,column1,newvalue,column2,oldvalue):
        cur.execute(f"update department set {column1}='{newvalue}' where {column2}={oldvalue}")
        conn.commit()

