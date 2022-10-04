import math
x = float(-4.5)
y = float(0.75*10**-4)
z = float(-0.845*10**2)
s=(math.sqrt((math.sqrt(9 + (x-y)**2)))/(x**2 + y**2 + 2) - (math.exp(abs(x-y))*(math.tan(z))**3) )
print(s)
