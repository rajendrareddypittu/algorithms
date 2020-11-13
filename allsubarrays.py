def allsubarray(arr):
    allsubarrays=[]
    for i in range(len(arr)):
        j=i
        while j < len(arr):
            #print("i:j",i,j)
            allsubarrays.append(arr[i:j+1])
            j+=1
    return allsubarrays
    
a=[1,2,3]
#print(len(a))
asa=allsubarray(a)
print(asa)    

o/p
--------
[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
