"""
Precise Time Complexity: O(2^(m + n)), 
where m and n are the lengths of text1 and text2, respectively.

Rounded Time Complexity: O(2^n), 
where n is the length of the longer string between text1 and text2.

Space Complexity: O(N*M) + O(N+M)

Reason: We are using an auxiliary recursion stack space(O(N+M)) and a 2D array ( O(N*M)).
"""


class Solution:
    def solve(self, s1, s2, ind1, ind2):
        if ind1 < 0 or ind2 < 0:
            return 0
        if s1[ind1] == s2[ind2]:
            return 1 + self.solve(s1, s2, ind1 - 1, ind2 - 1)
        else:
            p1 = self.solve(s1, s2, ind1 - 1, ind2)
            p2 = self.solve(s1, s2, ind1, ind2 - 1)
            return max(p1, p2)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1, text2, len(text1) - 1, len(text2) - 1)
