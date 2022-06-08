from queue import Queue
from sys import maxsize

def max_flow(capacity, source, sink):
    residual_capacity = [x[:] for x in capacity]
    augmented_paths = []
    max_flow = 0

    while True:
        found_augmented_path, parent = bfs(residual_capacity, source, sink)
        if not found_augmented_path:
            break
        augmented_path = []
        v = sink
        flow = maxsize

        while v != source:
            augmented_path.append(v)
            u = parent[v]
            if flow > residual_capacity[u][v]:
                flow = residual_capacity[u][v]
            v = u
        
        max_flow += flow

        augmented_path.append(source)
        augmented_path = augmented_path[::-1]
        augmented_paths.append(augmented_path)

        v = sink

        while v != source:
            u = parent[v]
            residual_capacity[u][v] -= flow
            residual_capacity[v][u] += flow
            v = u

    print("Augmented Paths:")
    print(augmented_paths)
    return max_flow        

def bfs(residual_capacity, source, sink):
    visited = set()
    queue = Queue()
    visited.add(source)
    queue.put(source)
    parent = {}
    found_augmented_path = False

    while not queue.empty():
        u = queue.get()
        for i in range(len(residual_capacity)):
            if i not in visited and residual_capacity[u][i] > 0:
                visited.add(i)
                queue.put(i)
                parent[i] = u
                if i == sink:
                    found_augmented_path = True
                    break
        if found_augmented_path:
            break
    
    return found_augmented_path, parent

if __name__ == "__main__":
    capacity = [[0, 3, 0, 3, 0, 0, 0],
                [0, 0, 4, 0, 0, 0, 0],
                [3, 0, 0, 1, 2, 0, 0],
                [0, 0, 0, 0, 2, 6, 0],
                [0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0, 0, 0]]
    
    max_val = max_flow(capacity, 0, 6)
    print(max_val)