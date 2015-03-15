a = [1,2,3,4,5,6,7,8,9]
import itertools

for i in range (0,len(a)):
    b = itertools.islice(a, i+1, 10)
    print str(a[i]) + ' : ', 
    for c in b:
        print c,
    
    print


b = {'a':1}



b.setdefault('c', set()).add(3)
b.setdefault('c', set()).add(4)
b.setdefault('c', set()).add(5)

print b



    