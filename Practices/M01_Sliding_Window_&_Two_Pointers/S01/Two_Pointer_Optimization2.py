'''#26. Remove Duplicates from Sorted Array
from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    i=0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))



#Remove elements
def removeElement(nums: List[int], val: int) -> int:
    i=0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums))
     


from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        while left<right:
            s=numbers[left]+numbers[right]
            if s==target:
                return [left+1,right+1]
            elif s>target:
                right-=1
            else:
                left+=1
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))
'''
from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
        res=[ele**2 for ele in nums]
        res.sort()
        return res
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

                