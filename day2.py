from int_compute import (load_input,
                         interp,
                         run_prog)

test1=[1,0,0,3,99]

def run_part_1():
  i = load_input("day2")
  i[1] = 12
  i[2] = 2
  run_prog(i)

def calc_prog_with_values(noun, verb):
  i = load_input("day2")
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
    except IndexError:
      #print(f"Failing on {noun}, {verb}" )
      pass

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