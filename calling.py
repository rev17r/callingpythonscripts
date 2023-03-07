from calculation import *

a = int(input("enter a number: "))
b = int(input("enter a number: "))

ad = adding(a,b)
su = subtraction(a,b)
mu = multiplication(a,b)
di = division(a,b)

print("addition is {}, subtraction is {}, product is {}, quotient is {}".format(ad,su,mu,di)) 