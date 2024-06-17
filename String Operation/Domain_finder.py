Email = input("Whats Your Email: ")
A = Email.find("@")
NEmail = Email[A + 1:]
print(f"For This Email {Email}, this is the Domain\n{NEmail}")