#Write a script to create UDF which check string is palindrome or not.

def palin():
    s=input("Enter any string : ")
    s1=s[::-1]
    if(s1==s):
        print('It is a palindrome string.')
    else:
        print('IT is not a palindrome string.')
palin()
