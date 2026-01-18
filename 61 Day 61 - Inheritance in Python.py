class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showDetail(self):
          print(f"Tha name of Employee:{self.id} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
      print("The default language is python")

e1 = Employee("Rohan",420)
e1.showDetail()
e2 = Programmer("harry",1)
e2.showDetail()
e2.showlanguage()