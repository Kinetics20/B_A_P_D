#!/usr/bin/python3
def circle_circuit(diameter):
    pi = 3.14
    circuit = diameter / 2 * pi
    return circuit


diameter = float(input("Enter a diameter : "))
new_circle_circuit = circle_circuit(diameter)
print(f"circle circuit for diameter {diameter} is {new_circle_circuit}")
