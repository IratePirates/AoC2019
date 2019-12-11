from int_compute import int_computer, load_input

def run_part_1():
  i = load_input("day5")
  in_data = [1]
  computer = int_computer(i, in_data)
  computer.run()
  print(computer.output)

if __name__ == "__main__":
  test_1()
  test_2()
  test_3()
  run_part_1()
