number=int(input("enter the number less than 100 : "))
if number<100:
    if number %2==0:
        print("the number is less than 100 and it is even number")
    else:
        print("the number is less than 100 and it is odd number")
elif number ==100:
    if number%2==0:
        print("the number is equal to 100 and it is even number")
    else:
        print("the number is odd number")
else:
    print("the number is grater than 100")