class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        lists = defaultdict(list)
        for e in edges:
            lists[e[0]].append(e[1])
            lists[e[1]].append(e[0])

        complete = 0
        visit = set()

        def dfs(node):
            v = 0
            e = 0
            stack = [node]
            visit.add(node)

            while stack:
                node = stack.pop()
                
                v += 1
                e += len(lists[node])

                for ne in lists[node]:
                    if ne not in visit:
                        stack.append(ne)
                        visit.add(ne)

            return v, e
            
        for node in range(n):
            if node not in visit:
                v, e = dfs(node)
                if v * (v - 1) == e:
                    complete += 1

        return complete
