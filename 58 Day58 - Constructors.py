class Person:
    def __init__(self,name,occ):   #done done method
        print("Hey! I am a person")
        self.name = name
        self.occ = occ

    name = "harry"
    occ = "Software Developer"

    def info(self):
        print(f"{self.name} is a/an {self.occ}")

a = Person("harry","Developer")
b = Person("Divya","HR")
a.info()
b.info()

# a.name = "Divya"
# a.occupation = "HR"
# a.info()