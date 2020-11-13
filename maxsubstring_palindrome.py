
def ispalindrom(str,max_palind_substr):
    #print('ispalindrom str',str)
    if len(str)%2==0:
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
    return status,max_palind_substr         
                
        
    
def substrpalindrom(arr):
    allsubstrings=[]
    max_palind_substr=''
    for i in range(len(arr)):
        j=i
        while j < len(arr):
            #print("i:j",i,j)
            allsubstrings.append(arr[i:j+1])
            j+=1
    
    for ele in allsubstrings:
        #slntype=str_ln_type(ele)
        #print("ele,slntype",ele,slntype)
        #print(ele,len(ele),len(ele)/2,int(len(ele)/2))
        #print(len(ele))
        if len(ele) == 1:
            status=True
        else:    
            status,max_palind_substr=ispalindrom(ele,max_palind_substr)
        #print(ele,status)    
            
        
    return max_palind_substr

a=[1,2,3]
str="aacabdkacaa"
#print(len(a))
max_palind_substr=substrpalindrom(str)
print(max_palind_substr)

input : aacabdkacaa

o/p
----
aca
