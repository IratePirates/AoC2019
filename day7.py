from int_compute import *

# ins = load_input("day7")

def filter_bad_numbers(num_in):
  num = str(num_in)
  for i in range(5):
    if num.count(str(i)) != 1:
      return False
  return True

def generate_inputs():
  all_in = [a for a in range(44444)]
  inputs = [a for a in all_in if filter_bad_numbers(a)]
  return inputs

def run_part_1():
  all_output = []
  input_codes = generate_inputs()
  
  for input_sig in input_codes:
    output = [0]
    for i in range(5):
      ins = load_input("day7")
      in_data = [int(str(input_sig)[i])] + output
      output = run_prog(ins, in_data)

    all_output.append(output[0])

  return(max(all_output))


if __name__ == "__main__":
  print(run_part_1())