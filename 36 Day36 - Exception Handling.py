try:
    a = int(input("enter the number: "))
    print(f"print multiplication table of {a} is: ")
    i = 0
    while( i < 10 ):
        print(f"{a} X {i+1} = {a*(i+1)}")
        i += 1
except Exception as e:
    print("Inavlid input!", e)

print("some important lines of code!")
print("end of program.")