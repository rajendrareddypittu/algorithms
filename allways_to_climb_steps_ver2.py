class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
counter=0
paths=[]
def allways(totsteps,jumps,remsteps,ind,path):
    global counter
    global paths
    if totsteps<1:
        #print("totsteps<1:")
        return
    elif remsteps<0:
        #print("remsteps<0:")
        return
    elif ind>=len(jumps):
        #print("ind>=len(jumps)")
        return
    elif (remsteps==0):
        counter+=1
        #print(counter)
        paths.append(path)
        return 1

     
    else:
        #print("allways1")
        for ind in range(len(jumps)):
            allways(totsteps,jumps,remsteps-int(jumps[ind]),0,path+str(jumps[ind]))
        
    
    #print(counter)
    
totsteps=3
jumps=[1,2,3]
allways(totsteps,jumps,totsteps,0,'')
print(counter)
print("************** Ways *********** ")
for ele in list(paths):
    print(list(ele))
print("************** Ways *********** ")

    
