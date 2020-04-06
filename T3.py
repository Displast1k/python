print ('ax^2+bx+c=0')
#a = int (input())
#b = int (input())
#c = int (input())
a = float ( input("Введи первое число: "))
b = float ( input("Введи второе число: "))
c = float ( input("Введи первое число: "))

d = b**2-4*a*c
if (d>0) :
	x1 = (-b+d**0.5) / (2*a)
	x2 = (-b-d**0.5) / (2*a)
	print('x1= ', x1)
	print('x2= ', x2)
elif (d == 0) :
	print ('x = ', -b/(2*a))
else:
	print('Корней нет.') 

#from math import sqrt
#a = float ( input("Введи первое число: "))
#b = float ( input("Введи второе число: "))
#с = float ( input("Введи второе число: "))

#if d > 0:
#	x1 = (-b + sqrt(d) / (2*a))
#	x2 = (-b - sqrt(d) / (2*a)) 
#	print ("x1 = %.2f" % (x1,x2))