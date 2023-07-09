import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='188A1a0339@'
)

cur = conn.cursor()


class deleted:
    
    def deletefromdepartment(x,id):
        cur.execute(f"delete from department where departmentid ={id}")
        conn.commit()
        
        
    def delete_from_course(x,courseid):
        cur.execute(f'delete from course where courseid={courseid}')
        conn.commit()
        
    def delete_from_student(x,sid):
        cur.execute(f'delete from student where student_id={sid}')
        conn.commit()
        
    
    def delete_from_faculty(x,fid):
        cur.execute(f'delete from faculty where faculty_id={fid}')
        conn.commit()