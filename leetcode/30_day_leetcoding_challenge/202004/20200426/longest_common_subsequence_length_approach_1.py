"""
Title:  Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some
characters(can be none) deleted without changing the relative order of the remaining
characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common
subsequence of two strings is a subsequence that is common to both strings.


If there is no common subsequence, return 0.


Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.


Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.


Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:
1) 1 <= text1.length <= 1000
2) 1 <= text2.length <= 1000
3) The input strings consist of lowercase English characters only.
"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return helper(text1, text2, 0, 0)


def helper(text1: str, text2: str, i: int, j: int) -> int:
    if i == len(text1) or j == len(text2):
        return 0
    if text1[i] == text2[j]:
        return 1 + helper(text1, text2, i + 1, j + 1)
    c1 = helper(text1, text2, i, j + 1)
    c2 = helper(text1, text2, i + 1, j)
    return max(c1, c2)


def get_test_case_1() -> (str, str):
    return None, None


def get_test_case_2() -> (str, str):
    return None, ""


def get_test_case_3() -> (str, str):
    return "", ""


def get_test_case_4() -> (str, str):
    return "a", ""


def get_test_case_5() -> (str, str):
    return "", "a"


def get_test_case_6() -> (str, str):
    return "a", "a"


def get_test_case_7() -> (str, str):
    return "a", "b"


def get_test_case_8() -> (str, str):
    text1 = "abcde"
    text2 = "ace"
    return text1, text2


def get_test_case_9() -> (str, str):
    text1 = "abc"
    text2 = "abc"
    return text1, text2


def get_test_case_10() -> (str, str):
    text1 = "abc"
    text2 = "def"
    return text1, text2


if __name__ == "__main__":
    solution = Solution()

    #text1, text2 = get_test_case_1()
    #text1, text2 = get_test_case_2()
    #text1, text2 = get_test_case_3()
    #text1, text2 = get_test_case_4()
    #text1, text2 = get_test_case_5()
    #text1, text2 = get_test_case_6()
    #text1, text2 = get_test_case_7()
    text1, text2 = get_test_case_8()
    #text1, text2 = get_test_case_9()
    #text1, text2 = get_test_case_10()
    print("\n text1: ", text1)
    print(" text2: ", text2)

    result = solution.longestCommonSubsequence(text1, text2)
    print("\n result: ", result)
