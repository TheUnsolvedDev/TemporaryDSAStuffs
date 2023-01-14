class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_pattern = {}
        hash_s = {}
        word_pattern = ''
        word_s = ''

        count = 0
        for i in pattern:
            try:
                if hash_pattern[i]:
                    pass
            except KeyError:
                hash_pattern[i] = count
                count += 1

        count = 0
        for i in s.split(' '):
            try:
                if hash_s[i]:
                    pass
            except KeyError:
                hash_s[i] = count
                count += 1

        for i in s.split(' '):
            word_s += str(hash_s[i])

        for i in pattern:
            word_pattern += str(hash_pattern[i])

        return word_s == word_pattern
        
