class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        A,B = nums1,nums2
        total = len(nums1)+ len(nums2)
        half = total//2


        if len(B) < len(A):
            A,B = B,A
        
        left = 0
        right = len(A) - 1

        while True:

            i = (left+right)//2
            j = half - i - 2

            leftACut = A[i] if i>= 0 else float("-infinity")
            rightACut = A[i+1] if (i+1) < len(A) else float("infinity")
            leftBCut = B[j] if j>= 0 else float("-infinity")
            rightBCut = B[j+1] if (j+1) < len(B) else float("infinity") 

            #if partition is correct
            if leftACut <=rightBCut and leftBCut <= rightACut:
                #check if odd
                if total %2:
                    return min(rightACut,rightBCut)
                #even
                return ( max(leftACut,leftBCut) + min(rightACut,rightBCut)) / 2
            elif leftACut > rightBCut:
                right = i-1
            else:
                left = i+1
