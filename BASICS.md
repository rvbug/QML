
# *Beauty of unknown*...


# Introduction

Quantum Mechanics is probabilistic and unpredictable in nature.  
Best way to understand complex topics is via inutition and [Thought Experiment](https://en.wikipedia.org/wiki/Einstein%27s_thought_experiments).




# Basics

![image](https://github.com/rvbug/q-gravity/assets/10928536/a6222ef3-fbd3-4cc9-883d-ab2cb9b5fb1f)



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
 
\$ (f(\theta))  = \\( \braket{0| U(\theta) (\hat B) U(\theta) | 0} \\$)  


Quantum Circuits are collection of quantum gates which are interconnected by quantum wires operating on small number of qubits.

These are called as quantum functions which has some constrains which is beyond the scope of this article


There are some common variational circuit architectures which can be used to build complex architectures

---
# References

* Pennylane [Pennylane](https://pennylane.ai/)
* [arXiv](https://arxiv.org/)  
* [Paper with Code](https://paperswithcode.com/)  
