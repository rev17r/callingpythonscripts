import sys 
from calculation import *

a = int(sys.argv[1])
b = int(sys.argv[2])
print(a)
print(b)
ad = adding(a,b)
su = subtraction(a,b)
mu = multiplication(a,b)
di = division(a,b)

print("addition is {}, subtraction is {}, product is {}, quotient is {}".format(ad,su,mu,di)) 
