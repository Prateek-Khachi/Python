from collections import defaultdict
import heapq
from typing import Dict


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> Dict[int, int]:

        alist = defaultdict(list)

        for u,v,w in edges:
            alist[u].append([v,w])

        ans = {}
        heap = [[0,src]]

        while heap:
            w, node = heapq.heappop(heap)
            if node in ans:
                continue
            ans[node] = w
            for othernode in alist[node]:
                heapq.heappush(heap,[w + othernode[1],othernode[0]])

        for x in range(n):
            if x not in ans:
                ans[x] =-1

        return ans                   