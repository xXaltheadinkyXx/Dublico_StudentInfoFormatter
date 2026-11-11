

firstn = input("Enter first name: ")
lastn = input("Enter last name: ")
section = input("Enter section: ")
favoritesub = input("Enter favorite subject: ")

print()
print('Formatted Output: ')

fn = firstn.title()
ln = lastn.title()
FN = firstn.upper()
LN = lastn.upper()
sc = section.upper()
fs = favoritesub.title()
fullname = (fn + " "+ln)
totalchar = len(fullname)

print("Name:", firstn, lastn)
print("Name Code:", FN, LN)
print("Section:", sc)
print("Favroite Subject:", fs)
print(f"Character Count:{totalchar}")



