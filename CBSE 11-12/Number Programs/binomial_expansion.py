#To expand a binomial expression to a given index using binomial coefficients.
import math
bin=input("Enter a binomial expression:")
index=int(input("Enter its index:"))
if "+" in bin:
    opends=bin.split("+")
else:
    opends=bin.split("-")
op1=opends[0]
op2=opends[1]
for i in range(index+1):
    if i%2==0:
        sign="-"
    else:
        sign="+"
    coeff=str(int((math.factorial(index)/(math.factorial(index-i)*math.factorial(i)))))
    term=coeff+op1+"^"+"("+str(index-i)+")"+op2+"^"+"("+str(i)+")"
    if i!=index:
        if "-" in bin:
           print(term,end=sign)
        else:
           print(term,end="+")
    else:
        print(term)