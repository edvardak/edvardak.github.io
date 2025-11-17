from main import CommentToken, HeaderBlock, Range, comment_ranges, is_list_number, link_transform,  scan_blocks, scan_header, TextBlock, CodeBlock, BlankLine, UnorderedListBlock, OrderedListBlock
import pytest

COMMENT_CASES = [
        ("",[]),
        ("<!-- Hey -->",[CommentToken(range=Range(start=0,end=11),text="Hey")]),
        ("<!-- Hey --> <!-- ha -->",[CommentToken(Range(start=0,end=11),text="Hey"), CommentToken(range=Range(start=13,end=23),text="ha")]),
        ("<!-- Hey bro --> <!-- ha -->",[CommentToken(range=Range(start=0,end=15),text="Hey bro"), CommentToken(range=Range(start=17,end=27),text="ha")]),
        ("<!-- <!-- Hey -->",[CommentToken(range=Range(start=0,end=16),text="<!-- Hey")]),
        ("<!-- <!--<!-- Hey -->",[CommentToken(range=Range(start=0,end=20),text="<!--<!-- Hey")]),
        ("<!-- <!-- Hey --> -->",[CommentToken(range=Range(start=0,end=16),text="<!-- Hey")]),
        ("is ok<!-- <!-- Hey --> -->",[CommentToken(range=Range(start=5,end=21), text="<!-- Hey")]),
        ("is ok<!-- <!-- Hey --> hoho -->",[CommentToken(Range(start=5,end=21),text="<!-- Hey")]),
        ("is ok<!-- <!-- Hey --> hoho <!-- dude -->",[CommentToken(range=Range(start=5,end=21), text="<!-- Hey"), CommentToken(range=Range(start=28, end= 40),text="dude")]),
    ]

@pytest.mark.parametrize("incoming, expected", COMMENT_CASES)
def test_lexing_comments(incoming, expected):
    assert comment_ranges(incoming) == expected

@pytest.mark.parametrize("pos, raw, expected", [
    (0, "1", False),
    (0, "1.", True),
    (1, " 1.", True),
    (1, " 10.", True),
    (1, " 10 .", False),
])
def test_list_number(pos, raw, expected):
    assert is_list_number(pos, raw) == expected


@pytest.mark.parametrize("incoming, expected", [
    ("#hey", HeaderBlock(level=1, content="hey")),
    ("# hey", HeaderBlock(level=1, content="hey")),
    ("## hey", HeaderBlock(level=2, content="hey")),
    ("##hey", HeaderBlock(level=2, content="hey")),
    ("### hey", HeaderBlock(level=3, content="hey")),
    ("#### hey", HeaderBlock(level=4, content="hey")),
    ("##### hey", HeaderBlock(level=5, content="hey")),
    ("###### hey", HeaderBlock(level=6, content="hey")),
])
def test_header_scanning(incoming, expected):
    assert scan_header(incoming) == expected



@pytest.mark.parametrize("incoming, expected", [
    ("## hey\n sup \n dude \n``` lalala ``` \n ok\n`no danger here`\n###3",[HeaderBlock(level=2, content='hey'), TextBlock(content='sup'), TextBlock(content='dude'), CodeBlock(content='lalala'),  TextBlock(content='ok'), TextBlock(content='`no danger here`'), HeaderBlock(level=3, content='3')]),
    ("## hey\n sup \n dude \n``` lalala",[HeaderBlock(level=2, content='hey'), TextBlock(content='sup'), TextBlock(content='dude'), CodeBlock(content='lalala')]),
    ("ha\nho\n\nhi",[TextBlock(content='ha'), TextBlock(content='ho'), BlankLine(), TextBlock(content='hi')]),
    ("## hey\n sup \n dude \n```ok```\n- my\n- unordered \n-list\n1.lol\n2. ok",[HeaderBlock(level=2, content='hey'), TextBlock(content='sup'), TextBlock(content='dude'), CodeBlock(content='ok'), UnorderedListBlock(content='my'), UnorderedListBlock(content='unordered'), UnorderedListBlock(content='list'), OrderedListBlock(content='lol'), OrderedListBlock(content='ok')]),
    ("ha\n1 list",[TextBlock(content='ha'), TextBlock(content='1 list')]),
])
def test_scan(incoming, expected):
    assert scan_blocks(incoming) == expected



@pytest.mark.parametrize("incoming, expected", [
    ("",""),
    ("[a](b)","<a href=\"b\">a</a>"),
    ("[Google is useful](https://google.com)","<a href=\"https://google.com\">Google is useful</a>"),
    ("![this is an image](an_image)","![this is an image](an_image)"),
])
def test_link_transform(incoming, expected):
    assert link_transform(incoming) == expected
