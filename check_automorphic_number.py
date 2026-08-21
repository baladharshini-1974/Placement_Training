num=int(input("Enter a number:"))
square=num*num
sum=0
if str(square).endswith(str(num)):
    print("Automorphic number")
else:
    print("Not an automorphic number")