def collatz(number):
    if number%2==0:
        result=number//2
        print(result)
        return result
    else:
        result=3*number+1
        print(result)
        return result

try:
    n=int(input("enter a number:"))
    while n!=1:
        n=collatz(n)
except ValueError:
    print("Error: please enter a valid integer")