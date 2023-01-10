class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].isupper():
            answer = True
            if word[1].isupper():
                for letter in word[2:]:
                    answer &= letter.isupper()
            else:
                for letter in word[2:]:
                    answer &= letter.islower()
            return answer

        else:
            for letter in word[1:]:
                if letter.isupper():
                    return False

        return True

        #also
        return word[1:].lower() == word[1:] or word.lower() == word or word.upper() == word