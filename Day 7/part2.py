import builtins

def print(*args):
  # builtins.print(*args)
  pass

total_space = 70000000
unused_needed = 30000000

class Directory:
  def __init__(self, name, parent):
    self.name = name
    self.contents = []
    self.parent = parent

  def is_dir(self):
    return True

  def calc_size(self):
    return sum((item.calc_size() for item in self.contents))

  def flattened_contents(self):
    return sum([item.flattened_contents() for item in self.contents], [self])

  def find_dir(self, name):
    print('searching for', name, 'in', self.contents)
    return next(item for item in self.contents if item.is_dir() and item.name == name)

  def __repr__(self):
    return f"dir-{self.name}"

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def is_dir(self):
    return False

  def calc_size(self):
    return self.size

  def flattened_contents(self):
    return [self]

  def __repr__(self):
    return f"file-{self.name}"


with open('input.txt') as f:
  input = f.read()

root = Directory('/', None)

current_directory = root
for line in input.split('\n')[1:]:
  print(line, 'inside', current_directory)
  tokens = line.split()
  if tokens[0] == '$':
    if tokens[1] == 'cd':
      current_directory = current_directory.parent if tokens[2] == '..' else current_directory.find_dir(tokens[2])
  elif tokens[0] == 'dir':
    current_directory.contents.append(Directory(tokens[1], current_directory))
  else:
    current_directory.contents.append(File(tokens[1], int(tokens[0])))

everything = root.flattened_contents()
print(everything)

unused_space = total_space - root.calc_size()
to_delete_size = unused_needed - unused_space

dir_sizes = [item.calc_size() for item in everything if item.is_dir()]
print(dir_sizes)

builtins.print(min(size for size in dir_sizes if size >= to_delete_size))