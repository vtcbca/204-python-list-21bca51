#WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().
l=[]
count=0
def createList(l):
    for i in range(5):
        s=input('Enter any string : ')
        l.append(s)
createList(l)
def evenOdd(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            print('Strings which have even length are {} is {}.'.format(i,count))
evenOdd(l)
