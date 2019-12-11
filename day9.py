from int_compute import *

def test_1():
  #produces a  recursive copyy of itself - no mechanism to stop yet.
  inst_in = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
  exp_out = inst_in
  c = int_computer(inst_in)
  c.run()
  #print(c.prog)
  print(c.output)

def test_2():
  inst_in = [104,1125899906842624,99]
  c = int_computer(inst_in)
  c.run()
  print(c.output)

def test_3():
  inst_in = [1102,34915192,34915192,7,4,7,99,0]
  c = int_computer(inst_in)
  c.run()
  print(c.output)

def test_4():
  inst_in = [109, -1, 4, 1, 99]
  c = int_computer(inst_in)
  c.run()
  print(c.output)

def test_5():
  inst_in = [109, 1, 203, 2, 204, 2, 99]
  c = int_computer(inst_in, [10])
  c.run()
  print("got {} expected {}".format( c.output, 10))

def part_1():
  inst = load_input("day9")
  c = int_computer(inst, [1])
  c.run()
  output = c.output
  print(output)

if __name__ == "__main__":
  # test_2()
  # test_1()
  # test_3()
  # test_4()
  test_5()
  #part_1()
