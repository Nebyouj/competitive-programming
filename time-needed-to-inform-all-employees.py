class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        tree = defaultdict(list)
        for emp_id, mgr in enumerate(manager):
            if mgr != -1:
                tree[mgr].append(emp_id)

        def dfs(emp):
            max_time = 0

            for s in tree[emp]:
                max_time = max(max_time, dfs(s))
            return informTime[emp] + max_time 

        return dfs(headID)
