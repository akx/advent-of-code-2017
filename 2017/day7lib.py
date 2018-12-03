# -- encoding: UTF-8 --
import re

from aoclib import read_input, compose, yes


def parse_day7_input(filename='input-d7.txt'):
    line_re = re.compile('^(?P<name>.+?) \((?P<weight>\d+)\)(?: -> (?P<children>.+))?$')
    data = list(read_input(
        filename,
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
    return data


def to_graph(data):
    return {row['name']: row['children'] for row in data}
