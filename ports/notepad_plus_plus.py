"""Notepad++: an XML theme per flavor (every built-in lexer Catppuccin covers, plus a few)."""

import re
from xml.sax.saxutils import quoteattr

from ports._editors import ui
from ports._lib import HEADER, Out, h

META = {
    "id": "notepad-plus-plus",
    "name": "Notepad++",
    "category": "Editors",
    "homepage": "https://notepad-plus-plus.org",
    "enable": {
        "where": "Settings → Style Configurator, after copying the file to %AppData%\\Notepad++\\themes",
        "code": "Select theme: {name}",
        "lang": "text",
    },
    "notes": "Syntax colours for 56 lexers plus the editor chrome: margins, folding, tabs, smart and find "
    "highlights. Pair the dark flavors with Settings → Preferences → Dark Mode so the menus match.",
}

# Lexer name|description, then "styleID NAME[=keywordClass]" entries (from Notepad++'s stylers.model.xml).
# "*user" stands for the eight USER KEYWORDS substyles (128–135).
LEXERS = """
java|Java
    11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 4 NUMBER; 6 STRING; 7 CHARACTER; 10
    OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 15 COMMENT LINE DOC;
    17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR; *user
cmake|CMake
    0 DEFAULT; 1 COMMENT; 2 STRING D; 3 STRING L; 4 STRING R; 5 COMMAND=instre1; 6 PARAMETER; 7
    VARIABLE; 8 USER DEFINED=type1; 9 WHILEDEF; 10 FOREACHDEF; 11 IFDEF; 12 MACRODEF; 13 STRING
    VARIABLE; 14 NUMBER
c|C
    9 PREPROCESSOR; 11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 4 NUMBER; 6 STRING;
    7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 15
    COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR; 23 PREPROCESSOR COMMENT;
    24 PREPROCESSOR COMMENT DOC; *user
cpp|C++
    9 PREPROCESSOR; 11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 4 NUMBER; 6 STRING;
    20 STRINGRAW; 7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3
    COMMENT DOC; 15 COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR; 23
    PREPROCESSOR COMMENT; 24 PREPROCESSOR COMMENT DOC; *user
diff|diff file
    0 DEFAULT; 1 COMMENT; 2 COMMAND; 3 HEADER; 4 POSITION; 5 DELETED; 6 ADDED
rust|Rust
    32 DEFAULT; 0 WHITESPACE; 1 BLOCK COMMENT; 2 LINE COMMENT; 3 BLOCK DOC COMMENT; 4 LINE DOC
    COMMENT; 5 NUMBER; 6 KEYWORDS 1=instre1; 7 KEYWORDS 2=instre2; 8 KEYWORDS 3=type1; 9 KEYWORDS
    4=type2; 10 KEYWORDS 5=type3; 11 KEYWORDS 6=type4; 12 KEYWORDS 7=type5; 13 REGULAR STRING; 14
    RAW STRING; 15 CHARACTER; 16 OPERATOR; 17 IDENTIFIER; 18 LIFETIME; 19 MACRO; 20 LEXICAL ERROR;
    21 BYTE STRING; 22 RAW BYTE STRING; 23 BYTE CHARACTER; 24 C STRING; 25 RAW C STRING
xml|XML
    12 XML START; 13 XML END; 0 DEFAULT; 9 COMMENT; 5 NUMBER; 6 DOUBLE STRING; 7 SINGLE STRING; 1
    TAG; 11 TAG END; 2 TAG UNKNOWN; 3 ATTRIBUTE; 4 ATTRIBUTE UNKNOWN; 21 SGML DEFAULT; 22 SGML
    COMMAND=instre1; 23 SGML 1ST PARAM; 24 SGML DOUBLESTRING; 25 SGML SIMPLESTRING; 31 SGML BLOCK
    DEFAULT; 17 CDATA; 10 ENTITY; 192 USER ATTRIBUTES 1=substyle1; 193 USER ATTRIBUTES 2=substyle2;
    194 USER ATTRIBUTES 3=substyle3; 195 USER ATTRIBUTES 4=substyle4; 196 USER ATTRIBUTES
    5=substyle5; 197 USER ATTRIBUTES 6=substyle6; 198 USER ATTRIBUTES 7=substyle7; 199 USER
    ATTRIBUTES 8=substyle8
html|HTML
    0 DEFAULT; 9 COMMENT; 5 NUMBER; 6 DOUBLE STRING; 7 SINGLE STRING; 1 TAG=instre1; 11 TAG END; 2
    TAG UNKNOWN; 3 ATTRIBUTE; 4 ATTRIBUTE UNKNOWN; 21 SGML DEFAULT; 22 SGML COMMAND=instre2; 23 SGML
    1ST PARAM; 24 SGML DOUBLESTRING; 25 SGML SIMPLESTRING; 31 SGML BLOCK DEFAULT; 17 CDATA; 19
    VALUE; 10 ENTITY; 192 USER TAGS1=substyle1; 193 USER TAGS2=substyle2; 194 USER TAGS3=substyle3;
    195 USER TAGS4=substyle4; 196 USER ATTRIBUTES1=substyle5; 197 USER ATTRIBUTES2=substyle6; 198
    USER ATTRIBUTES3=substyle7; 199 USER ATTRIBUTES4=substyle8
css|CSS
    0 DEFAULT; 1 TAG; 2 CLASS; 3 PSEUDOCLASS=instre2; 4 UNKNOWN PSEUDOCLASS; 5 OPERATOR; 6
    IDENTIFIER=instre1; 7 UNKNOWN IDENTIFIER; 8 VALUE; 9 COMMENT; 10 ID; 11 IMPORTANT; 12 DIRECTIVE;
    13 DOUBLE STRING; 14 SINGLE STRING; 16 ATTRIBUTE; 18 PSEUDOELEMENT=type3; 20 LEGACY
    PSEUDOELEMENT=type5; 22 MEDIA; 23 VARIABLE
cs|C#
    9 PREPROCESSOR; 11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 4 NUMBER; 6 STRING;
    7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 15
    COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR; 23 PREPROCESSOR COMMENT;
    24 PREPROCESSOR COMMENT DOC; *user
sql|SQL
    5 KEYWORD=instre1; 16 USER1=instre2; 19 KEYWORD2=type3; 4 NUMBER; 6 STRING; 7 STRING2; 10
    OPERATOR; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 24 Q OPERATOR
json|JSON
    0 DEFAULT; 1 NUMBER; 2 STRING; 3 STRING EOL; 4 PROPERTY NAME; 5 ESCAPE SEQUENCE; 6 LINE COMMENT;
    7 BLOCK COMMENT; 8 OPERATOR; 9 URI; 10 COMPACT IRI; 11 KEYWORD=instre1; 12 LD KEYWORD=instre2;
    13 ERROR
javascript|JavaScript (embedded)
    41 DEFAULT; 45 NUMBER; 46 WORD; 47 KEYWORD=instre1; 48 DOUBLE STRING; 49 SINGLE STRING; 53
    TEMPLATE LIT. (CLIENT); 68 TEMPLATE LIT. (SERVER); 50 SYMBOLS; 52 REGEX; 42 COMMENT; 43 COMMENT
    LINE; 44 COMMENT DOC; 200 USER KEYWORDS 1=substyle1; 201 USER KEYWORDS 2=substyle2; 202 USER
    KEYWORDS 3=substyle3; 203 USER KEYWORDS 4=substyle4; 204 USER KEYWORDS 5=substyle5; 205 USER
    KEYWORDS 6=substyle6; 206 USER KEYWORDS 7=substyle7; 207 USER KEYWORDS 8=substyle8
javascript.js|JavaScript
    11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 19 WINDOW INSTRUCTION=instre2; 4
    NUMBER; 6 STRING; 20 STRING RAW; 7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2
    COMMENT LINE; 3 COMMENT DOC; 15 COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD
    ERROR; *user
tcl|TCL
    0 DEFAULT; 10 MODIFIER; 11 EXPAND=type3; 12 TCL KEYWORD=instre1; 13 iTCL KEYWORD=type1; 14 TK
    KEYWORD=instre2; 15 TK COMMAND=type2; 3 NUMBER; 9 SUB BRACE; 8 SUBSTITUTION; 6 OPERATOR; 7
    IDENTIFIER; 4 WORD IN QUOTE; 5 IN QUOTE; 1 COMMENT; 2 COMMENT LINE; 20 COMMENT BOX; 21 BLOCK
    COMMENT; 16 USER1=type4; 17 USER2=type5; 18 USER3=type6; 19 USER4=type7
toml|TOML
    0 DEFAULT; 1 COMMENT; 2 IDENTIFIER; 3 KEYWORD=instre1; 4 NUMBER; 5 TABLE; 6 KEY; 7 ERROR; 8
    OPERATOR; 9 STRING SQ; 10 STRING DQ; 11 TRIPLE STRING SQ; 12 TRIPLE STRING DQ; 13 ESCAPE CHAR;
    14 DATETIME
typescript|TypeScript
    11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 19 WINDOW INSTRUCTION; 4 NUMBER; 6
    STRING; 20 STRING RAW; 7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT
    LINE; 3 COMMENT DOC; 15 COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR;
    *user
python|Python
    0 DEFAULT; 1 COMMENT LINE; 2 NUMBER; 3 STRING; 4 CHARACTER; 5 KEYWORDS=instre1; 6 TRIPLE; 7
    TRIPLE DOUBLE; 8 CLASS NAME; 9 DEF NAME; 10 OPERATOR; 11 IDENTIFIER; 12 COMMENT BLOCK; 14
    BUILTINS=instre2; 15 DECORATOR; 20 ATTRIBUTE; 16 F STRING; 17 F CHARACTER; 18 F TRIPLE; 19 F
    TRIPLEDOUBLE; *user
batch|Batch
    0 DEFAULT; 1 COMMENT; 2 KEYWORDS=instre1; 3 LABEL; 4 HIDE SYMBOL; 5 COMMAND; 6 VARIABLE; 7
    OPERATOR; 8 AFTER LABEL
ini|INI file
    0 DEFAULT; 1 COMMENT; 2 SECTION; 3 ASSIGNMENT; 4 DEFVAL; 5 KEY
inno|InnoSetup
    0 DEFAULT; 1 COMMENT; 2 KEYWORD=instre2; 3 PARAMETER=type1; 4 SECTION=instre1; 5
    PREPROCESSOR=type2; 6 PREPROCESSOR INLINE; 7 COMMENT PASCAL; 8 KEYWORD PASCAL=type3; 9 KEYWORD
    USER=type4; 10 STRING DOUBLE; 11 STRING SINGLE; 12 IDENTIFIER
ruby|Ruby
    0 DEFAULT; 1 ERROR; 2 COMMENT LINE; 3 POD; 4 NUMBER; 5 INSTRUCTION=instre1; 6 STRING; 7
    CHARACTER; 8 CLASS NAME; 9 DEF NAME; 10 OPERATOR; 11 IDENTIFIER; 12 REGEX; 13 GLOBAL; 14 SYMBOL;
    15 MODULE NAME; 16 INSTANCE VAR; 17 CLASS VAR; 18 BACKTICKS; 19 DATA SECTION; 24 STRING Q
bash|Bash
    0 DEFAULT; 1 ERROR; 4 INSTRUCTION WORD=instre1; 3 NUMBER; 5 STRING; 6 CHARACTER; 7 OPERATOR; 8
    IDENTIFIER; 9 SCALAR; 2 COMMENT LINE; 10 PARAM; 11 BACKTICKS; 12 HERE DELIM; 13 HERE Q; 128 USER
    KEYWORDS 1=substyle1; 129 USER KEYWORDS 2=substyle2; 130 USER KEYWORDS 3=substyle3; 131 USER
    KEYWORDS 4=substyle4; 132 USER SCALAR 1=substyle5; 133 USER SCALAR 2=substyle6; 134 USER SCALAR
    3=substyle7; 135 USER SCALAR 4=substyle8
haskell|Haskell
    0 DEFAULT; 1 IDENTIFIER; 2 KEYWORD; 3 NUMBER; 4 STRING; 5 CHARACTER; 6 CLASS; 7 MODULE; 8
    CAPITAL; 9 DATA; 10 IMPORT; 11 OPERATOR; 12 INSTANCE; 13 COMMENT LINE; 14 COMMENT BLOCK; 15
    COMMENT BLOCK2; 16 COMMENT BLOCK3
lua|Lua
    0 DEFAULT; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 8 LITERAL STRING; 9 PREPROCESSOR; 5
    INSTRUCTION WORD=instre1; 4 NUMBER; 6 STRING; 7 CHARACTER; 10 OPERATOR; 13 FUNC1=instre2; 14
    FUNC2=type1; 15 FUNC3=type2; 16 USER KEYWORDS 1=type3; 17 USER KEYWORDS 2=type4; 18 USER
    KEYWORDS 3=type5; 19 USER KEYWORDS 4=type6; 11 IDENTIFIER; 20 LABEL; 128 USER KEYWORDS
    5=substyle1; 129 USER KEYWORDS 6=substyle2; 130 USER KEYWORDS 7=substyle3; 131 USER KEYWORDS
    8=substyle4
yaml|YAML
    0 DEFAULT; 2 IDENTIFIER; 1 COMMENT; 3 INSTRUCTION WORD=instre1; 4 NUMBER; 5 REFERENCE; 6
    DOCUMENT; 7 TEXT; 8 ERROR
props|Properties file
    0 DEFAULT; 1 COMMENT; 2 SECTION; 3 ASSIGNMENT; 4 DEFVAL; 5 KEY
php|PHP
    18 QUESTION MARK; 118 DEFAULT; 119 STRING; 104 COMPLEX VARIABLE; 126 STRING VARIABLE; 120 SIMPLE
    STRING; 121 KEYWORDS=instre1; 122 NUMBER; 123 VARIABLE; 124 COMMENT; 125 COMMENT LINE; 127
    OPERATOR; 213 PREDEFINED=substyle6; 214 FUNCS AND METHODS 1=substyle7; 215 FUNCS AND METHODS
    2=substyle8; 208 USER KEYWORDS 1=substyle1; 209 USER KEYWORDS 2=substyle2; 210 USER KEYWORDS
    3=substyle3; 211 USER KEYWORDS 4=substyle4; 212 USER KEYWORDS 5=substyle5
makefile|Makefile
    0 DEFAULT; 1 COMMENT; 2 PREPROCESSOR; 3 IDENTIFIER; 4 OPERATOR; 5 TARGET; 9 IDEOL
powershell|PowerShell
    0 DEFAULT; 1 COMMENT; 2 STRING; 3 CHARACTER; 4 NUMBER; 5 VARIABLE; 6 OPERATOR; 7 IDENTIFIER; 8
    INSTRUCTION WORD=instre1; 9 CMDLET=instre2; 10 ALIAS=type1; 11 FUNCTION=type2; 12 USER
    KEYWORDS=type3; 13 COMMENT STREAM; 14 HERE STRING; 15 HERE CHARACTER; 16 COMMENT DOC
    KEYWORD=type4
matlab|Matlab
    0 DEFAULT; 1 COMMENT; 2 COMMAND; 3 NUMBER; 4 INSTRUCTION WORD=instre1; 5 STRING; 6 OPERATOR; 7
    IDENTIFIER; 8 DOUBLE QUOTE STRING
nncrontab|nnCron
    0 WHITE SPACE; 1 COMMENT; 2 TASK START/END; 3 SECTION KEYWORDS=instre1; 4 KEYWORDS=instre2; 5
    MODIFICATORS=type1; 6 ASTERISK; 7 NUMBER; 8 DOUBLE QUOTED STRING; 9 ENVIRONMENT VARIABLE; 10
    IDENTIFIER
lisp|LISP
    0 DEFAULT; 1 COMMENT LINE; 2 NUMBER; 3 FUNCTION WORD=instre1; 4 FUNCTION WORD2=instre2; 5
    SYMBOL; 6 STRING; 9 IDENTIFIER; 10 OPERATOR=type1; 11 SPECIAL; 12 COMMENT
pascal|Pascal
    0 DEFAULT; 1 IDENTIFIER; 2 COMMENT; 3 COMMENT LINE; 4 COMMENT DOC; 5 PREPROCESSOR; 6
    PREPROCESSOR2; 7 NUMBER; 8 HEX NUMBER; 9 INSTRUCTION WORD=instre1; 10 STRING; 12 CHARACTER; 13
    OPERATOR; 14 ASM; 15 MULTILINESTRING
r|R
    0 DEFAULT; 1 COMMENT; 2 INSTRUCTION WORD=instre1; 3 BASE WORD=instre2; 4 KEYWORD=type1; 5
    NUMBER; 6 STRING; 7 STRING2; 8 OPERATOR; 9 IDENTIFIER; 10 INFIX; 11 INFIXEOL; 12 BACKTICKS; 13
    RAWSTRING; 14 RAWSTRING2; 15 ESCAPESEQUENCE
registry|Registry
    32 DEFAULT STYLE; 0 DEFAULT; 1 COMMENT; 2 VALUE NAME; 3 STRING; 4 HEX DIGIT; 5 VALUE TYPE; 6
    ADDED KEY; 7 REMOVED KEY; 8 ESCAPED CHARACTERS IN STRINGS; 9 GUID IN KEY PATH; 10 GUID IN
    STRING; 11 PARAMETER; 12 OPERATORS
autoit|AutoIt
    0 DEFAULT; 1 COMMENT LINE; 2 COMMENT; 3 NUMBER; 4 FUNCTION=instre2; 5 INSTRUCTION WORD=instre1;
    6 MACRO=type1; 7 STRING; 8 OPERATOR; 9 VARIABLE; 10 SENT=type2; 11 PREPROCESSOR=type3; 12
    SPECIAL=type4; 13 EXPAND=type5; 14 COMOBJ
vb|VB / VBS
    7 DEFAULT; 1 COMMENT; 2 NUMBER; 3 WORD=instre1; 4 STRING; 5 PREPROCESSOR; 6 OPERATOR; 8 DATE
kix|KiXtart
    31 DEFAULT; 1 COMMENT; 2 STRING; 3 STRING2; 4 NUMBER; 5 VAR; 6 MACRO=instre2; 7 INSTRUCTION
    WORD=instre1; 8 FUNCTION=type1; 9 OPERATOR
latex|LaTeX
    0 WHITE SPACE; 1 COMMAND; 2 TAG OPENING; 3 MATH INLINE; 4 COMMENT; 5 TAG CLOSING; 6 MATH BLOCK;
    7 COMMENT BLOCK; 8 VERBATIM SEGMENT; 9 SHORT COMMAND; 10 SPECIAL CHAR; 11 COMMAND OPTIONAL
    ARGUMENT; 12 SYNTAX ERROR
searchResult|Search result
    1 Search Header; 2 File Header; 3 Line Number; 4 Hit Word; 6 Current line background colour
srec|S-Record
    0 DEFAULT; 1 RECSTART; 2 RECTYPE; 3 RECTYPE_UNKNOWN; 4 BYTECOUNT; 5 BYTECOUNT_WRONG; 6
    NOADDRESS; 7 DATAADDRESS; 8 RECCOUNT; 9 STARTADDRESS; 10 ADDRESSFIELD_UNKNOWN; 12 DATA_ODD; 13
    DATA_EVEN; 14 DATA_UNKNOWN; 15 DATA_EMPTY; 16 CHECKSUM; 17 CHECKSUM_WRONG; 18 GARBAGE
ihex|Intel HEX
    0 DEFAULT; 1 RECSTART; 2 RECTYPE; 3 RECTYPE_UNKNOWN; 4 BYTECOUNT; 5 BYTECOUNT_WRONG; 6
    NOADDRESS; 7 DATAADDRESS; 9 STARTADDRESS; 10 ADDRESSFIELD_UNKNOWN; 11 EXTENDEDADDRESS; 12
    DATA_ODD; 13 DATA_EVEN; 14 DATA_UNKNOWN; 15 DATA_EMPTY; 16 CHECKSUM; 17 CHECKSUM_WRONG; 18
    GARBAGE
tex|TeX
    0 DEFAULT; 1 SPECIAL; 2 GROUP; 3 SYMBOL; 4 COMMAND; 5 TEXT
erlang|Erlang
    0 DEFAULT STYLE; 1 DEFAULT COMMENT; 14 FUNCTION COMMENT; 15 MODULE COMMENT; 16 DOCUMENTATION
    HELPER IN COMMENT=type3; 17 DOCUMENTATION MACRO IN COMMENT=type4; 2 VARIABLE; 3 NUMBER; 5
    STRING; 9 CHARACTER; 10 MACRO; 19 MACRO QUOTED; 11 RECORD; 20 RECORD QUOTED; 7 ATOM; 18 ATOM
    QUOTED; 13 NODE NAME; 21 NODE NAME QUOTED; 4 RESERVED WORDS=instre1; 22 BUILT-IN
    FUNCTIONS=instre2; 8 FUNCTION NAME; 23 MODULE NAME; 24 MODULE ATTRIBUTES=type2; 12
    PREPROCESSOR=type1; 6 OPERATORS; 31 UNKNOWN: ERROR
verilog|Verilog
    0 DEFAULT; 11 IDENTIFIER; 5 INSTRUCTION WORD=instre1; 7 KEYWORD=type1; 10 OPERATOR; 4 NUMBER; 9
    PREPROCESSOR; 6 STRING; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT LINE BANG; 19 USER
vhdl|VHDL
    0 DEFAULT; 1 COMMENT; 2 COMMENT LINE BANG; 15 COMMENT BLOCK; 3 NUMBER; 4 STRING; 7 STRING EOL; 5
    OPERATOR; 6 IDENTIFIER; 8 INSTRUCTION=instre1; 9 STD OPERATOR=instre2; 10 ATTRIBUTE=type1; 11
    STD FUNCTION=type2; 12 STD PACKAGE=type3; 13 STD TYPE=type4; 14 USER DEFINE=type5
nfo|DOS Style
    32 DEFAULT
go|Go
    9 PREPROCESSOR; 11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 19 PREDECLARED
    IDENTIFIERS=instre2; 4 NUMBER; 6 STRING; 20 STRING RAW; 7 CHARACTER; 10 OPERATOR; 13 VERBATIM;
    14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 15 COMMENT LINE DOC; 17 COMMENT DOC KEYWORD;
    18 COMMENT DOC KEYWORD ERROR; 23 PREPROCESSOR COMMENT; 24 PREPROCESSOR COMMENT DOC; *user
perl|Perl
    0 DEFAULT; 5 INSTRUCTION WORD=instre1; 4 NUMBER; 10 OPERATOR; 11 IDENTIFIER; 12 SCALAR; 13
    ARRAY; 14 HASH; 15 SYMBOL TABLE; 40 PROTOTYPE; 2 COMMENT LINE; 7 STRING SINGLEQUOTE; 6 STRING
    DOUBLEQUOTE; 20 STRING BACKTICKS; 26 STRING Q; 27 STRING QQ; 28 STRING QX; 29 STRING QR; 30
    STRING QW; 17 REGEX MATCH; 18 REGEX SUBSTITUTION; 44 TRANSLATION; 22 HEREDOC DELIMITER; 23
    HEREDOC SINGLEQUOTE; 24 HEREDOC DOUBLEQUOTE; 25 HEREDOC BACKTICK; 43 VAR IN STRING; 54 VAR IN
    REGEX; 55 VAR IN REGEX SUBSTITUTION; 57 VAR IN BACKTICKS; 61 VAR IN HEREDOC DOUBLEQUOTE; 62 VAR
    IN HEREDOC BACKTICK; 64 VAR IN STRING QQ; 65 VAR IN STRING QX; 66 VAR IN STRING QR; 41 FORMAT
    IDENTIFIER; 42 FORMAT BODY; 21 DATA SECTION; 3 POD; 31 POD VERBATIM; 1 ERROR
swift|Swift
    9 PREPROCESSOR; 11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=type1; 4 NUMBER; 6 STRING;
    7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 15
    COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR; 23 PREPROCESSOR COMMENT;
    24 PREPROCESSOR COMMENT DOC; *user
objc|Objective-C
    19 DIRECTIVE=instre2; 11 DEFAULT; 20 QUALIFIER=type2; 9 PREPROCESSOR; 5 INSTRUCTION
    WORD=instre1; 16 TYPE WORD=type1; 4 NUMBER; 6 STRING; 7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14
    REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT DOC; 15 COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18
    COMMENT DOC KEYWORD ERROR
asm|Assembly
    0 DEFAULT; 1 COMMENT; 2 NUMBER; 3 STRING; 4 OPERATOR; 5 IDENTIFIER; 6 CPU INSTRUCTION=instre1; 7
    MATH INSTRUCTION=instre2; 8 REGISTER=type1; 9 DIRECTIVE=type2; 10 DIRECTIVE OPERAND=type3; 11
    COMMENT BLOCK; 12 CHARACTER; 14 EXT INSTRUCTION=type4
fortran|Fortran (free form)
    0 DEFAULT; 1 COMMENT; 2 NUMBER; 3 STRING; 4 STRING2; 6 OPERATOR; 7 IDENTIFIER; 8 INSTRUCTION
    WORD=instre1; 9 FUNCTION1=instre2; 10 FUNCTION2=type1; 11 PREPROCESSOR; 12 OPERATOR2; 13 LABEL;
    14 CONTINUATION
coffeescript|CoffeeScript
    9 PREPROCESSOR; 11 DEFAULT; 5 INSTRUCTION WORD=instre1; 16 TYPE WORD=instre2; 4 NUMBER; 6
    STRING; 7 CHARACTER; 10 OPERATOR; 13 VERBATIM; 14 REGEX; 1 COMMENT; 2 COMMENT LINE; 3 COMMENT
    DOC; 15 COMMENT LINE DOC; 17 COMMENT DOC KEYWORD; 18 COMMENT DOC KEYWORD ERROR; 19 PREDEFINED
    CONSTANT=type2; 22 COMMENT BLOCK; 23 VERBOSE REGEX; 24 VERBOSE REGEX COMMENT
nsis|NSIS
    0 DEFAULT; 1 COMMENT LINE; 2 STRING DOUBLE QUOTE; 3 STRING LEFT QUOTE; 4 STRING RIGHT QUOTE; 5
    FUNCTION=instre1; 6 VARIABLE=instre2; 7 LABEL=type1; 8 USER DEFINED=type2; 9 SECTION; 10
    SUBSECTION; 11 IF DEFINE; 12 MACRO; 13 STRING VAR; 14 NUMBER; 15 SECTION GROUP; 16 PAGE EX; 17
    FUNCTION DEFINITIONS; 18 COMMENT
"""

