def allsubsets(seta,pos,len,subsets):
    if pos==len:
        print(set(subsets))
        return 1
    if pos<len:
        allsubsets(seta,pos+1,len,subsets)
        allsubsets(seta,pos+1,len,subsets+str(seta[pos]))

    #print(subsets)
a=[1,2,3]
allsubsets(a,0,3,'')

output
---------
set()
{'3'}
{'2'}
{'2', '3'}
{'1'}
{'1', '3'}
{'1', '2'}
{'1', '2', '3'}
    
