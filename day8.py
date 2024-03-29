WIDTH = 25
HEIGHT = 6

def load_input(filename):
  input = []
  with open(filename, 'r')  as f:
    for l in f.readlines():
      input = [char for char in l]
  return input

def part_1():
  data_in = load_input("day8")

  size_layer = HEIGHT * WIDTH
  n_layers = len(data_in)//size_layer

  smallest_layer = n_layers + 1
  smallest_zeroes = size_layer

  for i in range(n_layers):
    patch = data_in[i*size_layer:(i+1)*size_layer]
    zeroes = patch.count("0")
    if zeroes < smallest_zeroes:
      smallest_zeroes = zeroes
      smallest_layer = i

  print(smallest_layer)
  print(smallest_zeroes)

  i = smallest_layer
  patch = data_in[i*size_layer:(i+1)*size_layer]
  print(patch.count("1")*patch.count("2"))

def get_dominant_colour(ra):
  for pix in range(len(ra)):
    if ra[pix] != "2":
      return ra[pix]

def part_2():
  test_data = "0222112222120000"
  test_input = [char for char in test_data]

  def collapse_pixels(height, width, data):
    output = []
    size_layer = height * width
    n_layers = len(data)//size_layer
    
    for h in range(height):
      for w in range(width):
        pix_data = data[w+h*width::height*width]
        output.append(get_dominant_colour(pix_data))
    return output

  def test_collapse():
    collapse_pixels(2,2,test_input)

  print(test_collapse())
  data_in = load_input("day8")
  output = collapse_pixels(HEIGHT, WIDTH, data_in)
  for h in range(HEIGHT):
      for w in range(WIDTH):
        if output[w+h*WIDTH] == "1":
          print("#", end="")
        else:
          print(" ", end="")
      print("")

if __name__ == "__main__":
  part_1()
  part_2()