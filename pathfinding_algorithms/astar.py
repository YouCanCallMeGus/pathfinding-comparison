import heapq

class Cell:
    def __init__(self):
        self.i = 0 
        self.j = 0  
        self.f = float('inf')  
        self.g = float('inf')  
        self.h = 0  

def valid(row, col, grid):
    return (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0])) and grid[row][col] != 1

def pathing(cell, dest):
    path = []
    row, col = dest

    while not (cell[row][col].i == row and cell[row][col].j == col):
        path.insert(0,(row, col))
        temp_row = cell[row][col].i
        temp_col = cell[row][col].j
        row = temp_row
        col = temp_col

    path.insert(0,(row, col))

    return path

def a_star(grid, src, dest):
    if not valid(src[0], src[1], grid) or not valid(dest[0], dest[1], grid):
        return []

    if src == dest:
        return [dest]

    closed_list = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cell = [[Cell() for _ in range(len(grid[0]))] for _ in range(len(grid))]

    i ,j = src
    cell[i][j].f = 0
    cell[i][j].g = 0
    cell[i][j].h = 0
    cell[i][j].i = i
    cell[i][j].j = j

    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    found = False

    while len(open_list) > 0:
        p = heapq.heappop(open_list)

        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if valid(new_i, new_j, grid) and not closed_list[new_i][new_j]:
                if (new_i, new_j) == dest:
                    cell[new_i][new_j].i = i
                    cell[new_i][new_j].j = j
                    found = True
                    return pathing(cell, dest)
                else:
                    g_new = cell[i][j].g + 1.0
                    h_new = ((new_i - dest[0])**2 + (new_j-dest[1])**2)**.5
                    f_new = g_new + h_new

                    if cell[new_i][new_j].f == float('inf') or cell[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell[new_i][new_j].f = f_new
                        cell[new_i][new_j].g = g_new
                        cell[new_i][new_j].h = h_new
                        cell[new_i][new_j].i = i
                        cell[new_i][new_j].j = j

    if not found:
        return []