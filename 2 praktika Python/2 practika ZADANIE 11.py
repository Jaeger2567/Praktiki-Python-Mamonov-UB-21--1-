import math
x = float(6.251)
y = float(0.827)
z = float(25.001)
s=(y**(pow(abs (x),1/3))+(math.cos(y))**3 * ((abs(x-y)*(1 + (((math.sin(z))**2)/(pow(x+y,1/2)))))/(math.exp(abs(x-y)) + x/2)))
print(s)
