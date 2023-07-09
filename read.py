import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='188A1a0339@'
)


cur = conn.cursor()

class readed:
    
    def readdatafromdepartment(x,id):
        cur.execute(f'select * from department where departmentid = {id}')
        print(cur.fetchall())
        
        
    def read_data_from_course(x,courid):
        cur.execute(f'select * from course where courseid = {courid}')
        print(cur.fetchall())
        
    def read_data_from_student(x,stid):
        cur.execute(f'select * from student where sid = {stid}')
        print(cur.fetchall())
        
        
    def read_data_from_faculty(x,fid):
        cur.execute(f'select * from faculty where facultyid = {fid}')
        print(cur.fetchall())
        
