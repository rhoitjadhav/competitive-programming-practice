class Solution:
    def solve(self, *args):
        n = args[0]
        arr = args[1]

        moves = 0

        for i in range(1, n):
            if arr[i] < arr[i-1]:
                move = arr[i-1] - arr[i]
                arr[i] += move
                moves += move

        return moves


if __name__ == "__main__":
    sol = Solution()

    n = int(input())
    arr = list(map(int, input().split()))
    result = sol.solve(n, arr)
    print(result)
