def close_compare(a, b, margin=0):
    # return 0 if not abs(a - b) < margin and not a > b else (1 if not abs(a - b) > margin and not a > b else -1)
    return -1 if a < b and abs(a-b) > margin else (1 if a > b else 0)



print(close_compare(3, 5, 3))
print(close_compare(3, 5, 0))
print(close_compare(2, 5, 3))
print(close_compare(5, 5, 3))
print(close_compare(4, 5, ))
print(close_compare(5, 5, ))
print(close_compare(6, 5, ))

# test.assert_equals(close_compare(4, 5), -1)
# test.assert_equals(close_compare(5, 5), 0)
# test.assert_equals(close_compare(6, 5), 1
# test.assert_equals(close_compare(2, 5, 3), 0)
# test.assert_equals(close_compare(5, 5, 3), 0)
# test.assert_equals(close_compare(8, 5, 3), 0)
# test.assert_equals(close_compare(8.1, 5, 3), 1)
# test.assert_equals(close_compare(1.99, 5, 3), -1)
