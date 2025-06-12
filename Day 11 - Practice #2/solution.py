contacts = {}

for _ in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone

print("Contact book:", contacts)
