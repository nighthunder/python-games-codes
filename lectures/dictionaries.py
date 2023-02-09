contacts = {"name": "Juliana", "age": "23", "email": "juliana@hotmail.com"} #Mutable

for item in contacts:
    print(item)

for item in contacts.values():
    print(item)

for item in contacts.keys():
    print(item)

contacts["name"] = "Juliano"

print(contacts)

contacts2 = dict([("name", "Juliana"),("age","23"),("email","juliaana@hotmail.com")]) # a list of tuples

print(contacts2)