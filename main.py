import pytest
import time
from dataclasses import dataclass

COMMENT_START = "<!--"
COMMENT_END = "-->"

@dataclass(frozen=True)
class Range:
    start: int
    end: int


def comment_ranges(incoming: str):
    comment_ranges = []
    pos = 0

    while True:
        next_start = incoming.find(COMMENT_START, pos)
        if next_start == -1: 
            break

        next_end = incoming.find(COMMENT_END, next_start+len(COMMENT_START))

        if next_end == -1:
            new_range = Range(start=next_start, end=len(incoming)-1)
            comment_ranges.append(new_range)
            break

        new_range = Range(start=next_start, end=next_end+len(COMMENT_END)-1)

        comment_ranges.append(new_range)

        pos = next_end+len(COMMENT_END)

    return comment_ranges

COMMENT_CASES = [
        ("",[]),
        ("<!-- Hey -->",[Range(start=0,end=11)]),
        ("<!-- Hey --> <!-- ha -->",[Range(start=0,end=11), Range(start=13,end=23)]),
        ("<!-- Hey bro --> <!-- ha -->",[Range(start=0,end=15), Range(start=17,end=27)]),
        ("<!-- <!-- Hey -->",[Range(start=0,end=16)]),
        ("<!-- <!--<!-- Hey -->",[Range(start=0,end=20)]),
        ("<!-- <!-- Hey --> -->",[Range(start=0,end=16)]),
        ("is ok<!-- <!-- Hey --> -->",[Range(start=5,end=21)]),
        ("is ok<!-- <!-- Hey --> hoho -->",[Range(start=5,end=21)]),
        ("is ok<!-- <!-- Hey --> hoho <!-- dude -->",[Range(start=5,end=21), Range(start=28, end= 40)]),
    ]


@pytest.mark.parametrize("incoming, expected", COMMENT_CASES)
def test_comment_ranges(incoming, expected):
    assert comment_ranges(incoming) == expected

with open("./templates/preamble.html") as f:
    preamble = f.read()


