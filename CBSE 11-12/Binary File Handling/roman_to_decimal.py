#To convert a Roman numeral to decimal using a pickled lookup dictionary.
import pickle
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
with open("filebinary.bin","wb") as f:
    pickle.dump(d,f)
def rodec(roman_no):
    x=0
    with open("filebinary.bin","rb") as fob:
        decimal_no=0
        decimal=pickle.load(fob)
        for i in range(len(roman_no)-1):
            if x==1:
                x=0
                continue
            numeral1=decimal[roman_no[i]]
            numeral2=decimal[roman_no[i+1]]
            if numeral1>=numeral2:
                decimal_no+=numeral1
            else:
                decimal_no+=numeral2-numeral1
                x=1
        if x==0:
            decimal_no+=decimal[roman_no[-1]]
    return decimal_no
print(rodec(input("Enter a roman number:").upper()))
#This code is not 100% efficient as it does not reject invalid roman numbers.