class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1

        while l<r:
            temp = (r-l) * min(height[l], height[r])
            res = max(temp, res)
            
            #conditionalyy updating pointer, goal is to maximise the result
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
        return res

        