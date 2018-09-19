# num1 = input("enter first number :")
# num2 = input("enter second number :")
# num3 = input("enter third number :")
# (int(num1)+int(num2)+int(num3))/3
# print(f"Average of three number  :{(int(num1)+int(num2)+int(num3))/3}")


#print in one line

num1,num2,num3 = input("enter three number  : ").split(",")
print(f"Average of three number  :{(int(num1)+int(num2)+int(num3))/3}")
