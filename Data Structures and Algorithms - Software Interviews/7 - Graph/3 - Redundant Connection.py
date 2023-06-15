#Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

# Constraints:
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

#Solution
class Solution:
    def findRedundantConnection(self, edges):
        parents = []

        for i in range(len(edges) + 1):
            parents.append(i)

        ranks = [1] * (len(edges) + 1)

        def find(node):
            parent = parents[node]
            while parent != parents[parent]:
                #path compression
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 == parent2:
                #connected
                return False
            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]

solution = Solution()
print(solution.findRedundantConnection([[1,2],[1,3],[2,3]])) # [2,3]
print(solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])) # [1,4]