import sys 
from calculation import *

a = sys.argv[1]
b = sys.argv[2]
a = int(float(a))
b = int(float(b))
ad = adding(a,b)
su = subtraction(a,b)
mu = multiplication(a,b)
di = division(a,b)

print("addition is {}, subtraction is {}, product is {}, quotient is {}".format(ad,su,mu,di)) 
