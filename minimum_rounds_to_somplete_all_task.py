class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = 0
        hash_map = {}

        for i in tasks:
            try:
                hash_map[i] += 1
            except KeyError:
                hash_map[i] = 1

        for task in hash_map.keys():
            if hash_map[task] < 2:
                return -1
            count += (hash_map[task])//3 + int(hash_map[task]%3 > 0)
        return count