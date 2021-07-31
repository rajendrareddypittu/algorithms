class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #print("start")
        def swapelements(array,i,n):
            while i<n:
                temp_ele=array[i]
                array[i]=array[n]
                array[n]=temp_ele
                i+=1
                n-=1
        k=k%len(nums)
        if k<1:
            return
        elif len(nums)>2:
            swapelements(nums,0,len(nums)-1)
            swapelements(nums,0,k-1)
            swapelements(nums,k,len(nums)-1)
        elif len(nums)==2:
            swapelements(nums,0,1)
        
