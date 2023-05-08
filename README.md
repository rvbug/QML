


# TOC

- Intro to basic QML
- Covers `QNLP` (Quantum NLP)

---
# Introduction


---
# Prerequisties




---
# Details

There are two types of circuits 

- Standard - These types are fixed and cannot be trained.
- Variational - Are parameterised and could be trained 

### Variational Circuits 

These circuits are adaptable and trained using classical optimization algorithms by querying to quantum device. It used the following three components   

- An initial state which is usually fixed (zero state)

- Quantum circuits \\(U(\theta) \\) with free parameters \\(\theta \\). Think of this as trainable parameters to optimize a cost function. Cost function are scalar quantity.

    These are defined as  \\( \theta = (\theta_1, \theta_2 , ..., \theta_n) \\)  

- Measurement - Observations as the output of a quantum circuits \\(\hat B\\). Could be at each wire in a circuit or at a collection of wires 

### Expectation Values
These are probability values of an experiment usually after a preprocessing stage. 
 
\\( f(\theta) \\)  = \\( \braket{0| U(\theta) (\hat B) U(\theta) | 0} \\)  


Quantum Circuits are collection of quantum gates which are interconnected by quantum wires operating on small number of qubits.

These are called as quantum functions which has some constrains which is beyond the scope of this article


# QNLP

---
# References

* Pennylane [Pennylane](https://pennylane.ai/)
* [arXiv](https://arxiv.org/)  
* [Paper with Code](https://paperswithcode.com/)  



