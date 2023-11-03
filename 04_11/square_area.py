#!/usr/bin/python3
def square_area(s_length, s_width):
    sq = s_length * s_width
    return sq


num_1 = float(input("Enter the square length : "))
num_2 = float(input("Enter the square width : "))

sum_sq = square_area(num_1, num_2)
print(f"for width : {num_1} and length : {num_2} square area is {round(sum_sq, 2)}")
