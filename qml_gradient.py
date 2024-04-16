import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# circuit = qml.QNode(my_quantum_function, dev)

# define device to run on single qubit simulator with 1 wire
dev = qml.device('default.qubit', wires=1)
@qml.qnode(dev)
def circuit(x):
    # x is used to define the rotation 
    # along x, y z axis on the 1st wire
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=0)
    qml.RZ(x[2], wires=0)
    # returns expectation value on 0th wire
    # calculating the avg value in the 
    #specific quantum state
    return qml.expval(qml.PauliZ(0))

# create QNode with list of params
result = circuit([0.543, 0.4, 0.9])
print(result)

# gradient calculataion w.r.t 1st arg
d = qml.grad(circuit, argnum=0)
d(([0.543, 0.4, 0.9]))

fig, ax = qml.draw_mpl(circuit)(([0.543, 0.4, 0.9]))
plt.show()


# Cost function
def cost(x):
  return circuit(x)

# automatic differentiation 
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

    if (i + 1) % 20 == 0:
        print("Cost after step {:5d}: {: .7f}".format(i + 1, cost(params)))

print("Optimized rotation angles: {}".format(params))
