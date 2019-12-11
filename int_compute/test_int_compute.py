import unittest
from int_compute import *

import unittest

class TestIntCompute(unittest.TestCase):
  def test_store_load(self):
    i = [3,0,4,0,99]
    in_data = [1616]
    exp_out = [1616]

    computer = int_computer(i, in_data)
    computer.run()
    self.assertEqual(exp_out, computer.output)

  def test_immediate_store(self):
    i = [1002,4,3,4,33]
    in_data = []
    exp_i = [1002,4,3,4,99]

    computer = int_computer(i, in_data)
    computer.run()
    self.assertEqual(exp_i, computer.prog)

  def test_3(self):
    i = [1101,100,-1,4,0]
    in_data = []
    exp_i = [1101,100,-1,4,99]

    computer = int_computer(i, in_data)
    computer.run()
    self.assertEqual(exp_i, computer.prog)
  
  def test_quine(self):
    #produces a  recursive copy of itself - no mechanism to stop yet.
    inst_in = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    exp_out = inst_in
    c = int_computer(inst_in)
    c.run()
    self.assertEqual(exp_out, c.output)

  def test_big_load(self):
    inst_in = [104,1125899906842624,99]
    c = int_computer(inst_in)
    c.run()
    self.assertEqual(1125899906842624, c.output[0])

  def test_big_multiply(self):
    inst_in = [1102,34915192,34915192,7,4,7,99,0]
    c = int_computer(inst_in)
    c.run()
    self.assertEqual(1219070632396864, c.output[0])

  def test_pic_change(self):
    inst_in = [109, -1, 4, 1, 99]
    c = int_computer(inst_in)
    c.run()
    self.assertEqual(-1, c.output[0])
    self.assertEqual(-1, c.base_address)

  def test_pic_load(self):
    inst_in = [109, 1, 203, 2, 204, 2, 99]
    c = int_computer(inst_in, [10])
    c.run()
    self.assertEqual(10, c.output[0])

if __name__ == '__main__':
  unittest.main()