Ninput = int(input("Enter the Number: "))
if __name__ == "__main__":
    match Ninput:
        case 0:
            print("Number is Zero")
        case Ninput if Ninput > 0:
            print("The number is positive")
        case Ninput if Ninput < 0:
            print("The number is negative")

