# How to find out which value is greater,lesser, equal to and not equal to other
a = int(input("enter a number"))
b = int(input("enter a number"))
if a > b:
  print(a, "is greater than ",b)
#This will if the user will give the value of "a" greater as compared to "b"
elif  a <= b: # This is the start of condition in a condition
 if a < b:
    print(a," is less than",b)
#This will if the user will give the value of "a" lesser as compared to "b"
 elif a == b:
    print(a," is equal to", b)
#This will if the user will give the value of "a" equal to "b"
else:
  print(a," is not equal to ",b)
#This will if the user will give the value of "a" not equal to "b"
