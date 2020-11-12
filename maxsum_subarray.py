def maxele(ele1,ele2):
    mele=max([ele1,ele2])
    return mele
def maxsumsubset(arr):
    max=-999999999999999999
    nmax=-99999999999999999999
    sum1=0
    maxsum=0
    for ele in arr:
        #print('ele',ele)
        sum1=sum1+ele
        nmax=maxele(nmax,ele)
        if sum1<0:
            sum1=0
        if sum1 >= 0:
            maxsum=maxele(sum1,maxsum)
    if sum1==0:
        return nmax
    else:
        return maxsum

a=[-1,-9,-2,-3,-1,-4]  
msum=maxsumsubset(a)
print(msum)
 
 o/p
 ----
 -1
 
