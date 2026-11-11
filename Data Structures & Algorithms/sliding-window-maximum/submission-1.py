from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        dq = deque()

        for index,num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(index)
            if dq[0] <= index - k:
                dq.popleft()
            if index >= k-1:
                res.append(nums[dq[0]])
        return res

