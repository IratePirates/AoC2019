import re

input_re = r"<x=(-?\d*), y=(-?\d*), z=(-?\d*)>"

class Moon(object):
  def __init__(self, points):
    self.velocity = [0,0,0]
    self.position = points

  @property
  def energy(self):
    vel_t = sum(abs(x) for x in self.velocity)
    pos_t = sum(abs(x) for x in self.position)
    return vel_t * pos_t

  def update_velocity(self, other_moons):
    for moon_pos in other_moons:
      for point in range(len(self.position)):
        if self.position[point] > moon_pos[point]:
          self.velocity[point] -= 1
        elif self.position[point] < moon_pos[point]:
          self.velocity[point] += 1

  def update_position(self):
    for point in range(len(self.position)):
      self.position[point] += self.velocity[point]

def load_input(filename):
  input = []
  with open(filename, 'r')  as f:
    for l in f.readlines():
      tokens = re.search(input_re, l)
      positions = [int(tokens.group(1))] + [int(tokens.group(2))] + [int(tokens.group(3))]
      input.append(Moon(positions))
  return input

def part_1():
  moons = load_input("day12")
  for i in range(1000):
    for moon in moons:
      other_moons = [m.position for m in moons if m != moon]
      moon.update_velocity(other_moons)
    for moon in moons:
      moon.update_position()
  print(sum(abs(m.energy) for m in moons))
  print("expecting 7471")

def check_looped(moons, start_positions, axis):
  for moon in moons:
    if 0 != moon.velocity[axis]:
      return False
  for idx, moon in enumerate(moons):
    if moon.position[axis] != start_positions[idx][axis]:
        return False
  return True

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def part_2():
  moons = load_input("day12")
  moon_start = [list(m.position) for m in moons]
  loop_points = []
  for axis in range(3):
    moons = load_input("day12")
    count = 0
    while(True):
      for moon in moons:
        other_moons = [m.position for m in moons if m != moon]
        moon.update_velocity(other_moons)
      for moon in moons:
        moon.update_position()
      count += 1
      if check_looped(moons, moon_start, axis):
        print("[{}]Success Loop: {}".format(axis, count))
        # for moon in moons:
        #   print(moon.position, moon.velocity)
        loop_points.append(count)
        break
  a = lcm(loop_points[0], loop_points[1])
  b = lcm(a, loop_points[2])
  print(b)

if __name__ == "__main__":
  part_1()
  part_2()
