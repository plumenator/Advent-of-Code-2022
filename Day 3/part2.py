with open('input.txt') as f:
  input = f.read()

rucksacks = input.split()

groups = []
for i in range(0, len(rucksacks), 3):
  groups.append(rucksacks[i:i+3])


def priority(group):
  r1, r2, r3 = group
  common = set(r1).intersection(r2).intersection(r3).pop()
  return item_priority(common)


def item_priority(ch):
  if ch.islower():
    return ord(ch)-ord('a')+1
  else:
    return ord(ch)-ord('A')+27

print(sum(map(priority, groups)))

# this is a version using list comprehension
# priorities = [priority(rucksack) for rucksack in rucksacks]
# print(sum(priorities))
