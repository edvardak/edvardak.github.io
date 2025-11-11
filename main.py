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

@dataclass(frozen=True)
class BlankLine: ...

MAX_HEADER_SIZE = 6
def scan_header(line: str) -> HeaderBlock:
    level = 0
    while line[level] == r'#' and level < MAX_HEADER_SIZE:
        level+=1
    return HeaderBlock(level=level,content=line[level:].strip())

def extract_until(pos: int, raw: str, until: str = "\n")-> tuple[int, str]:
    next_newline = raw.find(until,pos)
    if next_newline == -1:
        new_pos = len(raw)
        content = raw[pos:]
    else:
        new_pos = next_newline+len(until)
        content = raw[pos:next_newline]

    return new_pos, content.strip()
    
def scan(raw: str):
    pos = 0

    blocks = []

    while pos < len(raw):
        match raw[pos]:
            case '>': 
                pos, content = extract_until(pos, raw)
                blocks.append(QuoteBlock(content=content))
            case r'#': 
                pos, content = extract_until(pos, raw)
                blocks.append(scan_header(content))
            case '`': 
                # either a code block or just the start of inline block
                if raw[pos:pos+3]=="```":
                    pos, content = extract_until(pos+3, raw, "```")
                    blocks.append(CodeBlock(content))
                    # remove text after code block end
                    pos, _ = extract_until(pos, raw)
                else:
                    pos, content = extract_until(pos,raw)
                    blocks.append(TextBlock(content=content))
            case _: 
                pos, content = extract_until(pos,raw)
                if len(content) != 0:
                    blocks.append(TextBlock(content=content))
                else:
                    blocks.append(BlankLine())

    return blocks

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


