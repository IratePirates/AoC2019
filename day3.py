def load_input():
  input = []
  with open("day3", 'r')  as f:
    for idx, l in enumerate(f.readlines()):
      tmp_list = []
      for tok in l.split(','):
        tmp_list.append(tok.strip())
      input.append(tmp_list)

  return input

def follow(pos, buff, ins, dist, wire):
  d = ins[0]
  ll = int(ins[1:])

  #update the map
  for l in range(1, ll+1):
    if d is 'U':
      if buff[pos[0]][pos[1]+l] < wire:
        buff[pos[0]][pos[1]+l] += wire + dist + l
    elif d is 'D':
      if buff[pos[0]][pos[1]-l] < wire:
        buff[pos[0]][pos[1]-l] += wire + dist + l
    elif d is 'L':
      if buff[pos[0]-l][pos[1]] < wire:
        buff[pos[0]-l][pos[1]] += wire + dist + l
    elif d is 'R':
      if buff[pos[0]+l][pos[1]] < wire:
        buff[pos[0]+l][pos[1]] += wire + dist + l

  # update the position
  if d is 'U':
    pos = [pos[0], pos[1]+ll]
  elif d is 'D':
    pos = [pos[0], pos[1]-ll]
  elif d is 'L':
    pos = [pos[0]-ll, pos[1]]
  elif d is 'R':
    pos = [pos[0]+ll, pos[1]]

  return pos, ll

def init_map(length):
  full_length = length*2 + 1
  new_map = []

  for i in range(full_length):
    new_list = []
    for j in range(full_length):
      new_list.append(0)
    new_map.append(new_list)

  return new_map

def scan_map(buff, length):
  full_length = length*2 + 1
  crossings = []
  for i in range(full_length):
    for j in range(full_length):
      if buff[i][j] > 1200000:
        crossings.append([i,j, buff[i][j]])
  return crossings

def find_closest_crossing(crossings, length):
  l = (length*length*4)
  for c in crossings:
    d = abs(c[0]-length) + abs(c[1]-length)
    if d < l:
      l = d
  return l


def find_shortest_crossing(crossings):
  l = 400000000
  for c in crossings:
    if c[2] < l:
      l = c[2]
  return l - 1200000

def print_map(buff):
  print(buff)

MAX_DIR = 15000
#MAX_DIR = 1

if __name__ == "__main__":
  i = load_input()
  #i = [["U1","L1"],["L1","U1"]]

  m = init_map(MAX_DIR)

  pos =[MAX_DIR, MAX_DIR]
  tot_dist = 0
  dist = 0
  for idx, insts in enumerate(i[0]):
    pos, dist = follow(pos, m, insts, tot_dist, 400000)
    tot_dist += dist
    print(f"step {idx} - {pos} - {tot_dist}")
  print("First route complete")


  pos =[MAX_DIR, MAX_DIR]
  tot_dist = 0
  dist = 0
  for idx, insts in enumerate(i[1]):
    pos, dist = follow(pos, m, insts, tot_dist, 800000)
    tot_dist += dist
    print(f"step {idx} - {pos} - {tot_dist}")
  print("Second route complete")

  crossings = scan_map(m, MAX_DIR)
  print(f"{len(crossings)} crossings found")
  print(find_shortest_crossing(crossings))
  # print(find_closest_crossing(crossings, MAX_DIR))
  