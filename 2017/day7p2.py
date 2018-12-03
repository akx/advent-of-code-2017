# -- encoding: UTF-8 --

from day7lib import parse_day7_input, to_graph
from toposort import topological

data = parse_day7_input()
graph = to_graph(data)
topo_order = topological(graph)
by_name = {row['name']: row for row in data}


def get_child_weight(by_name, node):
    total_child_weight = 0

    def walk(node):
        nonlocal total_child_weight
        if 'child_weight' in node:
            total_child_weight += node['child_weight']
            return
        for node_name in node['children']:
            child = by_name[node_name]
            total_child_weight += child['weight']
            walk(child)

    walk(node)
    return total_child_weight


def is_balanced(node):
    if not node['children']:
        return True
    children = [by_name[child_name] for child_name in node['children']]
    w0 = children[0]['total_weight']
    return all(c['total_weight'] == w0 for c in children)


for name in reversed(topo_order):
    node = by_name[name]
    node['child_weight'] = get_child_weight(by_name, node)
    node['total_weight'] = node['weight'] + node['child_weight']

for name in topo_order:
    node = by_name[name]
    if not is_balanced(node):
        print(name, node)
