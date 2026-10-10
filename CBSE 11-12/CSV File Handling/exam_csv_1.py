#To add data manually into csv file and then create 2 functions to add record and display names under 'Work' category!
import csv
def AddRec():
    with open("filecsv.csv","a",newline='') as f:
        name=input("Enter name:")
        phn=int(input("Enter phone number:"))
        cat=input("Enter Category:")
        writer=csv.writer(f)
        writer.writerow([name,phn,cat])
def DisplayWork():
    with open("filecsv.csv","r",newline='') as f:
        reader=csv.reader(f)
        c=0
        next(reader)
        for data in reader:
            if data[2].lower()=="work":
                print(data[0])
                c+=1
        return c
AddRec()
print(DisplayWork())