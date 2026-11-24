
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, weight in graph.get(node, []):
                new_dist = d + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        ans = max(dist[1:])

        return ans if ans != float('inf') else -1
