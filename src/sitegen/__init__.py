from dataclasses import dataclass
from argparse import ArgumentParser
from pathlib import Path
from re import findall

@dataclass(frozen=True)
class Range:
    start: int
    end: int

@dataclass(frozen=True)
class CommentToken:
    range: Range
    text: str

@dataclass
class HeaderBlock:
    level: int
    content: str

@dataclass
class QuoteBlock:
    content: str

@dataclass
class CodeBlock:
    content: str

@dataclass
class UnorderedListBlock:
    content: str

@dataclass
class OrderedListBlock:
    content: str

@dataclass
class TextBlock:
    content: str

@dataclass(frozen=True)
class BlankLine: ...


Block = HeaderBlock | QuoteBlock | CodeBlock | TextBlock | BlankLine

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

def is_list_number(pos: int, raw: str) -> bool:
    end = raw.find(".", pos)
    if end == -1: return False

    return raw[pos:end].isdigit()

def scan_blocks(raw: str) -> list[Block]:
    pos = 0

    blocks: list[Block] = []

    while pos < len(raw):
        c = raw[pos]
        match c:
            case '>': 
                pos, content = extract_until(pos, raw)
                blocks.append(QuoteBlock(content=content))
            case r'#': 
                pos, content = extract_until(pos, raw)
                blocks.append(scan_header(content))
            case '`': 
                # either a code block or just the start of inline code block
                if raw[pos:pos+3]=="```":
                    pos, content = extract_until(pos+3, raw, "```")
                    blocks.append(CodeBlock(content))
                    # remove text after code block end
                    pos, _ = extract_until(pos, raw)
                else:
                    pos, content = extract_until(pos,raw)
                    blocks.append(TextBlock(content=content))
            case "*" | "-" | "+":
                pos+=1 # skip space
                pos, content = extract_until(pos, raw)
                blocks.append(UnorderedListBlock(content=content))
            case c if c.isdigit() and is_list_number(pos, raw):
                # if line starts with a digit, its an ordered list
                pos, _ = extract_until(pos, raw, ".")
                pos, content = extract_until(pos, raw)
                blocks.append(OrderedListBlock(content=content))
            case _: 
                pos, content = extract_until(pos,raw)
                if len(content) != 0:
                    blocks.append(TextBlock(content=content))
                else:
                    blocks.append(BlankLine())

    return blocks

def link_transform(base: str) -> str:

    link_matches = findall(r"(?<!!)\[(.*)\]\((.*)\)", base)

    for match in link_matches:
        text, href = match[0], match[1]
        base = base.replace(f"[{text}]({href})", f"<a href=\"{href}\">{text}</a>")

    return base

def image_transform(base: str) -> str:

    image_matches = findall(r"!\[(.*)\]\((\S+)\W?\"(.*)\"\)", base)

    for match in image_matches:
        alt, src, title = match[0], match[1], match[3]
        base = base.replace(f"![{alt}]({src} \"{title}\")", f"<img src=\"{src}\" alt=\"{alt}\" title=\"{title}\"/>")

    return base

def scan_inline(block: Block) -> Block:
    if isinstance(block, BlankLine):
        return BlankLine()

    block.content = link_transform(block.content)

    return block


def comment_ranges(raw_input: str):
    COMMENT_START = "<!--"
    COMMENT_END = "-->"
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

@dataclass
class Config:
    input_file: Path
    output_folder: Path
    preamble: Path


def get_config() -> Config:

    parser = ArgumentParser(
        prog="Site generator", 
        description="Simple tool to generate html from markdown,\
            adapted to my personal website"
    )

    parser.add_argument("file", help="input markdown file to convert", 
                        type=str)
    parser.add_argument("-o", "--output", 
                        help="output folder to put the converted files in",
                        default="build")
    parser.add_argument("-p", "--preamble", 
                        help="path to preamble file, included in head",
                        default="templates/preamble.html")

    cwd = Path.cwd()
    args = parser.parse_args()
    input_file = (cwd / args.file).resolve()
    output_folder = (cwd / args.output).resolve()
    preamble = (cwd / args.preamble).resolve()

    if not cwd in input_file.parents:
        print(f"file not in subfolder: file={args.file}")
        exit(1)

    if not cwd in output_folder.parents:
        print(f"output folder not in subfolder: file={args.output}")
        exit(1)

    return Config(input_file, output_folder, preamble)
