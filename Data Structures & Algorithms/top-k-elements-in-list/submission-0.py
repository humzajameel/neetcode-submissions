class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        print(res)
        for num in nums:
            dic[num] = dic.get(num, 0) +1
            if num in res:
                continue
            if len(res) < k:
                res.append(num)
            else:
                min_elem = min(res, key=lambda x: dic[x])
                if dic[min_elem] < dic[num]:
                    res.remove(min_elem)
                    res.append(num)
        return res
        