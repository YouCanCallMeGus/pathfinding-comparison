import heapq

def dijkstra(grid, src, dest):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    visited = set()
    distances = {src: 0}
    predecessors = {}
    queue = [(0, src)]  
    explored_cells = []

    while queue:
        current_distance, current_pos = heapq.heappop(queue)

        visited.add(current_pos)
        explored_cells.append(current_pos)

        if current_pos == dest:
            break

        current_row, current_col = current_pos
        for direction in directions:
            nrow, ncol = current_row + direction[0] , current_col + direction[1] 
            neighbor = (current_row + direction[0], current_col + direction[1])

            if 0 <= nrow < rows and 0 <= ncol < cols and neighbor not in visited:
                new_distance = current_distance + grid[nrow][ncol]

                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_pos
                    heapq.heappush(queue, (new_distance, neighbor))

    return explored_cells
