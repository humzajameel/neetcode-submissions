class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        in_memory = {}
        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str in in_memory:
                in_memory[sorted_str].append(word)
            else:
                in_memory[sorted_str] = [word]
        return list(in_memory.values())
        