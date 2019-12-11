from copy import deepcopy

def load_input(filename):
  input = []
  with open(filename, 'r')  as f:
    for l in f.readlines():
       for tok in l.split(','):
         input.append(int(tok))
  return input


class int_computer(object):
  def __init__(self, input_inst, input_values=None, tag=""):
    self._prog = deepcopy(input_inst) + [0]*len(input_inst)*200
    self.prog_len = len(input_inst)
    self._output = []
    self.input = []
    if input_values != None:
      self.input += input_values
    self.pc = 0
    self.running = True
    self.stalled = False
    self.tag = tag
    self.base_address = 0

  @property
  def output(self):
    res = self._output
    self._output = []
    return res
  
  @property
  def prog(self):
    return self._prog[:self.prog_len]

  def run(self):
    while self.running:
      self.step()

  def step(self):
    _, tmp_out = self.interpret_line(self._prog[self.pc:self.pc+4])
    if tmp_out != []:
      self._output += tmp_out

  def run_until_input(self, additional_input=None):
    res = 1
    self.stalled = False
    while self.running and not self.stalled:
      res, tmp_out = self.interpret_line(self._prog[self.pc:self.pc+4])
      if tmp_out != []:
        self._output.append(*tmp_out)
    # print("Computer {} - Is Stalled? {}".format(self.tag, self.stalled),
    #       " Is Running? {}". format(self.running))

  def get_par(self, line, par=1):
    mode = line[0] // (10 * (10 ** int(par))) % 10
    if mode == 0:
      par1 = self._prog[line[par]]
    elif mode == 1:
      par1 = line[par]
    elif mode == 2:
      par1 = self._prog[self.base_address + line[par]]
    else:
      raise IOError
    return par1

  def set_par(self, pos, value):
    if pos > self.prog_len:
      self.prog_len = pos
    self._prog[pos] = value

  def interpret_line(self, line):
    ins_len = -1
    res = []

    if not self.running:
      return ins_len, res

    try:
      op = line[0] % 100

      if op == 99:       # end
        ins_len = 0
        self.running = False

      elif op == 3:      # load
        try:
          self.set_par(self.get_par(line, 1),
                       self.input.pop(0))
          ins_len = 2
          self.pc += ins_len
        except IndexError:
          ins_len = 0
          self.stalled = True

      elif op == 4:      # _output
        res = [self.get_par(line,1)]
        ins_len = 2
        self.pc += ins_len

      elif op == 9: # adjust the relative base
        self.base_address += self.get_par(line,1)
        ins_len = 2
        self.pc += ins_len

      elif op == 5:      # Jump-if-true
        ins_len = 3
        if self.get_par(line,1) != 0:
          self.pc = self.get_par(line,2)
        else:
          self.pc += ins_len

      elif op == 6:      # Jump-if-false
        ins_len = 3
        if self.get_par(line,1) == 0:
          self.pc = self.get_par(line,2)
        else:
          self.pc += ins_len

      elif op == 1:      # Add
        self.set_par(line[3],
                     self.get_par(line,1) + self.get_par(line,2))
        ins_len = 4
        self.pc += ins_len

      elif op == 2:      # Mult
        self.set_par(line[3],
                     self.get_par(line,1) * self.get_par(line,2))
        ins_len = 4
        self.pc += ins_len

      elif op == 7: # less than
        self.set_par(line[3],
                     self.get_par(line,1) < self.get_par(line,2))
        ins_len = 4
        self.pc += ins_len

      elif op == 8: # less than
        self.set_par(line[3],
                     self.get_par(line,1) == self.get_par(line,2))
        ins_len = 4
        self.pc += ins_len

    except IndexError:
      print("Bad instruction? [{}] - {}".format(self.pc,
                                              line))
      raise

    return ins_len, res

def run_prog(instructions, in_data=None):
  computer = int_computer(input_inst=instructions,
                          input_values=in_data)
  computer.run()
  return computer._output