USER_KEYWORDS = "; ".join(f"{128 + i} USER KEYWORDS {i + 1}=substyle{i + 1}" for i in range(8))


def lexers():
    """[(name, desc, [(style_id, style_name, keyword_class | None)])]"""
    out = []
    for line in LEXERS.strip("\n").splitlines():
        if not line.startswith(" "):
            name, desc = line.split("|")
            out.append((name, desc, []))
            continue
        chunk = out[-1][2]
        chunk.append(line.strip())
    parsed = []
    for name, desc, chunks in out:
        styles = []
        for item in " ".join(chunks).replace("*user", USER_KEYWORDS).split("; "):
            sid, rest = item.split(" ", 1)
            sname, _, kw = rest.partition("=")
            styles.append((sid, sname, kw or None))
        parsed.append((name, desc, styles))
    return parsed


# Where the generic name rules below would guess wrong: (lexer, style) → role.
OVERRIDES = {
    ("cmake", "COMMAND"): "function", ("cmake", "STRING VARIABLE"): "string.escape",
    ("php", "COMPLEX VARIABLE"): "string.escape",
    ("cmake", "USER DEFINED"): "constant",
    ("cmake", "WHILEDEF"): "keyword", ("cmake", "FOREACHDEF"): "keyword",
    ("cmake", "IFDEF"): "keyword", ("cmake", "MACRODEF"): "keyword",
    ("diff", "COMMAND"): "keyword", ("diff", "HEADER"): "diff_header", ("diff", "POSITION"): "diff_position",
    ("diff", "DELETED"): "deleted", ("diff", "ADDED"): "added",
    ("rust", "KEYWORDS 2"): "keyword", ("rust", "KEYWORDS 3"): "type.builtin",
    ("rust", "KEYWORDS 4"): "type", ("rust", "KEYWORDS 5"): "type", ("rust", "KEYWORDS 6"): "type",
    ("rust", "KEYWORDS 7"): "type", ("rust", "LIFETIME"): "decorator",
    ("xml", "XML START"): "preproc", ("xml", "XML END"): "preproc",
    ("xml", "SGML COMMAND"): "preproc", ("html", "SGML COMMAND"): "preproc",
    ("xml", "TAG END"): "tag", ("html", "TAG END"): "tag",
    ("html", "VALUE"): "string",
    ("css", "TAG"): "tag", ("css", "CLASS"): "attribute", ("css", "ID"): "attribute",
    ("css", "PSEUDOCLASS"): "decorator", ("css", "UNKNOWN PSEUDOCLASS"): "decorator",
    ("css", "PSEUDOELEMENT"): "decorator", ("css", "LEGACY PSEUDOELEMENT"): "decorator",
    ("css", "IDENTIFIER"): "property", ("css", "UNKNOWN IDENTIFIER"): "property",
    ("css", "VALUE"): "constant", ("css", "IMPORTANT"): "keyword", ("css", "DIRECTIVE"): "keyword",
    ("css", "ATTRIBUTE"): "attribute", ("css", "MEDIA"): "keyword", ("css", "VARIABLE"): "property",
    ("sql", "USER1"): "function.builtin", ("sql", "KEYWORD2"): "type", ("sql", "Q OPERATOR"): "keyword",
    ("json", "PROPERTY NAME"): "key", ("json", "KEYWORD"): "constant", ("json", "LD KEYWORD"): "keyword",
    ("json", "URI"): "link", ("json", "COMPACT IRI"): "link",
    ("javascript", "WORD"): "variable",
    ("javascript.js", "WINDOW INSTRUCTION"): "variable.builtin",
    ("typescript", "WINDOW INSTRUCTION"): "variable.builtin",
    ("tcl", "MODIFIER"): "keyword", ("tcl", "EXPAND"): "keyword", ("tcl", "TK KEYWORD"): "function.builtin",
    ("tcl", "TK COMMAND"): "function", ("tcl", "SUB BRACE"): "punctuation", ("tcl", "SUBSTITUTION"): "string.escape",
    ("tcl", "WORD IN QUOTE"): "string", ("tcl", "IN QUOTE"): "string",
    ("toml", "TABLE"): "section", ("toml", "KEY"): "key", ("toml", "KEYWORD"): "boolean",
    ("python", "ATTRIBUTE"): "property", ("python", "BUILTINS"): "function.builtin",
    ("batch", "LABEL"): "decorator", ("batch", "HIDE SYMBOL"): "operator", ("batch", "COMMAND"): "function",
    ("batch", "AFTER LABEL"): "comment",
    ("ini", "SECTION"): "section", ("ini", "ASSIGNMENT"): "operator", ("ini", "DEFVAL"): "constant",
    ("ini", "KEY"): "key",
    ("props", "SECTION"): "section", ("props", "ASSIGNMENT"): "operator", ("props", "DEFVAL"): "constant",
    ("props", "KEY"): "key",
    ("inno", "SECTION"): "section", ("inno", "PARAMETER"): "parameter", ("inno", "KEYWORD USER"): "u1",
    ("ruby", "INSTRUCTION"): "keyword", ("ruby", "GLOBAL"): "variable.builtin", ("ruby", "SYMBOL"): "constant",
    ("ruby", "INSTANCE VAR"): "property", ("ruby", "CLASS VAR"): "property", ("ruby", "DATA SECTION"): "comment",
    ("bash", "SCALAR"): "variable.builtin", ("bash", "PARAM"): "string.escape",
    ("bash", "HERE DELIM"): "keyword", ("bash", "HERE Q"): "string", ("bash", "BACKTICKS"): "string.escape",
    ("haskell", "CLASS"): "type", ("haskell", "MODULE"): "namespace", ("haskell", "CAPITAL"): "type",
    ("haskell", "DATA"): "storage", ("haskell", "IMPORT"): "keyword", ("haskell", "INSTANCE"): "keyword",
    ("lua", "PREPROCESSOR"): "preproc", ("lua", "FUNC1"): "function.builtin", ("lua", "FUNC2"): "function.builtin",
    ("lua", "FUNC3"): "function.builtin", ("lua", "LABEL"): "decorator",
    ("yaml", "IDENTIFIER"): "key", ("yaml", "INSTRUCTION WORD"): "constant", ("yaml", "REFERENCE"): "decorator",
    ("yaml", "DOCUMENT"): "operator", ("yaml", "TEXT"): "string",
    ("php", "QUESTION MARK"): "preproc", ("php", "SIMPLE STRING"): "string", ("php", "STRING VARIABLE"): "string.escape",
    ("php", "PREDEFINED"): "variable.builtin", ("php", "FUNCS AND METHODS 1"): "function.builtin",
    ("php", "FUNCS AND METHODS 2"): "function.builtin",
    ("makefile", "PREPROCESSOR"): "preproc", ("makefile", "TARGET"): "function", ("makefile", "IDEOL"): "invalid",
    ("powershell", "CMDLET"): "function.builtin", ("powershell", "ALIAS"): "function",
    ("powershell", "FUNCTION"): "function", ("powershell", "USER KEYWORDS"): "u1",
    ("powershell", "COMMENT DOC KEYWORD"): "doc_keyword",
    ("matlab", "COMMAND"): "function",
    ("nncrontab", "TASK START/END"): "keyword", ("nncrontab", "SECTION KEYWORDS"): "section",
    ("nncrontab", "MODIFICATORS"): "storage", ("nncrontab", "ASTERISK"): "operator",
    ("lisp", "FUNCTION WORD"): "keyword", ("lisp", "FUNCTION WORD2"): "function.builtin",
    ("lisp", "SYMBOL"): "constant", ("lisp", "OPERATOR"): "operator", ("lisp", "SPECIAL"): "decorator",
    ("pascal", "PREPROCESSOR2"): "preproc", ("pascal", "ASM"): "string.escape",
    ("r", "BASE WORD"): "function.builtin", ("r", "KEYWORD"): "function", ("r", "INFIX"): "operator",
    ("r", "INFIXEOL"): "invalid", ("r", "BACKTICKS"): "variable",
    ("registry", "DEFAULT STYLE"): "default", ("registry", "VALUE NAME"): "key", ("registry", "VALUE TYPE"): "type",
    ("registry", "ADDED KEY"): "section", ("registry", "REMOVED KEY"): "deleted",
    ("registry", "GUID IN KEY PATH"): "constant", ("registry", "GUID IN STRING"): "constant",
    ("registry", "PARAMETER"): "parameter", ("registry", "HEX DIGIT"): "number",
    ("autoit", "MACRO"): "variable.builtin", ("autoit", "SENT"): "string.escape", ("autoit", "SPECIAL"): "decorator",
    ("autoit", "EXPAND"): "keyword", ("autoit", "COMOBJ"): "type",
    ("vb", "WORD"): "keyword", ("vb", "DATE"): "number",
    ("kix", "VAR"): "variable", ("kix", "MACRO"): "variable.builtin",
    ("latex", "COMMAND"): "keyword", ("latex", "SHORT COMMAND"): "keyword", ("latex", "TAG OPENING"): "tag",
    ("latex", "TAG CLOSING"): "tag", ("latex", "MATH INLINE"): "preproc", ("latex", "MATH BLOCK"): "preproc",
    ("latex", "VERBATIM SEGMENT"): "code", ("latex", "COMMAND OPTIONAL ARGUMENT"): "parameter",
    ("latex", "SPECIAL CHAR"): "string.escape", ("latex", "WHITE SPACE"): "default",
    ("tex", "SPECIAL"): "string.escape", ("tex", "GROUP"): "punctuation", ("tex", "SYMBOL"): "operator",
    ("tex", "COMMAND"): "keyword", ("tex", "TEXT"): "default",
    ("searchResult", "Search Header"): "search_header", ("searchResult", "File Header"): "file_header",
    ("searchResult", "Line Number"): "line_number", ("searchResult", "Hit Word"): "hit_word",
    ("searchResult", "Current line background colour"): "current_line",
    ("erlang", "DEFAULT STYLE"): "default", ("erlang", "MACRO"): "preproc", ("erlang", "MACRO QUOTED"): "preproc",
    ("erlang", "RECORD"): "type", ("erlang", "RECORD QUOTED"): "type", ("erlang", "ATOM"): "constant",
    ("erlang", "ATOM QUOTED"): "constant", ("erlang", "NODE NAME"): "namespace",
    ("erlang", "NODE NAME QUOTED"): "namespace", ("erlang", "MODULE ATTRIBUTES"): "decorator",
    ("verilog", "KEYWORD"): "type", ("verilog", "USER"): "u1",
    ("vhdl", "STD OPERATOR"): "keyword", ("vhdl", "ATTRIBUTE"): "decorator",
    ("go", "PREDECLARED IDENTIFIERS"): "function.builtin",
    ("perl", "SCALAR"): "variable", ("perl", "ARRAY"): "variable", ("perl", "HASH"): "variable",
    ("perl", "SYMBOL TABLE"): "variable", ("perl", "PROTOTYPE"): "type", ("perl", "TRANSLATION"): "regexp",
    ("perl", "HEREDOC DELIMITER"): "keyword", ("perl", "FORMAT IDENTIFIER"): "function",
    ("perl", "FORMAT BODY"): "string", ("perl", "DATA SECTION"): "comment", ("perl", "POD VERBATIM"): "code",
    ("objc", "DIRECTIVE"): "keyword", ("objc", "QUALIFIER"): "storage",
    ("asm", "CPU INSTRUCTION"): "keyword", ("asm", "MATH INSTRUCTION"): "function",
    ("asm", "REGISTER"): "variable.builtin", ("asm", "DIRECTIVE"): "preproc", ("asm", "DIRECTIVE OPERAND"): "parameter",
    ("asm", "EXT INSTRUCTION"): "function.builtin",
    ("fortran", "FUNCTION1"): "function.builtin", ("fortran", "FUNCTION2"): "function",
    ("fortran", "OPERATOR2"): "keyword", ("fortran", "LABEL"): "decorator", ("fortran", "CONTINUATION"): "operator",
    ("coffeescript", "TYPE WORD"): "keyword", ("coffeescript", "PREDEFINED CONSTANT"): "constant",
    ("coffeescript", "VERBOSE REGEX"): "regexp",
    ("nsis", "FUNCTION"): "function.builtin", ("nsis", "VARIABLE"): "variable.builtin", ("nsis", "LABEL"): "decorator",
    ("nsis", "USER DEFINED"): "u1", ("nsis", "SECTION"): "section", ("nsis", "SUBSECTION"): "section",
    ("nsis", "SECTION GROUP"): "section", ("nsis", "IF DEFINE"): "preproc", ("nsis", "MACRO"): "preproc",
    ("nsis", "STRING VAR"): "string.escape", ("nsis", "PAGE EX"): "keyword", ("nsis", "FUNCTION DEFINITIONS"): "keyword",
    ("nsis", "STRING LEFT QUOTE"): "string", ("nsis", "STRING RIGHT QUOTE"): "string",
}

