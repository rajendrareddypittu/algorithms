Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=missing_min_positive(nums)
        return res
        
def missing_min_positive(arr):
    if arr==None:
        return None
    if len(arr)<1:
        return 1
    else:
        missing_num=1
        for i in range(1,len(arr)+1):
           # print(i)
            if i in arr:
               # print("yes")
                missing_num+=1
                continue
            else:
                break
        return missing_num

arr=[1,2,3,4]
result=missing_min_positive(arr)
print(result)

o/p:
---
5
        
