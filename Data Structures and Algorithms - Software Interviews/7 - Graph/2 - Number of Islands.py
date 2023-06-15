#Number of Islands

#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#You may assume all four edges of the grid are all surrounded by water.

#Example 1:
#Input:
#11110
#11010
#11000
#00000

#Output: 1

#Example 2:
#Input:
#11000
#11000
#00100
#00011

#Output: 3

#Solution:
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        rowNumber = len(grid)
        columnNumber = len(grid[0])

        visited = set()

        islandCounter = 0

        def bfs(row, column):
            myQueue = []

            visited.add((row, column))
            myQueue.append((row, column))

            while len(myQueue) != 0:
                row, column = myQueue.pop(0)
                myDirections = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for rowDirection, columnDirection in myDirections:
                    newRow = row + rowDirection
                    newColumn = column + columnDirection

                    if (newRow in range(rowNumber) and newColumn in range(columnNumber) and grid[newRow][newColumn] == "1" and (newRow, newColumn) not in visited):
                        visited.add((newRow, newColumn))
                        myQueue.append((newRow, newColumn))

        for row in range(rowNumber):
            for column in range(columnNumber):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row, column)
                    islandCounter += 1

        return islandCounter
    
solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],
                            ["1","1","0","1","0"],
                            ["1","1","0","0","0"],
                            ["0","0","0","0","0"]]))
#Output: 1
print(solution.numIslands([["1","1","0","0","0"],
                            ["1","1","0","0","0"],
                            ["0","0","1","0","0"],
                            ["0","0","0","1","1"]]))
#Output: 3


