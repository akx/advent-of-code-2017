# -- encoding: UTF-8 --
import re

from aoclib import read_input, yes, split_by_whitespace, compose, imap
from toposort import topological

line_re = re.compile('^(?P<name>.+?) \((?P<weight>\d+)\)(?: -> (?P<children>.+))?$')

data = list(read_input(
    'input-d7.txt',
    record_processor=compose(
        line_re.match,
        lambda m: m.groupdict(),
        lambda m: dict(
            m,
            weight=int(m['weight']),
            children=(m['children'].split(', ') if m['children'] else []),
        ),
    ),
    record_postvalidator=yes,
))

graph = {}

for row in data:
    graph[row['name']] = row['children']

topo_order = topological(graph)

print(topo_order)