# Intel HEX and S-Record: tell the record fields apart.
HEX_FIELDS = {
    "RECSTART": "keyword", "RECTYPE": "type", "BYTECOUNT": "function", "NOADDRESS": "comment",
    "DATAADDRESS": "number", "STARTADDRESS": "number", "EXTENDEDADDRESS": "number", "RECCOUNT": "number",
    "DATA_ODD": "default", "DATA_EVEN": "property", "DATA_EMPTY": "comment", "CHECKSUM": "string.escape",
}

# Generic rules on the style name, first match wins.
RULES = [
    (r"COMMENT DOC KEYWORD ERROR", "error_badge"),
    (r"COMMENT DOC KEYWORD|DOCUMENTATION (HELPER|MACRO)", "doc_keyword"),
    (r"COMMENT|^POD", "comment"),
    (r"ERROR|GARBAGE|_WRONG|_UNKNOWN", "invalid"),
    (r"^USER (KEYWORDS|ATTRIBUTES|TAGS|SCALAR) ?\d$", "user"),
    (r"^(DEFAULT|WHITE ?SPACE|IDENTIFIER|TEXT)$", "default"),
    (r"^SGML (DEFAULT|1ST PARAM|BLOCK DEFAULT)$", "preproc"),
    (r"^VAR IN (REGEX|STRING|BACKTICKS|HEREDOC)", "string.escape"),
    (r"ESCAPE|^ENTITY$|^SPECIAL CHAR$", "string.escape"),
    (r"REGEX", "regexp"),
    (r"STRING|CHARACTER|TRIPLE|VERBATIM|HEREDOC|^HERE |BACKTICKS|TEMPLATE LIT|CDATA", "string"),
    (r"NUMBER|^HEX|DATETIME", "number"),
    (r"^DECORATOR$", "decorator"),
    (r"^MACRO$", "preproc"),
    (r"PREPROCESSOR|^DIRECTIVE$", "preproc"),
    (r"^(OPERATORS?|SYMBOLS?)$", "operator"),
    (r"^TAG", "tag"),
    (r"ATTRIBUTE", "attribute"),
    (r"^(TYPE WORD|TYPE|CLASS NAME|STD TYPE)$", "type"),
    (r"^(DEF NAME|FUNCTION|FUNCTION NAME|STD FUNCTION)$", "function"),
    (r"BUILT-?IN", "function.builtin"),
    (r"^(MODULE NAME|STD PACKAGE)$", "namespace"),
    (r"^(VARIABLE|VAR)$", "variable"),
    (r"ENVIRONMENT VARIABLE", "variable.builtin"),
    (r"^PARAM(ETER)?$", "parameter"),
    (r"^LABEL$", "decorator"),
    (r"INSTRUCTION|KEYWORD|^WORD$|RESERVED", "keyword"),
]
RULES = [(re.compile(p), r) for p, r in RULES]


