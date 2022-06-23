a = [1,7,3,6,5,6]
for i, x in enumerate(a):
    print(a[:i], a[i+1:], i, x)
    
a.sort()
print(a)