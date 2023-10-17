rev=0
n=eval(input("Enter the value"))
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
     print(" palindrome ")
else:
     print("Not palindrome")


