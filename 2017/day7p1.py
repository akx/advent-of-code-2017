# -- encoding: UTF-8 --

from day7lib import parse_day7_input, to_graph
from toposort import topological

data = parse_day7_input()
graph = to_graph(data)
topo_order = topological(graph)
print(topo_order[0])
