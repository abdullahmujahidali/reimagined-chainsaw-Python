def Newton(F,dF,x0,epsilon):
n = 0
xn = x0 # initially
while abs(F(xn)) >= epsilon: #criterion for stopping
Xn = xn - F(xn)/dF(xn) # newton's
xn = Xn
if n==25 or abs(dF(xn))<epsilon: # criteria for aborting
print("Method couldn't find root after maximum iterations")
return None
n = n + 1
return xn

#------------------- test 1---------------------------
def f1(x):
return x**2-5

def df1(x):
return 2*x


x = 2
xn = Newton(f1,df1,x,1e-10)

if type(xn) is float:
print ("f1(%1.8f) = %1.8f" %(xn,f1(xn)))
  
#--------------------- test 2 -------------------------
def f2(x):
return x**5 - x**4 + x**2 + x - 1

def df2(x):
return 5*x**4 - 4*x**3 + 2*x + 1

x = 1 # intial guess
xn = Newton(f2,df2,x,1e-10)

if type(xn) is float:
print ("f2(%1.8f) = %1.8f" %(xn,f2(xn)))

