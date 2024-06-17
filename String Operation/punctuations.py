import string
punctuations = string.punctuation
Istring = input("Enter a String: ")
Nstring= ""
for i in Istring:
    if i in punctuations:
        1 + 1
    else:
        Nstring += i
print("New String is:\n", Nstring)
#print(punctuations)
   