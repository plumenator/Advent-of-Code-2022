import builtins

def print(*args):
  # builtins.print(*args)
  pass

def scan_row(heights):
  indices = []
  prev = -1
  for index, height in heights:
    if height > prev:
      indices.append(index)
      prev = height
      print(index, height)
  return indices

def scan_grid(rows):
  indices = []
  for row in rows:
    indices.extend(scan_row(row))
  return indices

def transpose(rows):
  new_rows = [[] for row in rows]
  for row in rows:
    for index, height in enumerate(row):
      new_rows[index].append(height)

  return new_rows


visible = set()

with open('input.txt') as f:
  input = f.read()

grid = [[((x, y), int(height)) for x, height in enumerate(line)] for y, line in enumerate(input.split())]
visible.update(scan_grid(grid))

print(grid)

transposed_grid = transpose(grid)
visible.update(scan_grid(transposed_grid))

print(transposed_grid)

reversed_grid = [list(reversed(row)) for row in transposed_grid]
visible.update(scan_grid(reversed_grid))

print(reversed_grid)

flipped_grid = [list(reversed(row)) for row in grid]
visible.update(scan_grid(flipped_grid))

print(flipped_grid)

print(list(sorted(visible)))

builtins.print(len(visible))