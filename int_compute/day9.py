from int_compute import *

def part_1():
  inst = load_input("day9")
  c = int_computer(inst, [1])
  c.run()
  output = c.output
  print(output)

if __name__ == "__main__":
  part_1()
