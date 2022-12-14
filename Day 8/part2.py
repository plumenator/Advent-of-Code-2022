import builtins

def print(*args):
  builtins.print(*args)
  pass

def score(grid, x, y):
  up = 0
  for index in range(y - 1, -1, -1):
    up += 1
    if grid[index][x] >= grid[y][x]:
      break
  down = 0
  for index in range(y + 1, len(grid), 1):
    down += 1
    if grid[index][x] >= grid[y][x]:      
      break
  left = 0
  for index in range(x - 1, -1, -1):
    left += 1
    if grid[y][index] >= grid[y][x]:
      break
  right = 0
  for index in range(x + 1, len(grid), 1):
    right += 1
    if grid[y][index] >= grid[y][x]:
      break
  return up * down * left * right

with open('input.txt') as f:
  input = f.read()

grid = [[int(height) for height in line] for line in input.split()]

builtins.print(max(score(grid, x, y) for x in range(len(grid)) for y in range(len(grid))))