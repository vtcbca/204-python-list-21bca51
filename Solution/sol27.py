#WAS to create list with 5 string and print only even number character of each string using UDF.
l=[]
count=0
def createList(l):
    for i in range(5):
        s=input('Enter any string : ')
        l.append(s)
createList(l)
def even(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            for j in i:
                print('{}.'.format(j))
even(l)