def classify(lexer, name, kw):
    if (lexer, name) in OVERRIDES:
        return OVERRIDES[(lexer, name)]
    if lexer in ("ihex", "srec") and name in HEX_FIELDS:
        return HEX_FIELDS[name]
    for pat, role in RULES:
        if pat.search(name):
            return role
    if kw == "instre1":
        return "keyword"
    if kw == "type1":
        return "type"
    return "default"


def role_styles(f):
    """role → (fg, bg, fontStyle). fontStyle bits: 1 bold, 2 italic, 4 underline."""
    c = f
    u = ui(f)
    ink = c.crust if f.dark else c.base
    fs = lambda st: (1 if "bold" in st else 0) | (2 if "italic" in st else 0) | (4 if "underline" in st else 0)
    roles = {}
    for syntax_role in ("comment", "keyword", "storage", "operator", "punctuation", "function", "function.builtin",
                        "string", "string.escape", "regexp", "number", "constant", "boolean", "type",
                        "type.builtin", "variable", "variable.builtin", "parameter", "property", "namespace",
                        "tag", "attribute", "decorator", "heading", "link", "code", "invalid"):
        color, st = f.syntax(syntax_role)
        roles[syntax_role] = (color, c.base, fs(st))
    roles.update({
        "default": (c.text, c.base, 0),
        "preproc": (c.clay, c.base, 0),
        "doc_keyword": (c.overlay2, c.base, 3),
        "error_badge": (ink, c.red_hi, 0),
        "key": (f.syntax("function")[0], c.base, 0),  # JSON/TOML/INI keys, like the TextMate port
        "section": (c.orange, c.base, 1),
        "added": (c.green, c.base, 0),
        "deleted": (c.red_hi, c.base, 0),
        "diff_header": (c.denim, c.base, 1),
        "diff_position": (c.denim, c.base, 0),
        "search_header": (c.orange, c.mantle, 1),
        "file_header": (c.yellow, c.base, 1),
        "line_number": (u["line_nr"], c.base, 0),
        "hit_word": (c.text_hi, u["search"], 1),
        "current_line": (None, u["line"], None),
    })
    user = [c.yellow, c.sage, c.clay, c.denim, c.red_hi, c.green, c.orange_hi, c.subtext0]
    for i, col in enumerate(user, 1):
        roles[f"u{i}"] = (col, c.base, 0)
    return roles


