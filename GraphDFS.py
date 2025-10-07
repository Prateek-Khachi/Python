def dfs(node, visited, mp, temp):
    if not node:
        return
    
    temp.append(node)
    visited[node] = True

    if node in mp:
        for othernode in mp[node]:
            if not visited[othernode]:
                dfs(othernode, visited, mp, temp)




n = 10
edges = [[1,2],[1,3],[2,6],[3,4],[4,5],[3,5],[5,7],[6,8],[8,7],[9,10]]

mp = {}

for edge in edges:
    u = edge[0]
    v = edge[1]

    if u not in mp:
        mp[u] = []
    mp[u].append(v)


visited = [False] * 11
ans = []

for i in range(1, 11):
    if not visited[i]:
        temp = []
        dfs(i, visited, mp, temp)
        ans.append(temp)

print(ans)