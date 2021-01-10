from collections import Counter


class Solution:
    def solve(self, animals, dinosaurs):
        counter = Counter(animals)
        count = 0
        for char in dinosaurs:
            get = counter.get(char)
            if get:
                count += get
                del counter[char]

        return count


s = Solution()
animals = 'a'
dinosaurs = 'aa'
result = s.solve(animals, dinosaurs)
print(result)
