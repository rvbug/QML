# importing pennylane library
import pennylane as qml

import matplotlib.pyplot as plt
plt.style.use('dark_background')


def qfun():
'''
function definition:
apply PauliX & Hadamard on wires 0
return state
'''
  qml.PauliX(wires=0)
  qml.Hadamard(wires=0)
  return qml.state()

# define a device
dev = qml.device(name="default.qubit", wires=1)

# create a QNode for the function on device 
qnode = qml.QNode(qfun, dev)
print(qml.draw(qnode)())

# X is PauliX and H is Haramard gate

#### output
# 0: ──X──H─┤  State

