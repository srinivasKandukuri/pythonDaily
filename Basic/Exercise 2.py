a= int(input("enter a number"))

if(a>0):
  if(a%2 == 0):
    print("is a even number")
  else:
    print("is a odd number")
elif(a<0):
  if(a%2 == 0):
    print("is a even -ve")
  else:
    print("is a odd +ve")
else:
  print("is a even and zero")
