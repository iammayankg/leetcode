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
        N = len(employees)
        # adjList = defaultdict(list)
        elookup = {}
        for employee in employees:
            elookup[employee.id] = employee

        def dfs(head):
            head_importance = elookup[head].importance
            for sub in elookup[head].subordinates:
                head_importance += dfs(sub)
            return head_importance
        
        return dfs(id)


        