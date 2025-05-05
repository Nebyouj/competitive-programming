"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp = {}
        for i in range(len(employees)):
            emp[employees[i].id] = [employees[i].importance, employees[i].subordinates]
            
        res = 0
        stack = []
        stack.append(id)

        while stack:
            id_ = stack.pop()
            res += emp[id_][0]
            sub = emp[id_][1]

            for s in sub:
                stack.append(s)

        return res
        
