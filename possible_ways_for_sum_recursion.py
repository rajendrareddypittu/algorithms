def target_sum(index,options,targetsum,way):
    if targetsum==0:
        print("way :",list(way))
        return 1
    elif index >=len(options):
        #print("ind> lenop , index :",index)
        return 0
    elif targetsum <0:
        #print("targetsum:",targetsum)
        return 0

    else:
        
        target_sum(index+1,options,targetsum,way)
        #print("index ,way :",index,list(way))
        target_sum(index+1,options,targetsum-int(options[index]),way+str(options[index]))
        
        
    return 0

target_sum(0,[1,2,3],0,'')    
