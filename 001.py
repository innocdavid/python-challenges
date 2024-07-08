"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Follow-up: 
    Can you come up with an algorithm that is less than O(n2) time complexity
"""


# def twoSums(nums, target):
#     for ind1 in range(len(nums)):
#         for ind2 in range(ind1+1, len(nums)):
#             if nums[ind1] + nums[ind2] == target:
#                 return [ind1, ind2]
#     return None


def twoSums(nums, target):
    seen = {}
    for ind in range(len(nums)):
        num = nums[ind]
        if target - num in seen:
            return [ind, seen[target - num]]
        seen[num] = ind


nums = [2, 7, 11, 15]
target = 13

result = twoSums(nums, target)

if (result):
    print(result[0], result[1])
else:
    print('Target not found')
