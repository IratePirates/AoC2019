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

if __name__ == "__main__":
  part_1()
