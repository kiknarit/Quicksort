def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        
        return sort(less)+equal+sort(greater)  
   
    else:  
        return array



array=[12,21,71,4,2,1]
ans = sort(array)

print "INPUT  = [",
for i in range(len(array)):
    print array[i],
    if i < len(array)-1 :
        print " ",
print "]"
print "OUTPUT = [",
for i in range(len(ans)):
    print ans[i],
    if i < len(ans)-1 :
        print " ",
print "]"
