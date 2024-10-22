import math

def integralRieman(f,a,b,n):
	area = 0
	h = (b-a)/n
	for i in range(n):
		area+= f(a+i*h)*h
	return area

f=lambda x: x / (x**2 + 1)

def resultadoRieman(f,a,b,n):
    Rieman = integralRieman(f,a,b,n)
    print("|Valor Aproximado: ",Rieman, "|")
    print("**************************************************")
    return Rieman

if __name__ == '__main__':
    resultadoRieman(f,0,1,4)