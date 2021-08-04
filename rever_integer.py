#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


class Solution:
    def reverse(self, x: int) -> int:
        rev_int=0
        print(pow(2,31))
        if x <pow(-2,31) or x>pow(2,31)-1:
            return 0
        newx=abs(x)
        print(newx)
        while newx>0:
            remaider=newx%10
            newx=newx//10
            rev_int=rev_int*10+remaider
        if rev_int <pow(-2,31) or rev_int>pow(2,31)-1:
            return 0
        if x<0:
            rev_int=0-rev_int
            
        return rev_int    
            

