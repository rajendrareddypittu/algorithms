Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 
 def duplicatenum(arr):
    import heapq
    if arr==None:
        return None
    elif len(arr)<1:
        return None
    else:
        print(arr)
        ln=len(arr)-1
        heapq.heapify(arr)
        print(arr)
        prev_ele=heapq.heappop(arr)
        for ind in range(ln):
            cur_ele=heapq.heappop(arr)
            print(prev_ele,cur_ele)
            if prev_ele-cur_ele==0:
                return cur_ele
            else:
                prev_ele=cur_ele
                continue
        return None    

arr=[7,4,9,1,7]
result=duplicatenum(arr)
print(result)
    
        
        
        o/p
        ----------
        [7, 4, 9, 1, 7]
[1, 4, 9, 7, 7]
1 4
4 7
7 7
---> 7
> 
