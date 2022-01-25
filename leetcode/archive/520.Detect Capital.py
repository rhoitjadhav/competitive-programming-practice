class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result1 = self.all_caps(word)
        result2 = self.all_small(word)
        result3 = self.first_caps(word)

        return any([result1, result2, result3])

    def all_caps(self, word: str):
        for c in word:
            if c.islower():
                return False

        return True

    def all_small(self, word: str):
        for c in word:
            if c.isupper():
                return False

        return True

    def first_caps(self, word: str):
        if word[0].islower():
            return False

        for c in word[1:]:
            if c.isupper():
                return False

        return True
