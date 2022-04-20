s=input('Enter a string : ')
l=[]
num=int(input('Enter a number : '))
if num == 1:
    for i in s:
        if i not in l:
            print('{}-->{}'.format(i,s.count(i)))
        l.append(i)
if num == 2:
    for i in s:
        if i not in l:
            print('{}'.format(i))
        l.append(i)
if num == 3:
    s1=input('Enter a sentence : ')
    s2=s1.split()
    no=int(input('Enter a number : '))
    for i in s2:
        c=0
        for j in i:
            c+=1
        if(c>no):
            print(i)
