import math
x=float(0.0374)
y=float(-0.825)
z=float(16)
s=((1+math.sin(x+y)**2)/(x-(2*y)/(1+x*x*y*y))*math.pow(x,abs(y))+math.cos(math.atan(1/z))**2)
print(s)
