class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        front=0
        zeros=0
        back=0
        max_count=0
        while front<n:
            if nums[front]==0:
                zeros+=1
                while zeros>k:
                    if nums[back]==0:
                        zeros-=1
                    back+=1            
                max_count=max(max_count,front-back+1)
                front+=1
            else:           
                max_count=max(max_count,front-back+1)
                front+=1       
        return max_count

                
