from math import sqrt

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

def normalise_vectors(a):
  mag = sqrt(a[0]*a[0] + a[1]*a[1])
  return (round(a[0]/mag, 7), round(a[1]/mag, 7))

def find_visible_neighbours(asteroids):
  visible_neighbours = [0]*len(asteroids)
  print("total: ", len(asteroids))
  for idx, a in enumerate(asteroids):
    other_ast = [find_distance_vector(b, a) for b in asteroids]
    other_ast.pop(idx)
    # print(a)
    norm = [normalise_vectors(b) for b in other_ast]
    # print("init: ", norm)
    # print("norm: ", list(set(norm)))
    visible_neighbours[idx] = len(list(set(norm)))
  # print(asteroids)
  # print(visible_neighbours)
  print(asteroids[visible_neighbours.index(max(visible_neighbours))])
  print(max(visible_neighbours))

def test_1():
  asteroids = parse_map(5,5,vec1)
  # print(asteroids)
  find_visible_neighbours(asteroids)

def part_1():
  w,h,data_in = load_input("day10")
  # print(w,h,data_in)
  asteroids = parse_map(w,h,data_in)
  # print(asteroids)
  find_visible_neighbours(asteroids)

if __name__ == "__main__":
  #test_1()
  part_1()