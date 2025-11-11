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


@dataclass(frozen=True)
class HeaderBlock:
    level: int
    content: str

@dataclass(frozen=True)
class QuoteBlock:
    content: str

@dataclass(frozen=True)
class CodeBlock:
    content: str

@dataclass(frozen=True)
class TextBlock:
    content: str

class BlankLine: ...

MAX_HEADER_SIZE = 6
def scan_header(line: str) -> HeaderBlock:
    level = 0
    while line[level] == r'#' and level < MAX_HEADER_SIZE:
        level+=1
    return HeaderBlock(level=level,content=line[level:].strip())


def scan_code(): ...

def scan(raw: str):
    lines = map(lambda l: l.strip(), raw.splitlines())

    blocks = []

    for line in lines:
        if len(line)==0: blocks.append(BlankLine())
        match line[0]:
            case '>': blocks.append(QuoteBlock(content=line))
            case r'#': blocks.append(scan_header(line))
            case '`': blocks.append(scan_code())
            case _: blocks.append(TextBlock(content=line))


def parse_paragraphs(raw_input: str):
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


