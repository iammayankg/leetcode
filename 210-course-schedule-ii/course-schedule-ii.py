from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for course, prereq in prerequisites:
            if prereq == course:
                continue
            adjList[prereq].append(course)
            indegree[course] += 1

        q = deque([c for c in range(numCourses) if indegree[c] == 0])
        out = []
        while q:
            c = q.popleft()
            out.append(c)

            for nx in adjList[c]:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)

        return out if len(out) == numCourses else []
