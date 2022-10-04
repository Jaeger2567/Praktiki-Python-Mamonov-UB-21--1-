c=int(input())
a=int(input())
b=int(input())
if a<2 and b>3:
    c=a+b**2
elif a>b and a>3:
    c=b**2+2
else:
    c=b
print(c)
