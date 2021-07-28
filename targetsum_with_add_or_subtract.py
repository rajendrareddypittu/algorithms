#given set of array with integers , find ways to get target sum 
#by perfoming either addition subtraction of elements
way=0
def ways_for_target_sum(elements,target_sum,current_sum,path):
    global way
    print(current_sum,path)
    if target_sum==current_sum:
        way+=1
        print("Found way ",path)
        
        #print(current_sum)
        #return 1
    #elif current_sum >target_sum:
    #    return 0
    if len(elements)<1:
        return 0
    if 1==1:
        for ind in range(len(elements)):
            ele=elements[ind]
            
            ways_for_target_sum(elements[ind+1:],target_sum,current_sum-int(ele),path+',-'+str(ele))
            ways_for_target_sum(elements[ind+1:],target_sum,current_sum+int(ele),path+',+'+str(ele)) 
    return way        
#res=ways_for_target_sum([-3, 1, 3, 5],6,0,'')
#print("ways:",res)
res=ways_for_target_sum([2, 3, -4, 4],5,0,'')
print("ways:",res)
