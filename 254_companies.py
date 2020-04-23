# Given a number N and a 2D matrix(N*N filled with 1's or 0's), 
# find the number of island 1's(An island 1 is a 1 surrounded 
# by 0's on all sides).
# Input Size : 2 <= N <= 100000
# Sample Testcases :
# INPUT
# 2
# 1 0
# 0 0
# OUTPUT
# 1


class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited):
        return (i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    def countIslands(self):
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.DFS(i, j, visited)
                    count += 1
        return count


m = int(input())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split(' '))))
row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)
print(g.countIslands())
