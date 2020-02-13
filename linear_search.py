list=list(map(int, input("Enter the value to store in list 'with gap':").split()))
n=int(input("Enter the value which you want to search:"))
print(list)
a=len(list)
found=0
for i in range(0,a):
    if list[i]==n:
        found=1
        print("%d found at position %d" %(n,i+1))
        break
if not found:
    print("not found")

    
        

