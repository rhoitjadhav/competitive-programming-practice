class Solution:
    def solve(self, n, matrix):
        stars = []

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == "*":
                    stars.append([i, j])

        star1, star2 = stars[0], stars[1]
        newstar1 = [-1, -1]
        newstar2 = [-1, -1]

        # Rows
        if star1[0] == star2[0]:
            if star1[0] == 0:
                newstar1[0] = star1[0] + 1
                newstar2[0] = star2[0] + 1

            else:
                newstar1[0] = star1[0] - 1
                newstar2[0] = star2[0] - 1

            newstar1[1] = star1[1]
            newstar2[1] = star2[1]

        # Columns
        elif star1[1] == star2[1]:
            if star1[1] == 0:
                newstar1[1] = star1[1] + 1
                newstar2[1] = star2[1] + 1

            else:
                newstar1[1] = star1[1] - 1
                newstar2[1] = star2[1] - 1

            newstar1[0] = star1[0]
            newstar2[0] = star2[0]

        # Random
        else:
            newstar1[1] = star2[1]
            newstar2[1] = star1[1]

            newstar1[0] = star1[0]
            newstar2[0] = star2[0]

        matrix[newstar1[0]][newstar1[1]] = "*"
        matrix[newstar2[0]][newstar2[1]] = "*"

        return matrix


if __name__ == '__main__':
    sol = Solution()
    tests = int(input())
    results = []
    for test in range(tests):
        n = int(input())
        matrix = [list(input()) for _ in range(n)]

        result = sol.solve(n, matrix)
        results.append(result)

    for result in results:
        for row in result:
            print("".join(row))

    # matrix = [['*', '.'], ['*', '.']]
    # n = 2
    # result = sol.solve(n, matrix)
    # print(result)
