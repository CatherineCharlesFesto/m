#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
def palindrome(a):
    length=len(a)-1
    midpoint=length//2
    for i in range(0,midpoint+1):
        if a[i]==a[length]:

            length=length-1
        else:
            print("Not a palindrome")
            return
    print("It is a palindrome")
print("Not a palindrome")
print("It is a palindrome")
tuple1=(1,2,3,3,2,1)
palindrome(tuple1)