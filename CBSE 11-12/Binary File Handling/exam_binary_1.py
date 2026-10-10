#To add data and then create two functions to return avg transaction value of Steve and reverse the case of Hash field characters!
import pickle
with open("filebinary.bin","wb") as f:
    n=int(input("Enter no.of entries:"))
    for i in range(n):
        ID=int(input("Enter ID:"))
        User=input("Enter Username:")
        Value=float(input("Enter transaction value:"))
        Hash=input("Enter Hash:")
        Date=input("Enter transaction date:")
        pickle.dump([ID,User,Value,Hash,Date],f)
def DisplayAvg():
    l=list()
    with open("filebinary.bin","rb") as f:
        while True:
            try:
                data=pickle.load(f)
                if data[1]=="Steve":
                    l.append(data[2])
            except EOFError:
                break
    try:
        return sum(l)/len(l)
    except ZeroDivisionError:
        print("No User Steve found!")
def ReverseHashCase():
    with open("filebinary.bin","rb") as f:
        rec=[];newstr=str()
        try:
            while True:
                data=pickle.load(f)
                has=data[3]
                for char in has:
                    if char.islower():
                        newstr+=char.upper()
                    elif char.isupper():
                        newstr+=char.lower()
                    else:
                        newstr+=char
                data[3]=newstr
                rec.append(data)
                newstr=""
        except EOFError:
            pass
    with open("filebinary.bin","wb") as f:
        for record in rec:
            pickle.dump(record,f)
print(DisplayAvg())
ReverseHashCase()