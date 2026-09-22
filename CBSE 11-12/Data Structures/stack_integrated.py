#To push integers into a stack and then continuosly pop until it becomes empty!
n=int(input("Enter no.of integers to be pushed into the stack:"))
stack=list()
x=[]
for i in range(n):
    INT=int(input("Enter integer:"))
    x.append(INT)
stack.extend(x)#In exam do not use extend() for stacks and use one by one push(append())
print(stack)
while stack:
    print("Deleting:",stack.pop())
    if stack:
       print(stack)
print("Stack empty!")