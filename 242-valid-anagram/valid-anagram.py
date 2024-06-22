class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = list(s)
        for i in range(0, len(t)):
            if t[i] in a:
                a.remove(t[i])
            else:
                return False
        return True