import psycopg2

con = psycopg2.connect(database='postgres', user='postgres', password='1234',
                       host='127.0.0.1', port='5432')
print('Database opened successfully')

cur = con.cursor()
# cur.execute('''create table employee(
#             id int primary key not null,
#             fname text ,
#             lname text ,
#             age int,
#             department char(50),
#             salary int
#             );''')
# con.commit()
# con.close()

class Employee :
    employees = []
    def __init__(self ,id,first_name,last_name,age ,department ,salary ):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.department=department
        self.salary=salary
        Employee.employees.append(self)
        cur.execute(f"Insert into employee(id, fname,lname, age, department,salary) values( {id}, '{first_name}' ,'{last_name}', {age}, '{department}',{salary})")


    def transfer(self,dep):
        self.department=dep
        cur.execute(f"Update employee set department='{self.department}' where id={self.id}")
        
    def fire (self):
        Employee.employees.remove(self)
        cur.execute(f"delete from employee where id={self.id}")
        


    def show(self):
        print(self.id,self.first_name,self.last_name,self.age,self.department,self.salary)

    @staticmethod
    def List_employees():
        for i in Employee.employees:
            i.show()


# e1 =Employee(5,'ahmed','zaki',5,'x',1000)
# e1.transfer('y')
# e1.show()
# Employee.List_employees()
# e1.fire()
# con.commit()



class Manager(Employee):
    def __init__ (self ,id,first_name,last_name,age ,department ,salary,managed_department):
        Employee.__init__(self ,id,first_name,last_name,age ,department ,salary)
        self.managed_department=managed_department

    def show(self):
        print(self.id,self.first_name,self.last_name,self.age,self.department,"confidential" ,self.managed_department)
        
# m1=Manager(2,'ahmed','zaki',5,'x','1000' ,'x')
# m1.show()
# m1.transfer('z')
# m1.fire()
# con.commit()

state=True
while  state:
    op =input("enter emp to add employee , enter mgr to add manager , enter edit to edit department , enter del to delete ,enter  list to list :")
    if(op=="del"):
        id=int(input("enter id"))
        for i in Employee.employees:
            if(i.id==id):
                i.fire()

    elif(op=="edit"):
        id=int(input("enter id"))
        dep=input("enter department")
        for i in Employee.employees:
            if(i.id==id):
                i.transfer(dep)
    elif(op=="emp"):
        id=int(input("enter id:"))
        fname=input("enter fname :")
        lname=input("enter lname :")
        age=int(input("enter age :"))
        department=input("enter department :")
        salary=int(input("Salary:"))
        Employee(id,fname,lname,age,department,salary)

    elif(op=="mgr"):
        id=int(input("enter id:"))
        fname=input("enter fname :")
        lname=input("enter lname :")
        age=int(input("enter age :"))
        department=input("enter department :")
        salary=int(input("Salary:"))
        manged_dep=input("enter managed department :")
        Manager(id,fname,lname,age,department,salary,manged_dep)
    elif(op=='list'):
        Employee.List_employees()
    check=input(" continue or enter q ")
    if(check=='q'): state=False            
con.commit()
con.close()