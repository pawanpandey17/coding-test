"""
File for Coding test
"""


def product_sum(arr):
    """
    [2,4,[3,-4,[2,3],[5]],[6,[9]],8] =>
    Sum would be 1 * (2 + 4 + 2*(3 - 4 + 2 * (2+3) + 3 * (5)) + 3*(6 + 3*9) + 8 = 161
    6 + 2*24 + 3*33 + 8
    6+ 48 + 99 + 8

    Explanation - Initial multiplier is 1 for all elements in main array,
    now there's a sub array at the index 2 -[3,-4,[2,3],[5]], therefore the
    multiplier becomes (Base Parent Multiplier) * 2 = 1 * 2 = 2, inside
    the sub array there's another set of sub array at the index 2,3 respectively,
    so the multipliers are further multiplied by 2,3 , they become 4 , 6 for those
    sub arrays. Index 3 has another sub array, for which the multiplier becomes
    (Base Parent Multiplier) * 3 = 1 * 3 = 3, which again contains a sub array
     at the index 1, so the multiplier becomes (Parent Multiplier) * 3 = 3 * 3 = 9,
     for that sub array elements
    """
    initial_multiplier = 1
    total = 0
    for idx, val in enumerate(arr):
        if isinstance(val, list):
            total += (2 if idx % 2 == 0 else 3) * (initial_multiplier * product_sum(val))
        else:
            total += val
    return total


if __name__ == "__main__":
    print(product_sum([2, 4, [3, -4, [2, 3], [5]], [6, [9]], 8]))
    print(product_sum([[6, [[[6, 8]]]]]))
