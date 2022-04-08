#WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string in strSymmetric() and check string is symmetric or not.
#A string is said to be symmetrical if both the halves of the string are the same.

s1=input("Enter the string : ")
def strSymmetric(s1):
    
    l=len(s1)
    s2=s1[0:l//2]
    s3=s1[l//2:]
    print("symmatrical string " if s2==s3 else "asmmatrical string")
strSymmetric(s1)
