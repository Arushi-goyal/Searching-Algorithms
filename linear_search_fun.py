def linear(arry,key,lenght):
    for i in range(lenght):
        if arry[i]==key:
            print("%d found at position %d" %(key,i+1))
            return -1
    print("not found")
    return -1
lst=[]
lst=[]
size=int(input("Enter the size:"))
for j in range(size):
    numbers=int(input("Enter value:\t"))
    lst.append(numbers)
x=int(input("Enter number to search:"))
linear(lst,x,size)
