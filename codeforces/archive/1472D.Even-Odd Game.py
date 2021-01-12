class Solution:
    def solve(self, arr):

        alice = sorted([a for a in arr if a % 2 == 0], reverse=True)
        bob = sorted([a for a in arr if a % 2 != 0], reverse=True)
        alice_n = len(alice)
        bob_n = len(bob)
        alice_sum = 0
        bob_sum = 0
        turn = 0

        i = 0
        j = 0
        while True:
            if i == alice_n and j == bob_n:
                break
            
            if i == alice_n:
                num = bob[j]
                j += 1

            elif j == bob_n:
                num = alice[i]
                i += 1

            else:
                if alice[i] > bob[j]:
                    num = alice[i]
                    i += 1
                elif bob[j] > alice[i]:
                    num = bob[j]
                    j += 1
                else:
                    num = alice[i]

            if turn == 0:
                if num % 2 == 0:
                    alice_sum += num
                turn = 1

            else:
                if num % 2 != 0:
                    bob_sum += num
                turn = 0

        if alice_sum > bob_sum:
            return 'Alice'
        elif bob_sum > alice_sum:
            return 'Bob'
        else:
            return 'Tie'


if __name__ == "__main__":
    sol = Solution()
    tests = int(input())

    for t in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        result = sol.solve(arr)
        print(result)

    # arr = [1,2,3,4,5]
    # result = sol.solve(arr)
    # print(result)


"""
2
7 5 3
"""
