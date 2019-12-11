from int_compute import int_computer, load_input

def test_1():
  i = [3,0,4,0,99]
  in_data = [1616]
  exp_out = [1616]

  computer = int_computer(i, in_data)
  computer.run()
  print("Test 1: ", exp_out, " =? ", computer.output )

def test_2():
  i = [1002,4,3,4,33]
  in_data = []
  exp_i = [1002,4,3,4,99]

  computer = int_computer(i, in_data)
  computer.run()
  print("Test 2: ", exp_i, " =? ", computer.prog)

def test_3():
  i = [1101,100,-1,4,0]
  in_data = []
  exp_i = [1101,100,-1,4,99]

  computer = int_computer(i, in_data)
  computer.run()
  print("Test 2: ", exp_i, " =? ", computer.prog )

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
