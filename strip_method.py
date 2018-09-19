

name , char= input("enter your name and char : ").split(",")
print(f"Length of name : {len(name)}")
print(f"charecter count : {name.strip().lower().count(char.strip().lower())}")

