from int_compute import *

def test_0():
  i = [1,1,1,4,99,5,6,0,99]
  in_data = []
  exp_i = [30,1,1,4,2,5,6,0,99]

  run_prog(i, in_data)
  print("Test 0: ", exp_i, " =? ", i )

def test_1():
  i = [3,0,4,0,99]
  in_data = [1616]
  exp_out = [1616]

  out = run_prog(i, in_data)
  print("Test 1: ", exp_out, " =? ", out )

def test_2():
  i = [1002,4,3,4,33]
  in_data = []
  exp_i = [1002,4,3,4,99]

  run_prog(i, in_data)
  print("Test 2: ", exp_i, " =? ", i )

def test_3():
  i = [1101,100,-1,4,0]
  in_data = []
  exp_i = [1101,100,-1,4,99]

  run_prog(i, in_data)
  print("Test 3: ", exp_i, " =? ", i )

def run_part_1():
  i = load_input("day5")
  in_data = [1]
  print(run_prog(i, in_data))

if __name__ == "__main__":
  test_0()
  test_1()
  test_2()
  test_3()
  run_part_1()