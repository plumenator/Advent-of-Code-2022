with open('input.txt') as f:
  input = f.read()

stacks = [['T', 'D', 'W', 'Z', 'V', 'P'], 
          ['L', 'S', 'W', 'V', 'F', 'J', 'D'], 
          ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
          ['R', 'S', 'J'],
          ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
          ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
          ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
          ['P', 'T', 'B', 'Q'],
          ['H', 'G', 'Z', 'R', 'C']
         ]



lines = input.split('\n')
steps = [line.split() for line in lines] 
steps = [(int(count), int(source), int(destination)) for _, count, _, source, _, destination in steps]

for count, source, destination in steps:
  removed = stacks[source - 1][-count:]
  stacks[source - 1] = stacks[source - 1][:-count]  # actual deletion happens here
  stacks[destination - 1].extend(removed)


print(''.join((stack[-1] if stack else ' ') for stack in stacks ))

  

