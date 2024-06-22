from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        box = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            box[sorted_word].append(word)
        return list(box.values())