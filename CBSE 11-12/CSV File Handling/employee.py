#To add data into a CSV file and then read it to print conditioned data and also search for an employee.
import csv
with open("filecsv.csv","w",newline="") as fob:
    writer=csv.writer(fob)
    writer.writerow(["Employee ID","Name","Department","Salary"])
    while True:
        emp_id=int(input("Enter employee id:"))
        nm=input("Enter name:")
        dpt=input("Enter department:")
        sal=float(input("Enter salary:"))
        writer.writerow([emp_id,nm,dpt,sal])
        x=input("More data?[Y/N]")
        if x.upper()=="N" or x.upper()=="NO":
            break
f=open("filecsv.csv","r",newline="")
reader=list(csv.reader(f))
header=reader[0]
c=0;found=False;tot_sal=0.0
ID=int(input("Enter ID to search:"))
for data in reader[1:]:
    if data[2].upper()=="IT":
        print(data)
    if float(data[3])>50000.0:
        c+=1
    tot_sal+=float(data[3])
    if int(data[0])==ID and found==False:
        found=True
        pr_data=data
if not found:
    print("Employee ID not found!")
else:
    print("Employee ID found!",pr_data,sep="\n")
print("Total combined salary- INR",tot_sal,sep="",end="/-\n")
print("Total employees with salary more than 50000=",c)
f.close()