class Queue:
    def __init__(self):
        self.item=[]
    def push(self,val):
        self.item.append(val)
    def pop(self):
        val=self.item.pop(0)
        return val
def findWay(matrix):
    mx=matrix
    x=len(mx) #rows
    y=len(mx[0]) #columns
    print(x,y)
    queue=Queue()
    queue.push((0,0))
    while len(queue.item)>0:
        top=queue.pop()
        if top==(x-1,y-1):
            return True
        new_qd1=(top[0]+1,top[1]) if top[0]+1 <x and mx[top[0]+1][top[1]]>-1 else None
        print((top[0]+1,top[1]),new_qd1)
        new_qd2=(top[0],top[1]+1) if top[1]+1 <y and mx[top[0]][top[1]+1]>-1 else None
        print((top[0],top[1]+1),new_qd2)
        if new_qd1 is not None:
            queue.push(new_qd1)
        if new_qd2 is not None:
            queue.push(new_qd2)
    return False        
        #new_qd2=()
        #if mx[]    
        

            
            
            


arr = [[ 0, 0, 0, -1, 0 ],
       [-1, 0, 0, -1, -1],
       [-1, 0, 0, 0, -1],
       [ 0, 0, -1, 0, 0 ]]
print(findWay(arr) )
    
