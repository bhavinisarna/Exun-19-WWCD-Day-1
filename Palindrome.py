# Given a number n, check whether it is a palindrome or not.
# Given a number n, check whether it is a palindrome or not.
n=int(input("enter a number"))
t=n
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
if (t==rev):
    print("this is a palindrome")
else:
    print("this is not a palindrome")
