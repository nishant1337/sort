a=[15,1,5,3,0]
n=len(a)
for i in range (1,n):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
    
print("Sorted",a)
    