def global_styles(f):
    c = f
    u = ui(f)
    ink = c.crust if f.dark else c.base
    fill = lambda col: {"fgColor": col, "bgColor": col}
    tabs = [c.orange, c.green, c.yellow, c.denim, c.red_hi]
    styles = [
        ("Default Style", 32, {"fgColor": c.text, "bgColor": c.base, "fontName": "Consolas", "fontStyle": "0", "fontSize": "10"}),
        ("Indent guideline style", 37, {"fgColor": c.surface1, "bgColor": c.base, "fontName": "", "fontStyle": "0", "fontSize": ""}),
        ("Brace highlight style", 34, {"fgColor": u["bracket_fg"], "bgColor": u["bracket_bg"], "fontName": "", "fontStyle": "1", "fontSize": ""}),
        ("Bad brace colour", 35, {"fgColor": ink, "bgColor": c.red_hi, "fontName": "", "fontStyle": "0", "fontSize": ""}),
        ("Current line background colour", 0, {"bgColor": u["line"]}),
        ("Selected text colour", 0, {"bgColor": u["selection"], "fgColor": c.text_hi}),
        ("Multi-selected text color", 0, {"bgColor": u["selection"]}),
        ("Caret colour", 2069, {"fgColor": u["cursor"]}),
        ("Multi-edit carets color", 0, {"fgColor": c.overlay2}),
        ("Edge colour", 0, {"fgColor": c.surface0}),
        ("Line number margin", 33, {"fgColor": u["line_nr"], "bgColor": c.base, "fontName": "", "fontStyle": "0", "fontSize": ""}),
        ("Bookmark margin", 0, {"bgColor": c.base}),
        ("Change History margin", 0, {"bgColor": c.base}),
        ("Change History modified", 0, fill(c.yellow)),
        ("Change History revert modified", 0, fill(c.denim)),
        ("Change History revert origin", 0, fill(c.sage)),
        ("Change History saved", 0, fill(c.green)),
        ("Fold", 0, {"fgColor": c.overlay1, "bgColor": c.base}),
        ("Fold active", 0, {"fgColor": c.orange}),
        ("Fold margin", 0, {"fgColor": c.base, "bgColor": c.base}),
        ("White space symbol", 0, {"fgColor": c.surface2, "bgColor": c.base}),
        # Indicators below are drawn translucent over the text, so they take the plain accent.
        ("Smart Highlighting", 29, {"bgColor": c.overlay0}),
        ("Find Mark Style", 31, {"bgColor": c.orange}),
        ("Find status: Not found", 0, {"fgColor": c.red_hi}),
        ("Find status: Message", 0, {"fgColor": c.sage}),
        ("Find status: Search end reached", 0, {"fgColor": c.yellow}),
        ("Mark Style 1", 25, {"bgColor": c.denim}),
        ("Mark Style 2", 24, {"bgColor": c.red_hi}),
        ("Mark Style 3", 23, {"bgColor": c.yellow}),
        ("Mark Style 4", 22, {"bgColor": c.sage}),
        ("Mark Style 5", 21, {"bgColor": c.green}),
        ("Incremental highlight all", 28, {"bgColor": c.yellow}),
        ("Tags match highlighting", 27, {"bgColor": c.overlay0}),
        ("Tags attribute", 26, {"bgColor": c.denim}),
        ("Active tab focused indicator", 0, {"fgColor": c.orange}),
        ("Active tab unfocused indicator", 0, {"fgColor": c.overlay0}),
        ("Active tab text", 0, {"fgColor": c.text_hi}),
        ("Inactive tabs", 0, {"fgColor": c.overlay1, "bgColor": c.crust}),
        *((f"Tab color {i}", 0, {"bgColor": col}) for i, col in enumerate(tabs, 1)),
        *((f"Tab color dark mode {i}", 0, {"bgColor": col}) for i, col in enumerate(tabs, 1)),
        ("URL hovered", 0, {"fgColor": c.denim_hi, "bgColor": c.base, "fontStyle": "0"}),
        ("Document map", 0, {"fgColor": c.overlay0, "bgColor": c.surface1}),
        ("EOL custom color", 0, {"fgColor": c.surface2}),
        ("Non-printing characters custom color", 0, {"fgColor": c.overlay0}),
        ("Global override", 0, {"fgColor": c.text, "bgColor": c.base, "fontName": "", "fontStyle": "0", "fontSize": ""}),
    ]
    return styles


