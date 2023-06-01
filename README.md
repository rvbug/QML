
# Introduction

This is my jouney of learning Quantum ML specifically QNLP.  
You will have to learn lot of things and some time it will be very strange when you hear things like quantum superposition or entanglement. Best way is to understand is by Intution and also something very important which I learnt from Einstein when I was young - [Thought Experiment](https://en.wikipedia.org/wiki/Einstein%27s_thought_experiments) 

Welcome to the strange world of "Quantum Phyics". This will be very difficult but worth learning if you want to understand how the universe works at the subatomic level.

"Beauty of unknown"...

---
# Basics

PennyLane - A cross platform python library to program Quantum Circuits. This library comes with default simulator devices and can integarate with external software and hardware to run quantum circuits.  
Differential Programming - A paradiam where programs which are differential  
Quantum Computation - Execution of 1 or more Quantum Circuits  
Quantum Circuits (QC)- Collections of quantum gates interconnected by quantum wires   
Quantum Gates (QG) - Also known as  quantum gate is a basic quantum circuit operating on a small number of qubits  
Qubits - Quantum bits is the basic unit of information similar to bits in classical computing helps in storing information. They have more than 2 states unlike bits which are in 0's or 1's   



In Pennylane - these Quantum Circuits are represented as Quantum Node (QNode) and it is used to declare Quantum Circuit + attach to a specific device for execution.

Pennylane's python library does circuit evaluation + gradient calculations.

Quantum Function - A function that describes the wave characterstics of a particle. A quantum circuit is constructed as a special Python function, a quantum circuit function, or quantum function in short. 
<br>




There are two types of circuits 

* Standard - These types are fixed and cannot be trained.
* Variational - Parameterised and could be trained 

## Variational Circuts

These circuits are adaptable and trained using classical optimization algorithms by querying to quantum device. It used the following three components   

- An initial state which is usually fixed (zero state)

- Quantum circuits \$U(\Theta)$ with free parameters \$\Theta$. Think of this as trainable parameters to optimize a cost function where Cost function is a scalar quantity.

    These are defined as  \$\Theta = (\Theta_1, \Theta_2 , ..., \Theta_n)$

- Measurement - Observations as the output of a quantum circuits \$(\hat B$). Could be at each wire in a circuit or at a collection of wires 

### Expectation Values
These are probability values of an experiment usually after a preprocessing stage. 
 
\\( f(\theta) \\)  = \\( \braket{0| U(\theta) (\hat B) U(\theta) | 0} \\)  


Quantum Circuits are collection of quantum gates which are interconnected by quantum wires operating on small number of qubits.

These are called as quantum functions which has some constrains which is beyond the scope of this article


There are some common variational circuit architectures which can be used to build complex architectures

---


# QNLP

---
# References

* Pennylane [Pennylane](https://pennylane.ai/)
* [arXiv](https://arxiv.org/)  
* [Paper with Code](https://paperswithcode.com/)  



