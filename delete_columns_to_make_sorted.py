class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        len_rows = len(strs)
        len_cols = len(strs[0])

        count = 0
        for c in range(len_cols):
            for r in range(len_rows-1):
                if strs[r][c] > strs[r+1][c]:
                    count += 1
                    break
        return count