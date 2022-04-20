# WAS to enter any number and print the prime number between 1 to n number using UDF primeNo().
def primeNo(no):
	for i in range(no):
		if i%2==1:
			if i%3!=0:
				if i%5!=0:
					if i%7!=0:
						print(i)
no=int(input('Enter a number uptil you want to print the prime number : '))
primeNo(no)