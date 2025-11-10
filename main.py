from dataclasses import dataclass

COMMENT_START = "<!--"
COMMENT_END = "-->"

@dataclass(frozen=True)
class Range:
    start: int
    end: int

@dataclass(frozen=True)
class CommentToken:
    range: Range
    text: str

@dataclass(frozen=True)
class ParagraphToken:
    range: Range
    text: str

@dataclass(frozen=True)
class TitleToken:
    range: Range
    level: int
    text: str


def lex(raw_input: str):
    pos = 0
    tokens = []

    while pos < len(raw_input):
        paragraph_end = raw_input.find("\n\n", pos)
        if paragraph_end == -1:
            paragraph_end = len(raw_input)

        text = raw_input[pos:paragraph_end].strip()
        range = Range(pos,paragraph_end-1)

        tokens.append(ParagraphToken(range=range,text=text))

        pos = paragraph_end+2

    return tokens

def comment_ranges(raw_input: str):
    comment_ranges = []
    pos = 0

    while True:
        next_start = raw_input.find(COMMENT_START, pos)
        if next_start == -1: 
            break

        next_end = raw_input.find(COMMENT_END, next_start+len(COMMENT_START))

        if next_end == -1:
            new_range = Range(start=next_start, end=len(raw_input)-1)
            comment_ranges.append(new_range)
            break

        new_range = Range(start=next_start, end=next_end+len(COMMENT_END)-1)
        text = raw_input[new_range.start+4:new_range.end-2].strip()
        comment=CommentToken(range=new_range,text=text)



        comment_ranges.append(comment)

        pos = next_end+len(COMMENT_END)

    return comment_ranges

with open("./templates/preamble.html") as f:
    preamble = f.read()


