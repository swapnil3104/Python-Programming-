Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Num3 = int(input("Enter third number: "))

if (Num1 > Num2 and Num1 > Num3):
    print("Greater number is:", Num1)
elif (Num2 > Num1 and Num2 > Num3):
    print("Greater number is:", Num2)
else:
    print("Greater number is:", Num3)