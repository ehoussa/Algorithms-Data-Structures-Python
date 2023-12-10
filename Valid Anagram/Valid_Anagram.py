class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = ''.join(sorted(s))
        str2 = ''.join(sorted(t))
        if str2 != str1:
            return False
        return True
