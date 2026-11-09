num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

addition=num1+num2
difference=num1-num2
product=num1*num2


print("addition:", addition)
print("difference:", difference)
print("product:",product)

if num2!=0:
    divide=num1/num2
    print("divide:",divide)
else:
    print("division: cannot divide by 0")
