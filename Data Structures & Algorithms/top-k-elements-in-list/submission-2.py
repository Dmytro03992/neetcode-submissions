class Solution:
    
    def topKFrequent(self, nums: List[int], k: int):
        count = {}
        bucket = [[] for size in range(len(nums)+1) ]
        output = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, cnt in count.items():
            bucket[cnt].append(key)

        for n in range(len(bucket) - 1, 0, -1):
            for el in bucket[n]:
                output.append(el)
                if len(output) == k:
                    return output