#STUDENT MANAGEMENT SYSTEM--Covering all topics from Class 11 and 12 CBSE Computational Thinking and Programming!
import pickle as pk,csv
from statistics import median,mode
with open("filebinary1.bin","rb") as fob:
    try:
        students=pk.load(fob)
    except EOFError:
        students=dict()
with open("extra.txt","r") as file:
    data=file.read()
    if data=="":
        stack=[]
    else:
        stack=eval(data)
def add_modify(roll,name,marks):
    values=list(students.values())
    value={"name":name,"marks":marks}
    if students.setdefault(roll,value) in values:
        students[roll]=value
        print("Updated!")
    else:
        print("Added!")
def display(roll):
    data=students.get(roll,"Given roll not found!")
    if isinstance(data,str):
        print(data)
        return None
    marks=data['marks']
    print("Name-",data["name"])
    print("Marks-",marks)
    print("Total- ",sum(marks),"/500",sep=str())
    print("Average-",sum(marks)/5)
    print("Highest marks-",max(marks))
    print("Lowest-",min(marks))
    print("Median-",median(marks))
    print("Mode-",mode(marks))
def search():
    i=input("Enter R to search with roll or N for name or M for mark:")
    if i.upper()=='R':
        ch=input("Enter roll:")
    elif i.upper()=='N':
        ch=input("Enter name:")
    elif i.upper()=='M':
        ch=input("Enter mark:")
    else:
        print("Invalid choice!")
        return None
    l=[];c=0
    for roll,details in students.items():
        marks=[str(x) for x in details["marks"]]
        if ch==str(roll):
            print("Student found!")
            display(roll)
            c+=1
            break
        elif ch.lower()==details["name"].lower():
            l.append(roll)
        elif ch in marks:
            l.append(roll)
    if len(l)>1:
        print("Many students found!")
        for r in l:
            display(r)
            print("---------------------")
    elif len(l)==1:
        print("Student found!")
        display(l[0])
    elif c==0:
        print("Student not found!")
def update_marks(roll,new_marks):
    for roll_stored in students.keys():
        if roll==roll_stored:
            students[roll]["marks"]=new_marks
            break
def generate_report(roll,bonus=0):
    if bonus!=0:
        students[roll]["marks"][0]+=bonus
    display(roll)
def parse_text():
    f=open("File.txt","w")
    for roll,details in students.items():
        nm=details["name"]
        marks=details["marks"]
        f.write(str(roll)+" "+nm+" "+str(marks)+"\n")
    f.close()
def append_records(n):
    with open("File.txt","a") as fob:
        for i in range(n):
            marks=[]
            roll=int(input("Enter roll:"))
            nm=input("Enter name:")
            print("Enter 5 subjects marks:")
            for j in range(5):
                m=int(input())
                marks.append(m)
            fob.write(str(roll)+" "+nm+" "+str(marks)+"\n")
def read_file():
    with open("File.txt","r") as fob:
        return fob.read()
def read_line():
    with open("File.txt","r") as f:
        print("Line 1-")
        print(f.readline())
def display_word():
    with open("File.txt","r") as f:
        data=f.read()
        new_data=data.replace(" ","#")
    return new_data
def count():
    v=c=up=low=0
    with open("File.txt","r") as fob:
        data=fob.read()
        for char in data:
            if char.isalpha():
                if char in "AEIOUaeiou":
                    v+=1
                else:
                    c+=1
                if char.isupper():
                    up+=1
                else:
                    low+=1
    return "Vowels- "+str(v)+"\nConsonants- "+str(c)+"\nUppercase- "+str(up)+"\nLowercase- "+str(low)
