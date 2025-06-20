class Solution:
    def findMedian(self, n, edges, queries):  # <- renamed method
        from collections import defaultdict

        LOG = 17
        tree = defaultdict(list)
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n

        def dfs(u, p):
            for v, w in tree[u]:
                if v != p:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    dfs(v, u)

        dfs(0, -1)

        for k in range(1, LOG):
            for v in range(n):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        def get_path(u, v):
            path = []
            def go_up(x, stop):
                curr = x
                while curr != stop:
                    path.append(curr)
                    curr = parent[0][curr]
                return path
            l = lca(u, v)
            up = []
            curr = u
            while curr != l:
                up.append(curr)
                curr = parent[0][curr]
            path.extend(reversed(up))
            path.append(l)
            curr = v
            down = []
            while curr != l:
                down.append(curr)
                curr = parent[0][curr]
            path.extend(down)
            return path

        def find_weight(u, v):
            l = lca(u, v)
            return dist[u] + dist[v] - 2 * dist[l]

        res = []
        for u, v in queries:
            total = find_weight(u, v)
            half = total / 2

            path = get_path(u, v)
            curr_dist = 0
            for i in range(1, len(path)):
                prev = path[i - 1]
                curr = path[i]
                for nei, w in tree[prev]:
                    if nei == curr:
                        curr_dist += w
                        break
                if curr_dist >= half:
                    res.append(curr)
                    break
            else:
                res.append(path[-1])
        return res
