#To implement a stack using list and then perform operations according to user choice based on MENU!
stack=[]
Max=5
while True:
    print("\t\t\tMENU")
    print("1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT")
    ch=int(input("Enter choice:"))
    if ch==1:
        if len(stack)==Max:
            print("Stack overflow!")
        else:
            item=input("Enter item to push:")
            stack.append(item)
    elif ch==2:
        if not stack:
            print("Stack underflow!")
        else:
            print("Deleted:",stack.pop())
    elif ch==3:
        if len(stack)==0:
            print("Stack empty!")
        else:
            print(stack)
    elif ch==4:
        break
    else:
        print("Invalid input!")