from functools import wraps, partial
from operator import truth

def yes(value):
    return True


def compose(*functions):
    def composed(arg):
        for function in functions:
            arg = function(arg)
        return arg

    return composed


def imap(fn):
    return partial(map, fn)


def readlines(fp):
    yield from fp


def split_by_whitespace(record):
    return record.strip().split()


def last(iterable):
    ret = None
    for v in iterable:
        ret = v
    return ret


def sample_arr(elements, points):
    n = len(elements)
    yield elements[0]
    for i in range(1, n - 1, int(max(1, n / points))):
        yield elements[i]
    yield elements[n - 1]


def read_input(
    filename,
    records_iterator=readlines,
    record_processor=split_by_whitespace,
    record_prevalidator=truth,
    record_postvalidator=truth,
):
    with open(filename) as infp:
        for record in records_iterator(infp):
            if not record_prevalidator(record):
                continue
            record = record_processor(record)
            if record_postvalidator(record):
                yield record
