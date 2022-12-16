from collections import namedtuple
import builtins

def print(*args):
  builtins.print(*args)
  pass

def walk(direction, steps, knots, visited):
  for _ in range(steps):
    knots[0] = step(direction, knots[0][0], knots[0][1])
    for i in range(len(knots) - 1):
      hx, hy = knots[i][0], knots[i][1]
      tx, ty = knots[i + 1][0], knots[i + 1][1]
      if abs(tx - hx) > 1 or abs(ty - hy) > 1:
        knots[i + 1] = follow(tx, ty, hx, hy)
    visited.add((knots[i + 1][0], knots[i + 1][1]))
  return knots

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
  

knots = [(0, 0)] * 10
visited = set(knots)

with open('input.txt') as f:
  input = f.read()

for line in input.split('\n'):
  direction, steps = line.split()
  knots = walk(direction, int(steps), knots, visited)

print(len(visited))