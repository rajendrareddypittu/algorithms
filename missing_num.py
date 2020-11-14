Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



def missingnum(arr):
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
            print(itot,etot )
        missing=itot^etot    
    return missing

arr=[2,0,3]
#print(9^0)
result=missingnum(arr)
print(result)


o/p
---
1
> 