def search_file(name):
    with open("File.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            data=line.split()
            if data[1].lower()==name.lower():
                return "Student found!"
def copy_selected(n):
    rolls=names=list();copy=[]
    ch=input("Enter N to select using names or R to select using rolls:")
    if ch.upper()=="N":
        print("Enter names:")
        for i in range(n):
            nm=input().lower()
            names.append(nm)
    elif ch.upper()=="R":
        print("Enter rolls:")
        for i in range(n):
            roll=int(input())
            rolls.append(roll)
    else:
        print("Invalid data!")
        return None
    with open("File.txt","r") as f:
        fob=open("copyfile.txt","a")
        lines=f.readlines()
        for line in lines:
            data=line.split()
            if data[0] in rolls or data[1].lower() in names:
                copy.append(line)
        fob.writelines(copy)
        fob.close()
def parse_binary():
    fob=open("filebinary.bin","wb")
    for roll,data in students.items():
        name=data["name"]
        marks=data["marks"]
        pk.dump([roll,name,marks],fob)
    fob.close()
def append_binary(n):
    f=open("filebinary.bin","ab")
    for i in range(n):
        r=int(input("Enter roll:"))
        n=input("Enter name:")
        m=list()
        print("Enter 5 subjects marks one by one:")
        for k in range(5):
            mark=int(input())
            m.append(mark)
        pk.dump([r,n,m],f)
    f.close()
def display_binary():
    print("[Roll,Name,Marks]")
    with open("filebinary.bin","rb") as f:
        while True:
            try:
                data=pk.load(f)
                print(data)
            except EOFError:
                break
def search_binary(roll):
    with open("filebinary.bin","rb") as fob:
        try:
            while True:
                data=pk.load(fob)
                if data[0]==roll:
                    print("Student found!")
                    print(data)
                    break
        except EOFError:
            print("Student not found!")
def update_bin(roll):
    f=open("filebinary.bin",'rb')
    rec=[];c=0
    while True:
        try:
            data=pk.load(f)
            if data[0]==roll:
                c+=1
                data[2][0]+=10
            rec.append(data)
        except EOFError:
            break
    f.close()
    if c==0:
        return "Student not found!"
    else:
        with open("filebinary.bin","wb") as f:
            for data in rec:
                pk.dump(data,f)
        return "Marks updated!"
def parse_csv():
    with open("filecsv.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["Roll","Name","Average","Median","Mode"])
        for roll,details in students.items():
            writer.writerow([roll,details["name"],sum(details["marks"])/5,median(details["marks"]),mode(details["marks"])])
def append_csv(n):
    f=open("filecsv.csv","a",newline="")
    w=csv.writer(f);l=[]
    for i in range(n):
        r=int(input("Enter roll:"))
        n=input("Enter name:")
        print("Enter 5 subjects marks:")
        m=[]
        for j in range(5):
            mark=int(input())
            m.append(mark)
        l.append([r,n,sum(m)/5,median(m),mode(m)])
    w.writerows(l)
    f.close()
def read_csv():
    with open("filecsv.csv","r",newline="") as f:
        reader=csv.reader(f)#You can also use list slicing by converting this iterable object into a list!
        header=next(reader)
        print(header)
        for data in reader:
            print(data)
def search_csv(roll):
    fob=open("filecsv.csv","r",newline="")
    r=list(csv.reader(fob))
    for data in r[1:]:
        if int(data[0])==roll:
            return "Student found!\n"+str(data)
    else:
        return "Student not found!"
    fob.close()
def push(roll):
    stack.append(roll)
def pop_roll():
    if stack:
        return stack.pop(-1)
    else:
        return "Stack underflow!"
def peek():
    if stack: return stack[-1]
    else: return "Stack underflow!"
def display_stack():
    if stack: print(stack)
    else:
        print("Stack underflow!")
try:
    while True: 
        print("========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1.Add or modify student\n2.Display student report\n3.Search student\n4.Parse data to text file\n5.Add records in ",end="")
        print("text file\n6.Read text file\n7.Read text file line by line\n8.Get text file data separated by #\n9.Search text file",end="")
        print("\n10.Copy selected records to another text file\n11.Parse data to binary file\n12.Display binary file data\n",end="")
        print("13.Search binary file\n14.Update Binary file\n15.Add records to binary file\n16.Parse data to CSV file\n",end="")
        print("17.Add records to CSV file\n18.Display all records from CSV file\n19.Search CSV file\n20.Push roll to stack\n",end="")
        print("21.Pop top roll from stack\n22.Peek top roll from stack\n23.Display whole stack\n24.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            marks=[]
            print("Enter 5 subjects marks:")
            for i in range(5):
                m=int(input())
                marks.append(m)
            add_modify(int(input("Enter roll:")),input("Enter name:"),marks)
        elif ch==2:
            display(int(input("Enter roll:")))
        elif ch==3:
            search()
        elif ch==4:
            parse_text()
        elif ch==5:
            append_records(int(input("Enter no.of records to be added:")))
        elif ch==6:
            print(read_file())
        elif ch==7:
            read_line()
        elif ch==8:
            print(display_word())
        elif ch==9:
            print(search_file(input("Enter student name:")))
        elif ch==10:
            copy_selected(int(input("Enter no.of records:")))
        elif ch==11:
            parse_binary()
        elif ch==12:
            display_binary()
        elif ch==13:
            search_binary(int(input("Enter roll:")))
        elif ch==14:
            print(update_bin(int(input("Enter roll:"))))
        elif ch==15:
            append_binary(int(input("Enter no.of records:")))
        elif ch==16:
            parse_csv()
        elif ch==17:
            append_csv(int(input("Enter no.of records:")))
        elif ch==18:
            read_csv()
        elif ch==19:
            print(search_csv(int(input("Enter roll:"))))
        elif ch==20:
            push(int(input("Enter roll:")))
        elif ch==21:
            print(pop_roll())
        elif ch==22:
            print(peek())
        elif ch==23:
            display_stack()
        elif ch==24:
            with open("filebinary1.bin","wb") as f:
                pk.dump(students,f)
            with open("extra.txt",mode="w") as fob:
                fob.write(str(stack))
            break
        else:
            print("Invalid input!")
except Exception as e:
    print("Error occured!")
    print(e)
else:
    print("Operation done without errors. You can exit terminal!")
finally:
    print("Click run button if you want to execute the backend again. Bye!")