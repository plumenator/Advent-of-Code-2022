with open('input.txt') as f:
  input = f.read()

def is_marker(s):
  return len(set(s)) == 14

window = []


for index, c in enumerate(input):
  window.append(c)
  if len(window) > 14:
    window.pop(0)
  if is_marker(window):
    break

print(index+1)
