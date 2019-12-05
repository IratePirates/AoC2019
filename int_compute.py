def load_input(filename):
  input = []
  with open(filename, 'r')  as f:
    for l in f.readlines():
       for tok in l.split(','):
         input.append(int(tok))
  return input

def interp(line, buffer, input=[]):
  ins_len = -1
  res = None

  try:
    op = line[0] % 100

    if op == 99:       # end
      ins_len = 0

    elif op == 3:      # load
      buffer[line[1]] = input.pop(0)
      ins_len = 2

    elif op == 4:      # output
      res = buffer[line[1]]
      ins_len = 2

    elif op == 1:      # Add
      par1 = line[1]
      if ((line[0]&10000)//10000 == 0):
        par1 = buffer[line[1]]

      par2 = line[2]
      if ((line[0]&1000)//1000 == 0):
        par2 = buffer[line[2]]
      buffer[line[3]] = par1 + par2
      ins_len = 4

    elif op == 2:      # Mult
      par1 = line[1]
      if ((line[0]&10000)//10000 == 0):
        par1 = buffer[line[1]]

      par2 = line[2]
      if ((line[0]&1000)//1000 == 0):
        par2 = buffer[line[2]]

      buffer[line[3]] = par1 * par2
      ins_len = 4

  except IndexError:
    print("Bad instruction?", line)
    raise

  return ins_len, res

def run_prog(instructions, input=[]):
  out =[]
  pc = 0
  res = 1 #placeholder vlaue

  while res > 0:
    res, tmp_out = interp(instructions[pc:pc+4], instructions, input)
    pc += res
    if tmp_out != None:
      out.append(tmp_out)
  return out
