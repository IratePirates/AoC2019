def load_input():
  input = []
  with open("day1", 'r')  as f:
    for l in f.readlines():
       input.append(int(l))
  return input


def calc_fuel(mass):
  return (mass//3 - 2)

def calc_fuel_fuel(mass):
  fuel = 0
  res = mass
  while res > 8:
    a = calc_fuel(res)
    fuel += a
    res = a
    print(f"f {fuel}")
  return fuel


if __name__ == "__main__":
  i = load_input()
  mass = i
  fuel = 0
  for mod in i:
    fuel += calc_fuel_fuel(mod)
  print(fuel)