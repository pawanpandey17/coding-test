
from activity import product_sum


def test_case_one():
    assert product_sum([2, 4, [3, -4, [2, 3], [5]], [6, [9]], 8]) == 161


def test_case_two():
    assert product_sum([[6, [[[6, 8]]]]]) == 348
