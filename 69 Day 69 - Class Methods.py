class Empolyee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changecompny(self,newCompany):
        self.company = newCompany

e1 = Empolyee()
e1.name = "harry"
e1.show()
e1.changecompny("tesla")
e1.show()
print(Empolyee.company) 