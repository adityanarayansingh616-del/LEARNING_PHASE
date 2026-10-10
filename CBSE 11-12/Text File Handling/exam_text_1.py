#To count no.of digits in each word present in the text file data and return in tuple type!
with open("File.txt","w") as f:
    f.write("Room 112 has 5 fans and 20 lights")
def DisplayWords():
    t=()
    with open("File.txt","r") as f:
        data=f.read()
        words=data.split()
        for word in words:
            c=0
            for char in word:
                if char.isdigit():
                    c+=1
            t+=(c,)
    return t
print(DisplayWords())