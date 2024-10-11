def hill_climbing_min(f, x0):
    x = x0
    path = [x]

    while True:
        neighbors = generate_neighbors(x)

        if not neighbors:
            return path
        best_neighbor = min(neighbors, key=f)

        if f(best_neighbor) > f(x):
            return path
        x = best_neighbor
        path.append(x)

def heuristic(n):
    return h_values[n]



def generate_neighbors(node):
    neighbors_dict = {
        'A': ['B', 'C', 'U'],
        'B': ['E', 'G'],
        'C': ['I', 'J', 'G'],
        'U': ['Y'],
        'E': ['G'],
        'G': ['M'],
        'I': [],
        'J': ['K'],
        'K': ['J', 'Y'],
        'Y': ['M'],
    }
    return neighbors_dict.get(node, [])



h_values = {
    'A': 7,
    'B': 5,
    'C': 3,
    'U': 4,
    'E': 2,
    'G': 3,
    'I': 6,
    'J': 6,
    'K': 1,
    'Y': 2,
    'M': 0
}


start_node = 'A'
path_to_goal = hill_climbing_min(heuristic, start_node)


formatted_path = " → ".join(path_to_goal)
print(f"The path to the goal is: {formatted_path}")
