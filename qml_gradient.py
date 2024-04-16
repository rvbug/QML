import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# circuit = qml.QNode(my_quantum_function, dev)

dev = qml.device('default.qubit', wires=1)
@qml.qnode(dev)
def circuit(x):
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=0)
    qml.RZ(x[2], wires=0)
    return qml.expval(qml.PauliZ(0))


result = circuit([0.543, 0.4, 0.9])
print(result)

d = qml.grad(circuit, argnum=0)
d(([0.543, 0.4, 0.9]))

fig, ax = qml.draw_mpl(circuit)(([0.543, 0.4, 0.9]))
plt.show()

def cost(x):
  return circuit(x)

init_params = np.array([0.011, 0.012, 0.009], requires_grad=True)
print(cost(init_params))


# initialise the optimizer
opt = qml.GradientDescentOptimizer(stepsize=0.4)

# set the number of steps
steps = 100
# set the initial parameter values
params = init_params

for i in range(steps):
    # update the circuit parameters
    params = opt.step(cost, params)

    if (i + 1) % 5 == 0:
        print("Cost after step {:5d}: {: .7f}".format(i + 1, cost(params)))

print("Optimized rotation angles: {}".format(params))
