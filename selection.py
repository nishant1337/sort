a=[10,15,4,23,0]
n=len(a)
for i in range (n):
    min=i 
    for j in range(i+1,n):
        if a[min]>a[j]:
            min=j
    a[min],a[i]=a[i],a[min]
    print("iter",i+1,a)
print("sorted",a)    
