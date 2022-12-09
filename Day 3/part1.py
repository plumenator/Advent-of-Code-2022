with open('input.txt') as f:
  input = f.read()

rucksacks = [(line[:len(line)//2], line[len(line)//2:]) for line in input.split('\n')]

def priority(rucksack):
  c1, c2 = rucksack
  common = set(c1).intersection(c2).pop()
  return item_priority(common)


def item_priority(ch):
  if ch.islower():
    return ord(ch)-ord('a')+1
  else:
    return ord(ch)-ord('A')+27

print(sum(map(priority, rucksacks)))

# this is a version using list comprehension
# priorities = [priority(rucksack) for rucksack in rucksacks]
# print(sum(priorities))
