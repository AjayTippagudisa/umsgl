import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='188A1a0339@'
)

cur = conn.cursor()

class inserted:
    
    def departmentinsert(x,dptid,dptname):
        cur.execute(f"insert into department values({dptid},'{dptname}')")
        conn.commit()
        
        
    def courseinsert(x,courseid,coursename,coursefee,duration):
        cur.execute(f'insert into course values({courseid},"{coursename}",{coursefee},{duration})')
        conn.commit()
        
        
    def student_insert(x,sid,student_name,course_id,department_id):
        cur.execute(f'insert into student values({sid},"{student_name}",{course_id},{department_id})')
        conn.commit()
        
        
    def faculty_insert(x,facultyid,facultyname,departmentid,salary,courseid):
        cur.execute(f"insert into faculty values({facultyid},'{facultyname}',{departmentid},{salary},{courseid})")
        conn.commit()

        
        
    
  
        
