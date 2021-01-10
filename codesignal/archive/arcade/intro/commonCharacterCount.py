# Common character count

def commonCharacterCount(s1, s2):
    count = 0
    hash_set = set()
    for i in range(len(s1)):
        for j in range(len(s2)):
            if (s1[i] == s2[j]) and (j not in hash_set):
                hash_set.add(j)
                count += 1
                break

    return count


# keeping_it_leal's solution(229)
def commonCharacterCount1(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "adcaa"

    print(commonCharacterCount(s1, s2))