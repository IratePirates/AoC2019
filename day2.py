test1=[1,0,0,3,99]

def load_input():
  input = []
  with open("day2", 'r')  as f:
    for l in f.readlines():
       for tok in l.split(','):
         input.append(int(tok))
  return input

def interp(line, buffer):
  if len(line) == 4:
    try:
      if line[0] == 1:
        buffer[line[3]] = buffer[line[1]] + buffer[line[2]]
        return True
      elif line[0] == 2:
        buffer[line[3]] = buffer[line[1]] * buffer[line[2]]
        return True
    except IndexError:
      print(f"Aborting on {line}")
      raise
  elif len(line) == 1:
    if line[0] == 99:
      print("finished")
      return None
  else:
    print("invalid")

def run_prog(input):
  res = interp(input[0:4], input)
  idx = 0
  while res == True:
    #print(f"computing - idx {idx}")
    res = interp(input[idx:idx+4], input)
    idx +=4

def run_part_1():
  i = load_input()
  i[1] = 12
  i[2] = 2
  run_prog(i)

def calc_prog_with_values(noun, verb):
  i = load_input()
  # print(noun,verb,len(i))
  i[1] = noun
  i[2] = verb
  run_prog(i)
  return i[0]  


MAX_SEARCH = 99
def run_part_2():
  noun = 0
  verb = 0
  res = 0

  while res != 19690720:
    try:
      res = calc_prog_with_values(noun, verb)
      if res > 99:
        print(f"interesting result {noun}, {verb}")
    except Exception:
      print(f"Failing on {noun}, {verb}" )

    noun += 1
    if noun > MAX_SEARCH:
      noun = 0
      verb += 1
      if verb  > MAX_SEARCH:
        print ("NO SOLUTION FOUND")
        return 


  print(f"Solution found: {noun} {verb}")

if __name__ == "__main__":
  run_part_2()