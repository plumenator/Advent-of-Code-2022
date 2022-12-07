with open('input.txt') as f:
  input = f.read()

games = [line.split() for line in input.split('\n')]

def score(game):
  theirs, ours = game
  return selection_score(ours) + result_score(theirs, ours)

def selection_score(selection):
  return dict(X = 1, Y = 2, Z = 3)[selection]

def result_score(theirs, ours):
  return dict(AX = 3, BX = 0, CX = 6, AY = 6, BY = 3, CY = 0, AZ = 0, BZ = 6, CZ = 3)[theirs + ours]

scores = [score(game) for game in games]

print(sum(scores))
