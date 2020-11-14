
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def uniquenum(arr):
    missing=0
    itot=0
    etot=0
    if arr==None:
        return None
    elif len(arr)<1:
        return None
    else:
        for ind,ele in enumerate(arr):
            itot=itot^ind+1
            etot=etot^ele
            #print(itot,etot )
        missing=etot    
    return missing

arr=[2,2,3]
#print(9^0)
result=uniquenum(arr)
print(result)


o/p
-------
3
