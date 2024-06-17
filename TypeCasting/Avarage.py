lst = []
amount = int(input("How many Number will you be Avaraging: "))
sum = 0
for i in range(amount):
    number = int(input("Enter the Number: "))
    lst.append(number)
for i in lst:
    sum += i
print(sum/len(lst))