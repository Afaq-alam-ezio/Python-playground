import sys


def tsp_dp(graph):
    """
    Solve the Traveling Salesman Problem (TSP) using Dynamic Programming.

    Parameters:
    graph (list of lists): The adjacency matrix representing the weighted graph.

    Returns:
    tuple: A tuple containing the shortest path length and the shortest path itself.
    """
    n = len(graph)
    # Initialize the memoization table to store the shortest path lengths
    dp = [[-1] * n for _ in range(1 << n)]

    # Base case: starting city to itself has distance 0
    dp[1][0] = 0

    # Function to recursively compute the shortest path length
    def dfs(mask, last):
        if dp[mask][last] != -1:
            return dp[mask][last]

        # Try all possible next cities
        min_dist = sys.maxsize
        for city in range(n):
            if mask & (1 << city):
                new_mask = mask ^ (1 << city)
                new_dist = dfs(new_mask, city) + graph[last][city]
                min_dist = min(min_dist, new_dist)

        dp[mask][last] = min_dist
        return min_dist

    # Calculate the shortest path length starting from the first city (index 0)
    min_length = dfs((1 << n) - 1, 0)

    # Reconstruct the shortest path
    path = [0]
    mask = (1 << n) - 1
    last = 0
    while len(path) < n:
        for city in range(1, n):
            if mask & (1 << city):
                if dp[mask][last] == dp[mask ^ (1 << city)][city] + graph[last][city]:
                    path.append(city)
                    mask ^= (1 << city)
                    last = city
                    break

    return min_length, path


# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
shortest_length, shortest_path = tsp_dp(graph)
print("Shortest path length:", shortest_length)
print("Shortest path:", shortest_path)
