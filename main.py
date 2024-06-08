import heapq
import random
from pyscript import window, document
from pyscript.js_modules import code

canvas = document.getElementById("boardCanvas")
ctx = canvas.getContext("2d")

def generate_grid(size):
  return [[0 for _ in range(size)] for _ in range(size)]

def place_obstacles(grid, num_obstacles):
  size = len(grid)
  for _ in range(num_obstacles):
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    grid[x][y] = 1  # 1 represents an obstacle (signal or crosswalk)

def heuristic(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
  size = len(grid)
  open_list = [(0, start)]
  heapq.heapify(open_list)
  came_from = {}
  g_score = {(i, j): float("inf") for i in range(size) for j in range(size)}
  g_score[start] = 0
  f_score = {(i, j): float("inf") for i in range(size) for j in range(size)}
  f_score[start] = heuristic(start, goal)

  while open_list:
    current = heapq.heappop(open_list)[1]
    if current == goal:
      path = []
      while current in came_from:
        path.append(current)
        current = came_from[current]
        
      path.append(start)
      
      return path[::-1]  # return reversed path

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in neighbors:
      neighbor = (current[0] + dx, current[1] + dy)
      
      if 0 <= neighbor[0] < size and 0 <= neighbor[1] < size:
        tentative_g_score = (g_score[current] + 1 + grid[neighbor[0]][neighbor[1]])
        
        if tentative_g_score < g_score[neighbor]:
          came_from[neighbor] = current
          g_score[neighbor] = tentative_g_score
          f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
          heapq.heappush(open_list, (f_score[neighbor], neighbor))

  return None  # return None if no path is found

size = 10
grid = generate_grid(size)
place_obstacles(grid, 20)  # Place 20 random obstacles

start = (random.randint(0, 5), random.randint(0, 5))
waypoints = [(random.randint(2, 7), random.randint(2, 7))]
goal = (random.randint(0, 10), random.randint(0, 10))

while (start[0] - goal[0]) + (start[1] - goal[1]) <= 0:
  start = (random.randint(0, 5), random.randint(0, 5))
  goal = (random.randint(0, 10), random.randint(0, 10))

code.drawDot(
  ctx,
  45 * (start[0], + 1),
  45 * (11 - start[1]),
  5,
  "rgb(255, 255, 255)"
)
code.drawDot(
  ctx,
  45 * (waypoints[0][0] + 1),
  45 * (11 - waypoints[0][1]),
  5,
  "rgb(0, 255, 0)"
)
code.drawDot(
  ctx,
  45 * (goal[0] + 1),
  45 * (11 - goal[1]),
  5,
  "rgb(255, 0, 0)"
)

path = []
current_start = start

# Iterate through waypoints to form the complete path
for wp in waypoints + [goal]:
  sub_path = a_star(grid, current_start, wp)
  if sub_path is None:
    print(f"No path found to {wp}")
    break
  if path and sub_path:
    path += sub_path[1:]  # avoid duplicating the waypoint
  else:
    path = sub_path
  current_start = wp

if path is not None:
  for i in range(len(path)):
    if len(path) > i + 1:
      code.drawArrow(
        ctx,
        45 * (path[i][0] + 1),
        45 * (11 - path[i][1]),
        45 * (path[i + 1][0] + 1),
        45 * (11 - path[i + 1][1]),
        "red"
      )
  print("Path found:", path)
else:
  print("No path found to goal")
