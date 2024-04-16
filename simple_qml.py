import pennylane as qml
# import numpy as np
import matplotlib.pyplot as plt


device = qml.device('default.qubit', wires=2, shots=1000)


def my_quantum_function():
    qml.RZ(0.9, wires=0)
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)
    qml.RY(0.3, wires=1)
    return qml.probs(wires=[0,1])

qnode = qml.QNode(my_quantum_function, device)
print(qml.draw(qnode)())

# output is as shown below
# 0: ──RZ(0.90)─╭●──H────────┤ ╭Probs
# 1: ───────────╰X──RY(0.30)─┤ ╰Probs

# another way to see the circuit
fig, ax = qml.draw_mpl(my_quantum_function)()
plt.show()
