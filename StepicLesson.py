a=[17,24,91,96,67,-27]
n = len(a)
for i in range(n-1):
    for j  in  range(n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)git initgit# S t e p i c L e s s o n . p y  
 