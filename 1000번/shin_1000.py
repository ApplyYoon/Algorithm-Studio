import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
ans = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs():
    q = deque([(X, 0)])
    dist = [-1] * (N + 1)
    dist[X] = 0

    while q:
        x, t = q.popleft()
        child = graph[x]

        for c in child:
            if dist[c] == -1:
                dist[c] = t + 1
                q.append((c, t + 1))
    return  dist

result = bfs()
ans = []

for i in range(1, N + 1):
    if result[i] == K:
        ans.append(i)

if ans:
    print(*ans)
else:
    print(-1)