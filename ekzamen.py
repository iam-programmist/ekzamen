# И мисоли сеюмай устод ира кор кадаги бдм проста факториалш хато бд

# class Calculator:
#     @staticmethod
#     def factorial(n):
#         res=1
#         for i in range(1,n+1):
#             res*=i
#         print(res)
#     @staticmethod
#     def power(a,b):
#         print(a**b)
#     @staticmethod
#     def sqrt(n):
#         print(n**0.5)
# Calculator.factorial(int(input()))
# Calculator.power(int(input()),int(input()))
# Calculator.sqrt(int(input()))

# И мисоли панчумай устод ира кор кадаги набдм ай сабаби ки вакт нарасид

# class Student:
#     idcounter=1
#     def __init__(self,name,username,age):
#         self.id=Student.idcounter
#         self.name=name
#         self.username=username
#         self.age=age
#         Student.idcounter+=1
#     def __str__(self):
#         return f"{self.id}, {self.name}, {self.username}, {self.age}"
# class StudentManager:
#     def __init__(self):
#         self.students=[]
#     def accept(self,name,username,age):
#         student=Student(name,username,age)
#         self.students.append(student)
#         print(f"Student {name} added successfully.")
#     def display(self):
#         for student in self.students:
#             print(student)
#     def search(self,username):
#         for student in self.students:
#             if student.username==username:
#                 print(student)
#             else:
#                 print(f"No student found with username: {username}")
#     def delete(self,studentid):
#         for student in self.students:
#             if student.id==studentid:
#                 self.students.remove(student)
#                 print(f"Student with id {studentid} deleted successfully.")
#             else:
#                 print(f"No student found with id: {studentid}")
#     def update(self,studentid,name,username,age):
#         for student in self.students:
#             if student.id==studentid:
#                 if name!="":
#                     student.name=name
#                 if username!="":
#                     student.username=username
#                 if age!="":
#                     student.age=int(age)
#                 print(f"Student with id {studentid} updated successfully.")
#             else:
#                 print(f"No student found with id: {studentid}")
# obj=StudentManager()
# while True:
#     print("1. Add Student")
#     print("2. Display Student")
#     print("3. Search Student")
#     print("4. Delete Student")
#     print("5. Update Student")
#     print("6. Exit")
#     a=int(input("Select the option: "))
#     if a==1:
#         name=input("Enter name: ")
#         username=input("Enter username: ")
#         age=int(input("Enter age: "))
#         obj.accept(name,username,age)
#     if a==2:
#         obj.display()
#     if a==3:
#         username=input("Enter username: ")
#         obj.search(username)
#     if a==4:
#         studentid=int(input("Enter student id to delete: "))
#         obj.delete(studentid)
#     if a==5:
#         studentid=int(input("Enter student id to update: "))
#         name=input("Enter name: ")
#         username=input("Enter username: ")
#         age=input("Enter age: ")
#         obj.update(studentid,name,username,age)
#     if a==6:
#         print("Program has ended.")
#         break
#     else:
#         print("Invalid option")

# И мисоли шашумай устод ишам ранги панчум кор каданда успет накадм

# class User:
#     def __init__(self,firstname,lastname,username,password):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.username=username
#         self.password=password
# class UserManager:
#     def __init__(self):
#         self.users=[]
#     def registration(self):
#         firstname=input("Enter first name: ")
#         lastname=input("Enter last name: ")
#         username=input("Enter username: ")
#         password=input("Enter password: ")
#         if password.isdigit():
#             user=User(firstname,lastname,username,password)
#             self.users.append(user)
#             print(f"User {username} registered successfully.")
#         else:
#             print("Password must be integers.")
#     def login(self):
#         username=input("Enter username: ")
#         password=input("Enter password: ")
#         for user in self.users:
#             if user.username==username:
#                 if user.password==password:
#                     print("You login successfully.")
#                 else:
#                     print("Password incorrect.")
#             else:
#                 print(f"User with username {username} not found.")
#     def changepassword(self):
#         username=input("Enter username: ")
#         oldpassword=input("Enter old password: ")
#         newpassword=input("Enter new password:")
#         for user in self.users:
#             if user.username==username:
#                 if user.password==oldpassword:
#                     user.password=newpassword
#                     print("Password changed successfully.")
#                 else:
#                     print("Old password is incorrect.")
#             else:
#                 print("User with username {username} not found.")
#     def getusers(self):
#         for user in self.users:
#             print(f"Username: {user.username}, Name: {user.firstname} {user.lastname}")
# obj=UserManager()
# while True:
#     print("1. Registration")
#     print("2. Login")
#     print("3. Change Password")
#     print("4. Show All Users")
#     print("5. Exit")
#     a=input("Select the option: ")
#     if a=="1":
#         obj.registration()
#     if a=="2":
#         obj.login()
#     if a=="3":
#         obj.changepassword()
#     if a=="4":
#         obj.getusers()
#     if a=="5":
#         print("Program has ended.")
#         break
#     else:
#         print("Invalid option")