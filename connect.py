import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.connection = sqlite3.connect("emp.db")
            #5
            try:
                  self.connection.execute('''create table if not exists employee(
                        emp_name text,
                        email text,
                        mobile text,
                        emp_type char,
                        emp_salary integer,
                        emp_exp integer
                  )''')
                  print("DB created")
            except:
                  pass
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            self.connection.execute("insert into employee values (?,?,?,?,?,?)",(ename,eemail,emob,etype,eexp,esalary))
            self.connection.commit()

      def display(self):
            #7
            e_name = input("Enter the employee: ")
            show_data = self.connection.execute("select * from employee where emp_name=:emp_name",{"emp_name":e_name})
            # print(show_data.fetchall())

            for i in show_data:
                  print("Your Name :",i[0])
                  print("Your Email :",i[1])
                  print("Your Mobile No. :",i[2])
                  print("Your Job Type :",i[3])
                  print("Your Experience :",i[4])
                  print("Your Salary :",i[5])