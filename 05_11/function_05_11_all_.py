#!/usr/bin/python3

# 01

def chessboard(n):
    idx = 0

    for _ in range(n):
        if not idx % 2:
            print("# " * (n // 2))
        else:
            print(" #" * (n // 2))
        idx += 1


chessboard(10)
