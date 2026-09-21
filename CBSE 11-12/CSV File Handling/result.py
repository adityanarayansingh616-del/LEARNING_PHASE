#To add data into CSV and then perform operations!
import csv
with open("filecsv.csv","w",newline="") as f:
    l=list()
    n=int(input("Enter no. of entries:"));i=1
    while i<=n:
        roll=int(input("Enter roll:"))
        nm=input("Enter name:")
        eng=float(input("Enter english marks:"))
        phy=float(input("Enter physics marks:"))
        chem=float(input("Enter chem marks:"))
        cs=float(input("Enter Computer Science marks:"))
        i+=1
        l.append([roll,nm,eng,phy,chem,cs])
    csw=csv.writer(f)
    csw.writerow(["Roll","Name","English","Physics","Chemistry","Computer Science"])
    csw.writerows(l)
with open("filecsv.csv","r",newline="") as fob:
    csr=csv.reader(fob)
    reader=csr
    next(csr)
    x=[];tot_list=list();found=False
    rollin=int(input("Enter roll to search:"))
    for data in csr:
        total=sum([float(n) for n in data[2:]])
        tot_list.append([data,total])
        print("Student name-",data[1])
        print("Total marks- ",total,"/400",sep="")
        if total>=360.00:
            x.append(data)
        if rollin==int(data[0]) and found==False:
            found=True
            pr_data=data
    if not found:
        print("Student roll not found!")
    else:
        print("Student roll found!",pr_data,sep="\n")
    print("Students whose total is atleast 360-")
    for o in x:
        print(o)
    print("Student with highest total-")
    t=tuple([c for w,c in tot_list])
    hi=max(t)
    for data in tot_list:
        if data[1]==hi:
            print(data[0])