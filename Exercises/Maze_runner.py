# Maze Runner
# 6 kyu

# You will be given a 2D array of the maze and an array of directions.
# Your task is to follow the directions given.
# If you reach the end point before all your moves have gone, you should return Finish.
# If you hit any walls or go outside the maze border, you should return Dead. 
# If you find yourself still in the maze after using all the moves, you should return Lost.

def maze_runner(maze, directions):
    # Input maze will alway be a sqaure, so dimensions the same
    # ie width = height = length of maze
    dim = len(maze)
    for x in range(dim):
        for y in range(dim):
        # x--> Row selector (y coordinate)
        # y--> Column selector (x coordinate)
            if maze[x][y] == 2:
                xco = y
                yco = x
    
    for dir in directions:
        if dir == 'N':
        # Going north, going up one y coordinate, which is down one index
            yco -= 1
        elif dir == 'S':
            yco += 1
        elif dir == 'E':
            xco += 1
        elif dir == 'W':
            xco -= 1
        
        # If the x or y coordinates are out of range, or the coordinates represent a wall
        if not xco in range(dim) or not yco in range(dim) or maze[yco][xco] == 1: return "Dead"
        
        # If the coorinates represent the end point
        elif maze[yco][xco] == 3: return "Finish"
        
    # If the loop is finished, the maze is not completed, but a wall has not been hit
    return "Lost"
