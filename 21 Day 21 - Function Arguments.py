def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average of numbers is",sum/len(numbers))
    return sum/len(numbers)

c = average(1,2,3,4,5,6)
print("Average of numbers is",c)

def name(**name):
    print(type(name))
    print("Hello!,",name["fname"],name["mname"],name["lname"])

name(fname="Abhay", mname="Singh", lname="Chauhan")