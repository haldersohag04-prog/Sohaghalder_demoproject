a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("1.addition:")
print("2.multiplication:")
print("3.substraction:")
print("4.divide:")
print("5.remainder:")
choice=int(input("\n enter choice(1 to 5):" ))
print("your choice is :",choice)

if choice==1 :
 print("you perform addition:", a+b)
 
elif choice==2 :
 print("you perform multiplication:", a*b)

elif  choice==3:
 print("you perform substractionn:", a-b)

elif choice==4 :
 print("you perform divide:", a/b)

elif  choice==5:
 print("you perform remainder:", a%b)
 
else:
 print("you enter wrong choice ")