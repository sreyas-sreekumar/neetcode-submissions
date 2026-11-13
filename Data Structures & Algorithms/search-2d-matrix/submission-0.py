class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix) , len(matrix[0]) #length of rows for m and n = num of columns

        low , high = 0, m*n - 1 # low is 0 , high = num of rows x columns -1

        while low<= high:
            mid = (low+high) //2

            #convert mid index to the actual value
            value = matrix[mid//n][mid%n] #mid//n finds the row,mid%n finds the column
            if value == target:
                return True
            if value < target:
                low = mid +1
            else:
                high = mid -1
        return False