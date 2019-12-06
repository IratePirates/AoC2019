def load_input(filename):
  input = []
  with open(filename, 'r')  as f:
    for l in f.readlines():
       for tok in l.split(','):
         input.append(int(tok))
  return input


class int_computer(object):
  def __init__(self, input_inst, input=[]):
    self.prog  = input_inst
    self.output = []
    self.input = input
    self.pc = 0

  def run(self):
    res = 1 #placeholder vlaue
    while res > 0:
      res, tmp_out = self.interpret_line(self.prog[self.pc:self.pc+4],
                            input)
      if tmp_out != None:
        self.output.append(tmp_out)

  def get_par1(self, line):
    if (line[0] // 100 % 10) == 0:
      par1 = self.prog[line[1]]
    else:
      par1 = line[1]
    return par1

  def get_par2(self, line):
    if (line[0] // 1000 % 10) == 0:
      par1 = self.prog[line[2]]
    else:
      par1 = line[2]
    return par1

  def interpret_line(self, line, input=[]):
    ins_len = -1
    res = None

    try:
      op = line[0] % 100

      if op == 99:       # end
        ins_len = 0

      elif op == 3:      # load
        self.prog[line[1]] = self.input.pop(0)
        ins_len = 2
        self.pc += ins_len

      elif op == 4:      # output
        res = self.prog[line[1]]
        ins_len = 2
        self.pc += ins_len

      elif op == 5:      # Jump-if-true
        ins_len = 3
        if self.get_par1(line) != 0:
          self.pc = self.get_par2(line)
        else:
          self.pc += ins_len

      elif op == 6:      # Jump-if-false
        ins_len = 3
        if self.get_par1(line) == 0:
          self.pc = self.get_par2(line)
        else:
          self.pc += ins_len

      elif op == 1:      # Add
        self.prog[line[3]] = self.get_par1(line) + self.get_par2(line)
        ins_len = 4
        self.pc += ins_len

      elif op == 2:      # Mult
        self.prog[line[3]] = self.get_par1(line) * self.get_par2(line)
        ins_len = 4
        self.pc += ins_len

      elif op == 7: # less than
        if self.get_par1(line) < self.get_par2(line):
          self.prog[line[3]] = 1
        else:
          self.prog[line[3]] = 0
        ins_len = 4
        self.pc += ins_len

      elif op == 8: # less than
        if self.get_par1(line) == self.get_par2(line):
          self.prog[line[3]] = 1
        else:
          self.prog[line[3]] = 0
        ins_len = 4
        self.pc += ins_len

    except IndexError:
      print("Bad instruction?", line)
      raise

    return ins_len, res

def run_prog(instructions, input=[]):
  computer = int_computer(input_inst=instructions,
                          input=input)
  computer.run()
  return(computer.output)
