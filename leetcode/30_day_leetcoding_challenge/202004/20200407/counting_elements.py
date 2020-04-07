"""
Title:  Counting Elements

Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them separately.


Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.


Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.


Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.


Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.


Constraints:
1 <= arr.length <= 1000
0 <= arr[i] <= 1000


Time:  O(N)
Space:  O(1)
"""

from typing import List


class Solution:

    def countElements(self, arr: List[int]) -> int:
        count_of_elements = 0

        if 1 <= len(arr) <= 1000:
            for element in arr:
                if 0 <= element <= 1000 and element + 1 in arr:
                    count_of_elements += 1
        return count_of_elements


if __name__ == "__main__":
    solution = Solution()
    #arr = [1, 2, 3]
    #arr = [1, 1, 3, 3, 5, 5, 7, 7]
    #arr = [1, 3, 2, 3, 5, 0]
    arr = [1, 1, 2, 2]
    print("\n arr: ", arr)

    count_of_elements = solution.countElements(arr)
    print("\n count_of_elements: ", count_of_elements)

