#brute force
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxV = 0
        for i in range(0,n):
           curr:int = 0
           for j in range(i,n):
                curr = curr + nums[j]
                maxV = max(maxV,curr)    
        return maxV

  # optimal

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxV = nums[0]
        curr = nums[0]
        for i in range(1,n):
           curr = max(curr + nums[i],nums[i])
           maxV = max(maxV,curr)
        return maxV
           
