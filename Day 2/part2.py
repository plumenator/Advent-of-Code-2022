with open('input.txt') as f:
  input = f.read()

games = [line.split() for line in input.split('\n')]

def score(game):
  theirs, instruction = game
  ours = move(theirs, instruction)
  return selection_score(ours) + result_score(theirs, ours)

def move(theirs, instruction):
  if instruction == 'X':
    return dict(A = 'C', B = 'A', C = 'B')[theirs]
  if instruction == 'Y':
    return theirs
  if instruction == 'Z':
    return dict(A = 'B', B = 'C', C = 'A')[theirs]

def selection_score(selection):
  return dict(A = 1, B = 2, C = 3)[selection]

def result_score(theirs, ours):
  return dict(AA = 3, BA = 0, CA = 6, AB = 6, BB = 3, CB = 0, AC = 0, BC = 6, CC = 3)[theirs + ours]

scores = [score(game) for game in games]

print(sum(scores))

