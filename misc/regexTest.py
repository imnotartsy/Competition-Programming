import re
strings1 = ["10384937cm",
"60in",
"190cm",
"190in",
"190"
]

for stri in strings1:
    print(stri, bool(re.match("[0-9]*in", stri)) or bool(re.match("[0-9]*cm", stri)))


strings2 = \
[
    "#123abc",
    "#123abz",
    "123abc",
    "#111111",
    "#1111111",
    "#1111121",
    "#11121234134"
]




for stri in strings2:
    print(stri, len(stri) == 7 and bool(re.match("#[0-9,a-f]{6}", stri)))

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
for stri in strings1:

    print(stri[:-2])