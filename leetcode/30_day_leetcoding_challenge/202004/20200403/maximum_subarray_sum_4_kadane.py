"""
Title:  Maximum Subarray Sum


Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Kadane's algorithm
Time:  O(N)
Space:  O(1)
"""

from typing import List
import math


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = -math.inf

        subarray = [0 for i in range(len(nums))]

        subarray[0] = nums[0]
        max_subarray_sum = max(subarray[0], max_subarray_sum)

        for i in range(1, len(nums)):
            subarray[i] = max(nums[i], subarray[i - 1] + nums[i])
            max_subarray_sum = max(subarray[i], max_subarray_sum)

        print("\n subarray: ", subarray)

        return max_subarray_sum


if __name__ == "__main__":
    #nums = [-2]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #nums = [-2, 1, -3, 44]
    #nums = [1, 2, 3, 4, 5]
    #nums = [-1, -2]
    print("\n nums: ", nums)

    solution = Solution()
    max_subarray_sum = solution.maxSubArray(nums)
    print("\n max_subarray_sum: ", max_subarray_sum)
