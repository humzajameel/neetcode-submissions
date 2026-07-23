from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        in_memory = defaultdict(list)
        print(in_memory)
        for word in strs:
            sorted_str = "".join(sorted(word))
            in_memory[sorted_str].append(word)
        return list(in_memory.values())       