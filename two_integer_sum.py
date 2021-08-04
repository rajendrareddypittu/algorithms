#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtbl={}
        for ind,ele in enumerate(nums):
            if target-ele in hashtbl.keys():
                return list((hashtbl[target-ele],ind))
            else:
                hashtbl[ele]=ind
                

                
            
