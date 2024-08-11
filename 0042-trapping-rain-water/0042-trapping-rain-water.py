class Solution:
    def trap(self, height: List[int]) -> int:
        # lh = [0] * len(height)
        # rh = [0] * len(height)
        # for i in range(len(height)):
        #     if i > 0:
        #         lh[i]  = max(lh[i-1], height[i-1])
        

        # for i in range(len(height) -2, -1, -1):
        #     rh[i] = max(rh[i+1], height[i+1] )
        
        # res = 0
        # for i in range(len(height)):
        #     if min(lh[i], rh[i]) - height[i] > 0:
        #         res += min(lh[i], rh[i]) - height[i]
        # return res

        if not height:
            return 0
        maxL, maxR, l, r, res = height[0], height[-1], 0, len(height)-1, 0
        while l<r:
            if maxL < maxR:
                l+=1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res+= maxR-height[r]
        return res

                

        