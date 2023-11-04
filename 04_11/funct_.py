#!/usr/bin/python3
# def num_sum(x, y, z=30):
#     g_sum = x + y + z
#     return g_sum
#
#
# num_1 = 400
# num_2 = 500
# num_sum_1 = num_sum(num_1, num_2)
# print(f"sum of {num_1} and {num_2} is {num_sum_1} ")

def circle_circuit(diameter):
    pi = 3.14
    circuit = diameter / 2 * pi
    return circuit


diameter = float(input("Enter a diameter : "))
new_circle_circuit = circle_circuit(diameter)
print(f"circle circuit for diameter {diameter} is {new_circle_circuit}")
