from functools import wraps, partial
from operator import truth


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
