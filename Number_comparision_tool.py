#step 1: get two number user input
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))

# step 2 comparision :
if num1 == num2:
    print(f"both number are equal {num1}")
elif num1<num2:
    print(f"the {num1} is less than the {num2}")
else:
    print(f"the {num1} is grater than the {num2}")

# step 3 chek the number is zero or not:
if num1==0 or num2==0:
    print("At least one number is zero")
else:
    print("both number are non zero")