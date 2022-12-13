with open('input.txt') as f:
  input = f.read()

lines = input.split()
pairs = [line.split(',') for line in lines]
assignments = [(first.split('-'), second.split('-')) for first, second in pairs]
assignments = [(list(map(int, first)), list(map(int, second))) for first, second in assignments]

def fully_contained(first, second):
  first_start, first_end = first
  second_start, second_end = second
  return (second_start <= first_start and second_end >= first_end) 

count = 0
for first, second in assignments:
  if fully_contained(first, second):
    count = count + 1
  elif fully_contained(second, first):
    count = count + 1

print(count)
  

