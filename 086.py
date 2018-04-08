"""
Given a string of parentheses, write a function to compute the minimum number
of parentheses to be removed to make the string valid (i.e. each open
parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string
")(", you should return 2, since we must remove all of them.
"""


def min_removals(s):
    count_open = 0
    extra_close = 0
    for paren in s:
        if paren == "(":
            count_open += 1
            continue
        if count_open == 0:
            extra_close += 1
        count_open = max(0, count_open - 1)
    return extra_close + count_open


tests = [
    ("(()())", 0),
    ("()())()", 1),
    (")(", 2),
    ("()(((", 3)
]

for x, count in tests:
    assert(min_removals(x) == count)
