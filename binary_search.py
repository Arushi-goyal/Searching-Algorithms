def binary(sort_list,lenght,key):
    start=0
    end=lenght-1
    while start<=end:
        mid=(start+end)//2
        if key==sort_list[mid]:
            print("Entered number %d is present at position: %d" %(key,mid+1))
            return -1
        elif key<sort_list[mid]:
            end=mid-1
        elif key>sort_list[mid]:
            start=mid+1
    print("Element not found!")
    return -1
lst=[]
size=int(input("Enter the size:"))
for j in range(size):
    numbers=int(input("Enter value:\t"))
    lst.append(numbers)
lst.sort()
print("\nThe list will be sorted is:",lst)
x=int(input("Enter the number to search: "))
binary(lst,size,x)

        


