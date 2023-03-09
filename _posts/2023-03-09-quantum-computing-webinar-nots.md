---
title: "Quantum Computing, Webinar notes"
tags: quantum computing, webinar
---

Host: Jeron Mulder.

Speakers:
- Frank Phillipson
- Stan van der Linde

# Frank Phillipson

TNO, Maastricht University

**Superposition**.

**Entanglement** -- elements are coupled and they react to each-others changes even in far distances.

Qubits can be in 0 or 1 simultaneously.

Power grows exponentially with number of qubits.

Quantum computers have high error rates and must be kept in ultracold environment.

Good for:
- optimization problems
- data analysis
- simulations

Implementations:
- quantum gates -- IBM, Rigetti, Google, QuTech
- quantum annealer -- D-Wave machine
- Photonic quantum computers (solves boson sampling problem) -- Xanadu and Quix

[!Qubit roadmap](https://www.grss-ieee.org/wp-content/uploads/2022/05/622c4958aa939ca1169e777d_QC_roadmap.png)

Famous Algorythms

- Shor's - factoring
- Grover's - searching in unordered lists
- HHL's - linear systems

Hybrid algorythms:
- QAQA
- VQA

Key outcomes:
- a lot of expectations
- not an answer to all problems
- only small examples currently
- focus on math hard problems, not big data ones
- hybrit approach
- QC is a new tool in your toolbox

## Links

- Learning at [qutechacademy.nl](https://qutechacademy.nl)
- QuTech Academy [on youtube](https://www.youtube.com/qutechacademy)
- https://en.wikipedia.org/wiki/Quantum_error_correction
- https://www.tno.nl/en/digital/digital-innovations/trusted-ict/cyber-security-through-quantum-safe/




## Q&As

> Breaking current-day cryptography sounds like a big problem. How close are we to QC this realistically becoming an issue?

Frank Phillipson 04:43 pm:
> Very close. It is expected to be broken in around 15 years. However, store now and decrypt later is used, so we should already encrypt information differently if we want it to be secret in the future.
> Quoting A Resource Estimation Framework for Quantum Attacks Against Cryptographic Functions – Recent Developments as a summary:  “The currently deployed public key schemes, such as RSA and ECC, are completely broken by Shor’s algorithm. In contrast, the security parameters of symmetric methods and hash functions are reduced by, at most, a factor of two by the known attacks – by “brute force” searches using Grover’s searching algorithm. All those algorithms require large-scale, fault-tolerant quantum machines, which are not yet available. Most of the expert community agree that they will likely become a reality within 10 to 20 years.

So take action: use QC safe cryptography now!


# Stan van der Linde

**Q-Rostering** problem: create a roster for each worker and check that all requirements are met.

QUBO -- Quadratic Unconstrained Binary Optimization

Workflow

1. Formulate problem
2. Create a Quadratic **Constrained** Binary Optimization
3. Classify constraints as *hard* and *soft*
4. Add constraints via penalty function to the objective function

