from collections import deque

def path(graph, start, goal):
    queue = deque([[start]])
    seen = {start}
    while queue:
        current = queue.popleft()
        if current[-1] == goal:
            return current
        for node in graph.get(current[-1], []):
            if node not in seen:
                seen.add(node)
                queue.append(current + [node])
    return None

def solve(value):
    return path(value["graph"], value["start"], value["goal"])
