import builtins
import itertools

def print(*args):
  builtins.print(*args)
  pass

with open('input.txt') as f:
  input = f.read()

lines = input.split('\n')

def parse(line):
  if line == 'noop':
    return [0]
  _, value = line.split()
  return [0, int(value)]

cycles = sum(map(parse, lines), [1])

values = list(itertools.accumulate(cycles))
signal_strengths = list(cycle * xvalue for cycle, xvalue in zip(range(20, 220 + 40, 40), values[19:(219 + 40):40]))

print(sum(signal_strengths))

