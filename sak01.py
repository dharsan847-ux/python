a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))
if(a<b and a<c):
  print("A is smaller")
elif(b<c and b<a):
  print("B is smaller")
else:
  print("c is smaller")