import itertools

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

for sprite_positions in (values[0:40], values[40:80], values[80:120], values[120:160], values[160:200], values[200:240]):
  for screen_position, sprite_position in enumerate(sprite_positions):
    if screen_position in (sprite_position - 1, sprite_position, sprite_position + 1):
      print('#', end='')
    else:
      print('.', end='')
  print()