def attrs(d):
    return " ".join(f"{k}={quoteattr(h(v) if k.endswith('Color') else v)}" for k, v in d.items())


def theme(f):
    roles = role_styles(f)
    lines = ['<?xml version="1.0" encoding="UTF-8" ?>', f"<!-- {HEADER} -->", "<NotepadPlus>", "    <LexerStyles>"]
    for lexer, desc, styles in lexers():
        lines.append(f'        <LexerType name="{lexer}" desc={quoteattr(desc)} ext="">')
        for sid, name, kw in styles:
            role = classify(lexer, name, kw)
            if role == "user":
                role = f"u{int(name[-1])}"
            fg, bg, style = roles[role]
            d = {"name": name, "styleID": sid}
            if fg:
                d["fgColor"] = fg
            d["bgColor"] = bg
            if style is not None:
                d.update({"fontName": "", "fontStyle": str(style), "fontSize": ""})
            if kw:
                d["keywordClass"] = kw
            lines.append(f"            <WordsStyle {attrs(d)} />")
        lines.append("        </LexerType>")
    lines += ["    </LexerStyles>", "    <GlobalStyles>"]
    for name, sid, d in global_styles(f):
        lines.append(f"        <WidgetStyle {attrs({'name': name, 'styleID': str(sid), **d})} />")
    lines += ["    </GlobalStyles>", "</NotepadPlus>"]
    return "\n".join(lines) + "\n"


def build(flavors):
    return [
        Out(f"{f.name}.xml", theme(f), flavor=f.id, dest=f"%AppData%\\Notepad++\\themes\\{f.name}.xml", lang="xml")
        for f in flavors
    ]
