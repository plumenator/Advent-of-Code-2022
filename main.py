with open('input.txt') as f:
  input = f.read()

blocks = input.split('\n\n')

block_totals = []

for block in blocks:
  calories_counts = block.split()
  block_total = sum(int(calories_count) for calories_count in calories_counts)
  block_totals.append(block_total)

block_totals.sort()

print(block_totals[-1])
print(sum(block_totals[-1:-4:-1]))