
import random

def doublelinked_list():
    ca={}
    first=None
    last=None
    
    for i in range(1,10):
        ele=random.randint(1,5)
        #print(ele)
        if len(ca)<1:
            first=ele
            last=ele
            ca[ele]={'prev':None,'next':None}
        else:
            if ele in ca:
                if ca[ele]['prev']==None:
                    continue
                else:
                    prev_ele=ca[ele]['prev']
                    next_ele=ca[ele]['next']
                    ca[prev_ele]['next']=ca[ele]['next']
                    last=prev_ele

                    if next_ele!=None:
                        ca[next_ele]['prev']=ca[ele]['prev']
                        last=ca[ele]['next']
                    
                    ca[ele]['prev']=None
                    ca[ele]['next']=first
                    ca[first]['prev']=ele
                    first=ele
            else:
                ca[ele]={'prev':None,'next':first}
                ca[first]['prev']=ele
                first=ele
        print(ca)
        print('ele :',ele,',first :',first,'last :',last)

                
doublelinked_list()           
                
