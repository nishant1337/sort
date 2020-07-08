a=[10,15,4,23,0]
n=len(a)
for i in range (n-1):
    for j in range (n-i-1):
        if a[j+1]<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
    print("iter",i+1,a)   
print("sorted",a)     
      