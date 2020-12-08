"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""


def two_sum(nums, target):
    # Slow Solution O(n^2)
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         num1 = nums[i]
    #         num2 = nums[j]
    #         if num1 + num2 == target:
    #             return [i, j]
    # return None

    # Fast Solution O(N)
    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i

    for i in range(len(nums)):
        current_num = nums[i]
        complement = target - current_num
        if complement in num_dict and i != num_dict[complement]:
            return [i, num_dict[complement]]


print(two_sum(nums=[2, 5, 9, 13], target=7))
print(two_sum(nums=[4, 3, 5], target=8))

# Your code here
# Input =  list of number and a integer
# Output = indices of a list that add up to the target return None if no answer.

# Plan

# Start with one of the pointers aat arr[0] and another one at arr[1] see
# if they add up to the target and increment until they do
