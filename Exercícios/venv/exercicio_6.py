# Cálculo de raízes
import math

def SegundoGrau(a,b,c):
    delta = ((b**2) - (4*a*c))

    if delta < 0:
        print("A equação não tem raízes")

    else:
        x1 = (-b + math.sqrt(delta))/ 2*a
        x2 = (-b - math.sqrt(delta))/ 2*a
        print("raízes: %f e %f" %(x1,x2))


SegundoGrau(1,-64,663)