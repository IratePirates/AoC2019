from int_compute import *

# ins = load_input("day7")
def generate_inputs(start, end):
  def filter_bad_numbers(num_in, start, end):
    num = str(num_in)
    for i in range(start, end):
      if num.count(str(i)) != 1:
        return False
    return True

  start_point = str(start)*5
  end_point = int(str(end)*5)+1
  print("generating inputs in range: {} - {}".format(start_point, end_point))
  all_in = [a for a in range(int(start_point), end_point)]
  print("filtering numbers in range {} - {}".format(start, end+1))
  inputs = [a for a in all_in if filter_bad_numbers(a,start,end+1)]
  return inputs

def run_part_1():
  all_output = []
  input_codes = generate_inputs(0,4)
  
  for input_sig in input_codes:
    output = [0]
    for i in range(5):
      ins = load_input("day7")
      in_data = [int(str(input_sig)[i])] + output
      output = run_prog(ins, in_data)

    all_output.append(output)

  print(max(all_output))

def run_part_2():
  input_codes = generate_inputs(5,9)
  thrust_results = []

  # for each potential input
  for input_signal in input_codes:
    int_computers = [int_computer(load_input("day7"),
                     [int(str(input_signal)[x])],
                     str(x)) for x in range(5)]

    # # input_signal = [9,8,7,6,5]
    # test_prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    # int_computers = [int_computer(test_prog,
    #                  [int(input_signal[x])],
    #                  str(x)) for x in range(5)]

    count = 0
    result = 0
    int_computers[0].input += [0]

    while int_computers[0].running and int_computers[4].running:
      int_computers[0].run_until_input()

      int_computers[1].input += int_computers[0].output
      int_computers[1].run_until_input()
      
      int_computers[2].input += int_computers[1].output
      int_computers[2].run_until_input()

      int_computers[3].input += int_computers[2].output
      int_computers[3].run_until_input()
      
      int_computers[4].input += int_computers[3].output
      int_computers[4].run_until_input()

      result = int_computers[4].output

      if not int_computers[4].running:
        break

      #complete the loop
      int_computers[0].input += result
      count += 1

    thrust_results.append(result)
  print(max(thrust_results))

if __name__ == "__main__":
  run_part_1()
  run_part_2()
