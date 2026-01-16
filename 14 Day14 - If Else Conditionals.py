# a = int(input("enter your age: "))
# print("your age is:",a)

# if(a>=18):
#     print("you can drive.")
# else:
#     print("you can't drive.")
#     print("No")
# print("Yay!")

# num = int(input("enter value of num: "))
# if(num<0):
#     print("num is a negative value.")
# elif(num==0):
#     print("num is equals to zero.")
# elif(num==999):
#     print("num is special.")
# else:
#     print("num is a positive value.")

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")