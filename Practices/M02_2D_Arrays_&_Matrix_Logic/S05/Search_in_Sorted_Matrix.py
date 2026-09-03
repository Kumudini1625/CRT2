from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for row in matrix:
            arr+=row
        n=len(arr)
        left,right=0,n+1
        while left<=right:
            mid=(left+right)//2
            if target==arr[mid]:
                return True
            elif target<arr[mid]:
                right=mid-1
            else:
                left=mid+1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))




from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        r,c=0,n-1
        while r<m and c>=0:
            if target==matrix[r][c]:
                return True
            elif target<matrix[r][c]:
                c-=1
            else:
                r+=1
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]] 
target = 5 
print(searchMatrix(matrix,target))      

