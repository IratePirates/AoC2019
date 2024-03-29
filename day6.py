def load_input(filename):
  input = []
  with open(filename, 'r')  as f:
    for l in f.readlines():
      input.append(l.strip())
  return input

def parse_graph(txt_input):
    res = {}
    for line in txt_input:
        orbit = line.split(')')
        if orbit[0] in res:
            res.update({orbit[0]:res[orbit[0]]+[orbit[1]]}) 
        else:
            res.update({orbit[0]:[orbit[1]]})   
    return res

test1_data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G",
               "G)H", "D)I", "E)J", "J)K", "K)L"]


# def count_downstream_links(graph, start_node="COM", count=0):
#   for orbit in graph[start_node]:
#     try:
#       count += count_downstream_links(graph, orbit, count)
#     except KeyError:
#       count += 1
#       pass
#   return count

def get_parent(graph, node):
  for point, orbits in graph.items():
    if node in orbits:
      return point

def calc_upsteam_distance(graph, start_node):
    # find upstream node
    res = start_node
    distance = 0
    while res is not None:
      res = get_parent(graph, res)
      distance += 1
    return distance - 1

def calc_upsteam_path(graph, start_node):
    # find upstream node
    res = start_node
    path = []
    while res is not None:
      res = get_parent(graph, res)
      if res:
        path += [res]
    return path

def all_nodes(graph):
  planets = []
  for point, orbits in graph.items():
    planets += orbits
  return(list(set(planets)))

def calc_total_orbits(graph):
  res = 0
  for point in all_nodes(graph):
    res += len(calc_upsteam_path(graph, point))
  return res

def test_1():
  graph = parse_graph(test1_data)

  print(calc_upsteam_distance(graph, "B"))
  print(calc_upsteam_path(graph, "C"))
  links = calc_total_orbits(graph)
  print("Test 1: ", links, " =? ",  42 )

def part_1():
  graph = parse_graph(load_input("day6"))
  print(calc_total_orbits(graph))

def part_2():
  graph = parse_graph(load_input("day6"))

  a = calc_upsteam_path(graph, "SAN")
  b = calc_upsteam_path(graph, "YOU")

  a_path = []
  for stop in a:
    if stop not in b:
      a_path += [stop]
    else:
      break

  b_path = []
  for stop in b:
    if stop not in a:
      b_path += [stop]
    else:
      break

  return len(a_path) + len(b_path)

if __name__ == "__main__":
  test_1()
  part_1()
  part_2()
