def Gcd(x,y):
    while(y):
        x , y = y,(x % y)
    return x

num1 = int(input("Enter the Larger Number:\n"))
num2 = int(input("Enter the Smaller Number:\n"))
print(f"GCD of {num1} and {num2} is {Gcd(num1,num2)}")