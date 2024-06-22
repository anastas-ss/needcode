from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

        box = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            box[sorted_word].append(word)
        return list(box.values())