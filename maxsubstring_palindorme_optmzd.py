
def ispalindrom(str1,max_palind_substr,actual_str,substrind,max_start,max_end):
    #print('ispalindrom str',str)
    str=actual_str[substrind[0]:substrind[1]+1]
    if (int(substrind[0])>=max_start and int(substrind[1]) <= max_end):
        #start
        mid_pos1=max_start
        mid_pos2=max_end
    
    elif len(str)%2==0:
        mid_pos1=int(len(str)/2)-1
    else:
        mid_pos1=int(len(str)/2)
    mid_pos2=int(len(str)/2)
    #print("mid_pos1,mid_pos2",len(str),mid_pos1,mid_pos2)
    status=False
    if str[mid_pos1]==str[mid_pos2]:
        start=mid_pos1
        end=mid_pos2
        while start>=0 and end <=len(str)-1:
            if str[start]==str[end]:
                status=True
            else:
                status=False
                break
            start=start-1
            end=end+1
    else:
        status=False
    if (status):
        if len(str)>len(max_palind_substr):
            max_palind_substr=str
            max_start=substrind[0]
            max_end=substrind[1]
    return status,max_palind_substr ,max_start ,max_end     
                
        
    
def substrpalindrom(arr):
    allsubstrings=[]
    substrind=[[]]
    if len(arr)>0:
        max_palind_substr=arr[0]
        
    
    max_start=0
    max_end=0
    for i in range(len(arr)):
        j=i
        while j < len(arr):
            #print("i:j",i,j)
            allsubstrings.append(arr[i:j+1])
            substrind.append(list([i,j]))
            
            j+=1
    #print(substrind)
    for ind,ele in enumerate(allsubstrings):
        #slntype=str_ln_type(ele)
        #print("ele,slntype",ele,slntype)
        #print(ele,len(ele),len(ele)/2,int(len(ele)/2))
        #print(len(ele))
        if len(ele) == 1:
            status=True
            
        else:    
            if len(ele)>len(max_palind_substr)  :
                status,max_palind_substr,max_start,max_end=ispalindrom(ele,max_palind_substr,arr,substrind[ind+1],max_start,max_end)
        #print(ele,status)    
            
        
    return max_palind_substr

a=[1,2,3]
str="cbba"
#print(len(a))
max_palind_substr=substrpalindrom(str)
print(max_palind_substr)
