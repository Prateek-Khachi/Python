from collections import deque
n = 4
# edges = [[1,2],[1,3],[2,6],[3,4],[4,5],[3,5],[5,7],[6,8],[8,7],[9,10]]
edges =[[0,1],[1,2],[2,3],[3,1]]

mp = {}
indeg = [0] * n


for edge in edges:
    u = edge[0]
    v = edge[1]

    if u not in mp:
        mp[u] = []
    mp[u].append(v)
    indeg[v] +=1


q = deque([x for x in range(n) if indeg[x] == 0])
# visited = [False] * n
ans = []    




# for i in range(1,n):
#     if not  visited[i]:
#         q.append(i)
#         visited[i] = True
#         temp = []
#         while q:
#             node = q.popleft()
#             temp.append(node)
#             if node in mp:
#                 for othernode in mp[node]:
#                     if not visited[othernode]:
#                         q.append(othernode)
#                         visited[othernode] = True
#         ans.append(temp)
# print(ans)

while q:
    node = q.popleft()
    ans.append(node)
    if node in mp:
        for othernode in mp[node]:
            indeg[othernode] -=1
            if indeg[othernode] == 0:
                q.append(othernode)

if len(ans) != n:
    print("Cycle exists")
    print(ans)
else:
    print("Cycle doesn't exist")
    print(ans)
