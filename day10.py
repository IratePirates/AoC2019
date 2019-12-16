from math import sqrt, atan, sin, cos

vec1 = [".#..#",
        ".....",
        "#####",
        "....#",
        "...##"]

def load_input(filename):
  input = []
  rows = 0
  with open(filename, 'r')  as f:
    for l in f.readlines():
      input.append(l.strip())
      rows += 1
  w = len(input[0])
  return w, rows, input

def parse_map(width, height, vec_in):
  asteroids = []
  for h in range(height):
    for w in range(width):
      if vec_in[h][w] == '#':
        asteroids.append((w,h))
  return asteroids

def find_distance_vector(a, b):
  return(a[0] - b[0], a[1] - b[1])

def normalise_vector(a):
  mag = sqrt(a[0]*a[0] + a[1]*a[1])
  return (round(a[0]/mag, 7), round(a[1]/mag, 7), mag)

def get_visible_neighbours(point, array):
  this = array.index(point)
  other_ast = [find_distance_vector(b, point) for b in array]
  other_ast.pop(this)

  norm = {}
  for b in other_ast:
    vecx, vecy, mag = normalise_vector(b)
    try:
      if mag < norm[(vecx, vecy)]:
        norm.update({(vecx, vecy):mag})
    except KeyError:
      norm.update({(vecx, vecy):mag})
  return(norm)

def find_base(asteroids):
  visible_neighbours = [0]*len(asteroids)

  for idx, a in enumerate(asteroids):
    norm = get_visible_neighbours(a, asteroids)
    visible_neighbours[idx] = len(norm)

  base = asteroids[visible_neighbours.index(max(visible_neighbours))]
  visible_neighbours = get_visible_neighbours(base, asteroids)
  return (base, visible_neighbours)

def test_1():
  asteroids = parse_map(5,5,vec1)
  b,v = find_base(asteroids)
  print(b, len(v)) # expecting 3,4

def part_1():
  w,h,data_in = load_input("day10")
  # print(w,h,data_in)
  asteroids = parse_map(w,h,data_in)
  # print(asteroids)
  b,v = find_base(asteroids)
  print(b, len(v))

def part_2():
  w,h,data_in = load_input("day10")
  # print(w,h,data_in)
  asteroids = parse_map(w,h,data_in)

  base, targets = find_base(asteroids)
  polar_form = []
  count = 0
  for k, mag in targets.items():
    
    print(count, "- ", (k[1],k[0]), "- ")
    try:
      print((atan(k[1]/k[0]), mag))
      polar_form.append((atan(k[1]/k[0]), mag))
    except ZeroDivisionError:
      polar_form.append((0 , mag))
      # print(count, "- ", (k[1],k[0]), "- ")
    count += 1

  print(base)
  polar_form.sort()
  for idx in range(198,202,1):
    res = polar_form[idx]
    print("[{}] = {}, {}".format(idx, 
      round(res[1] * cos(res[0]), 3),
      round(res[1] * sin(res[0]), 3)))

if __name__ == "__main__":
  #test_1()
  part_1()
  part_2()