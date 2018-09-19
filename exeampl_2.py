# name = input("Enter your name : ")
# print(f"Your name is {name[:1]}")


name, char = input("enter name and charter : ").split(",")
print(f"length of your name {len(name)} ")
# print(f"charecter count : {name.count(char)}")   #case sensitive

print(f"charecter count : {name.lower().count(char.lower())}")



name, char = input("Enter your name  and char : ").split(",")
print(f"length of name {len(name)}")
print(f"char. count {name.lower().count(char.lower())}")




