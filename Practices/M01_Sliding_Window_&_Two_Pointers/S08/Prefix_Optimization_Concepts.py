'''from typing import List

def runningSum(nums: List[int]) -> List[int]:
    
    res=[0]*(len(nums))
    for i in range(len(nums)):
        curr_sum=0
        for j in range(i+1):
            curr_sum += nums[j]
        res[i]=curr_sum
    return res
nums = [1,2,3,4]
print(runningSum(nums))


from typing import List
def largestAltitude(gain: List[int]) -> int:
        n=len(gain)
        alt=[0]*(n+1)
        for i in range(1,n+1):
            alt[i]=alt[i-1]+gain[i-1]
        return max(alt)
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

curr_alt=0
max_alt=0
for g in gain:
    curr_alt+=g
    max_alt=max(curr_alt,max_alt)
return max_alt
'''

from typing import List


def findMiddleIndex(nums: List[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            right_sum=total-nums[i]-left_sum
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))        

    
