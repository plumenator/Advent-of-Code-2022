import itertools

with open('input.txt') as f:
  input = f.read()

monkey_attrs = input.split('\n\n')

class Monkey:
  def __init__(self, monkey_num, items, op, test, truthy, falsy):
    self.num = monkey_num
    self.items = items
    self.op = op
    self.test = test
    self.truthy = truthy
    self.falsy = falsy
    self.count = 0
    
def parse(monkey_attr):
  monkey_num, items, op, test, truthy, falsy = monkey_attr.split('\n')
  return Monkey(parse_num(monkey_num), parse_items(items), parse_op(op), parse_test(test), parse_action(truthy), parse_action(falsy))

def parse_num(num_text):
  return int(num_text[7])

def parse_items(items_text):
  return [int(i) for i in items_text.split(':')[1].split(',')]

import operator
def parse_op(op_text):
  _, _, _, first, op, second = op_text.split()
  op = {'+': operator.add, '*': operator.mul}[op]
  def fun(old):
    first_num = old if first == 'old' else int(first)
    second_num = old if second == 'old' else int(second)
    return op(first_num, second_num)
  return fun

def parse_test(test_text):
  _, _, _, n = test_text.split()
  return int(n)

def parse_action(action_text):
  _, _, _, _, _, n = action_text.split()
  return int(n)

monkeys = list(map(parse, monkey_attrs))


for round in range(1, 21):
  for monkey in monkeys:
    for item in monkey.items:
      worry = monkey.op(item) // 3
      dest = monkey.falsy if worry % monkey.test else monkey.truthy
      monkeys[dest].items.append(worry)
    monkey.count += len(monkey.items)
    monkey.items = []
    
second, first = sorted([m.count for m in monkeys])[-2:]
print(first * second)