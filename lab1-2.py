from math import *

x = float(input("X (в градусах) = "))
y = float(input("Y (в градусах) = "))

x *= pi/180
y *= pi/180 
z = (sin(x)**2 + cos(y)**2)*2

print(z)