from collections import namedtuple
import builtins

def print(*args):
  builtins.print(*args)
  pass

def walk(direction, steps, h, t, visited):
  hx, hy = h
  tx, ty = t
  for _ in range(steps):
    hx, hy = step(direction, hx, hy)
    if abs(tx - hx) > 1 or abs(ty - hy) > 1:
      tx, ty = follow(tx, ty, hx, hy)
    visited.add((tx, ty))
  return (hx, hy), (tx, ty)

def step(direction, hx, hy):
  if direction == 'U':
    hy += 1
  elif direction == 'D':
    hy -= 1
  elif direction == 'L':
    hx -= 1
  else:
    hx += 1
  return hx, hy

def follow(tx, ty, hx, hy):
  if tx == hx:
    ty += -1 if hy < ty else 1
  elif ty == hy:
    tx += -1 if hx < tx else 1
  else:
    ty += -1 if hy < ty else 1
    tx += -1 if hx < tx else 1
  return tx, ty
  

h = (0, 0)
t = (0, 0)
visited = set([h, t])

with open('input.txt') as f:
  input = f.read()

for line in input.split('\n'):
  direction, steps = line.split()
  h, t = walk(direction, int(steps), h, t, visited)

print(len(visited))