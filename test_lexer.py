from main import CommentToken, HeaderBlock, ParagraphToken, Range, comment_ranges, parse_paragraphs, scan_header
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


@pytest.mark.parametrize("incoming, expected", [
    ("",[]),
    ("hey", [ParagraphToken(range=Range(0,2),text="hey")]),
    ("hey ho", [ParagraphToken(range=Range(0,5),text="hey ho")]),
    ("hey ho\n", [ParagraphToken(range=Range(0,6),text="hey ho")]),
    ("hey ho\nha", [ParagraphToken(range=Range(0,8),text="hey ho\nha")]),
    ("hey ho\n\n", [ParagraphToken(range=Range(0,5),text="hey ho")]),
    ("hey ho\n\nhaha", [ParagraphToken(range=Range(0,5),text="hey ho"),ParagraphToken(range=Range(8,11),text="haha")]),
    ("hey ho\n\nhaha\nok", [ParagraphToken(range=Range(0,5),text="hey ho"),ParagraphToken(range=Range(8,14),text="haha\nok")]),
])
def test_lexing_paragraph(incoming, expected):
    assert parse_paragraphs(incoming) == expected



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
