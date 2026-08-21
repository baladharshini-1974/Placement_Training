num=int(input("Enter a number:"))
square=num*num
sum=0
while square>0:
    digit=square%10
    sum+=digit
    square//=10
if sum==num:
    print("Neon number")
else:
    print("Not a neon number")