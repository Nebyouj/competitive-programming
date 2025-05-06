class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        pro = 0
        visited = [False] * len(isConnected[0])
        
        def dfs(node, visited):
            visited[node] = True

            for i in range(len(isConnected)):
                if isConnected[node][i] and not visited[i]:
                    dfs(i,visited)

        for i in range(len(isConnected)):
            if not visited[i]:
                pro += 1
                dfs(i, visited)

        return pro
