from insert import inserted
from update import updated
from delete import deleted
from read import readed

obj = inserted()
obj1 = updated()

obj2 = deleted()
obj3 = readed()


print('------------------------UMS PROJECT----------------------------')
print('***you have 4 operations on database:*****')
print('for adding the values enter "Add":')
print('for updating the values enter "Update":')
print('for deleting the values enter "Delete":')
print('for featching the values enter "Read":')

operation = input('please enter the "Operation":')



if operation == 'Add':
    print('for inserting data in department table please press - 1:')

    tab = int(input('please enter the number to insert data in table :'))

    if tab == 1:
        department_id = int(input('please enter department_id:'))
        department_name = input('please enter department name:')
        obj.departmentinsert(department_id,department_name)
        print('your data entered successfully')
        
        
        
if operation == 'Update':
    print('for updating the data in department table please press - 1:')
    
    tab = int(input('please enter the number to update data in table :'))
    
    if tab==1:
        column_1 = input('please enter the column name :')
        new_value = input('please enter the new value :')
        column_2 = input('please enter the second column name : ')
        old_value = int(input('please enter the old value :'))
        obj1.update_department(column1=column_1,newvalue=new_value,column2=column_2,oldvalue=old_value)
        print('your values updated successfully')


if operation == 'Delete':
    print("for deleting the data in department table please press - 1 :")
    
    tab = int(input("please enter the number to delete the data in table :"))
    
    if tab==1:
        id = int(input("please enter the department id where you want to delete the data :"))
        obj2.deletefromdepartment(id)
        print('your data deleted successfully')
        
        
        
        
if operation == 'Read':
    print('for reading the data in department please press 1 :')
    
    tab = int(input('plase enter the number to delete the data in table :'))
    
    if tab==1:
        id=int(input('please enter the departmentid to featch the data from department table :'))
        obj3.readdatafromdepartment(id)
    
    
    


if operation == 'Add':
    print('for inserting data in course table please press - 2:')

    tab = int(input('please enter the number to insert data in table :'))

    if tab == 2:
        course_id = int(input('please enter course_id:'))
        course_name = input('please enter course name:')
        course_fee = input('please enter course fee :')
        course_duration = int(input('please enter course duration :'))
        obj.courseinsert(course_id,course_fee,course_fee,course_duration)
        print('your data entered successfully in course table')
        
        
if operation == 'Update':
    print('for updating the data in coourse table please press - 2:')
    
    tab = int(input('please enter the number to update data in table :'))
    
    if tab==2:
        column_1 = input('please enter the column name :')
        new_value = input('please enter the new value :')
        column_2 = input('please enter the second column name : ')
        old_value = int(input('please enter the old value :'))
        obj1.update_course(column1=column_1,newvalue=new_value,column2=column_2,oldvalue=old_value)
        print('your values updated successfully')
        
        
if operation == 'Delete':
    print('for deleting the data in course table please press - 2 :')
    
    tab = int(input('please enter the number to update data in table :'))
    
    if tab==2:
        cour_id= int(input('please enter the course id where you want to delete data :'))
        obj2.delete_from_course(cour_id)
        print(('your data deleted successfully'))
        
        
if operation == 'Read':
    print('for reading the in course table please press - 2 :')
    
    tab = int(input('please enter the number to read the data in table :'))
    
    if tab==2:
        course_id = int(input('please enter the course id to featch the data from course table :'))
        obj3.read_data_from_course(course_id)
        
        
if operation=='Add':
    print('for inserting the data in student table please press - 3 :')
    
    tab = int(input('please enter the number to insert the data in table :'))
    
    if tab == 3:
        sid=int(input('please enter the student id :'))
        sname=input('please enter the student name :')
        courseid=int(input('please enter the course id :'))
        departmentid = int(input('please enter the department id :'))
        obj.student_insert(sid,sname,courseid,departmentid)
        print('your data entered successfully')
        
        
if operation == 'Update':
    print('for updating the data in student table please press - 3:')
    
    tab = int(input('please enter the number to update data in table :'))
    
    if tab==3:
        col1 = input('please enter the column name :')
        new = input('please enter the new value :')
        col2 = input('please enter the second column name : ')
        old = int(input('please enter the old value :'))
        obj1.update_student(column1=column_1,newvalue=new_value,column2=column_2,oldvalue=old_value)
        print('your values updated successfully')
        
        
if operation == 'Delete':
    print('for deleting the data in student table please press - 3 :')
    
    tab = int(input('please enter the number to update data in table :'))
    
    if tab==3:
        stu_id= int(input('please enter the student id where you want to delete data :'))
        obj2.delete_from_student(stu_id)
        print(('your data deleted successfully'))
        
        
        
if operation == 'Read':
    print('for reading the in student table please press - 3 :')
    
    tab = int(input('please enter the number to read the data in table :'))
    
    if tab==3:
        stu_id = int(input('please enter the student id to featch the data from student table :'))
        obj3.read_data_from_student(stu_id)
        
        
if operation == 'Add':
    print('for inserting the values in faculty table plaese press - 4 :')
    
    tab = int(input('plase enter the number to inset the data in  table :'))
    
    if tab==4:
        faculty_id=int(input('please enter the faculty id :'))
        faculty_name =input('please enter the faculty name :')
        department_id = int(input('please enter the department id :'))
        salary = input('please enter the salary :')
        cour_id = int(input('please enter the course id :'))
        obj.faculty_insert(faculty_id,faculty_name,department_id,salary,cour_id)
        print('your data entered successfully')
        
        
        
if operation == 'Update':
    print('for updating the data in faculty table please press - 4:')
    
    tab = int(input('please enter the number to update data in table :'))
    
    if tab==4:
        column_1 = input('please enter the column name :')
        new_value = input('please enter the new value :')
        column_2 = input('please enter the second column name : ')
        old_value = int(input('please enter the old value :'))
        obj1.update_student(column1=column_1,newvalue=new_value,column2=column_2,oldvalue=old_value)
        print('your values updated successfully')
        
        
        
if operation == 'Delete':
    print('for deleting the values in faculty table please press  - 4 :')
    
    tab = int(input('please enter the number to delete the data in table :'))
    
    if tab==4:
        facultyid=int(input('please enter the faculty id :'))
        obj2.delete_from_faculty(facultyid)
        print('your data deleted successfully')
        
        
if operation == 'Read':
    print('for reading the values in faculty table please press  - 4 :')
    
    tab = int(input('please enter the number to Read the data in table :'))
    
    if tab==4:
        facalid=int(input('please enter the faculty id :'))
        obj3.read_data_from_faculty(facalid)
        
        
        

        