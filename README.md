# ⚛️ Quantum Computing Project – Bell State Simulation

## 📌 Overview

This project demonstrates the creation and simulation of a **Bell State** using Qiskit.

The Bell State is one of the most fundamental examples of **quantum entanglement**, a core concept in quantum computing and quantum information theory.

This implementation builds a quantum circuit, applies quantum gates, and simulates measurement outcomes using a quantum simulator.

---

## 🧠 Core Concepts Demonstrated

### 🔹 Superposition

Using the Hadamard Gate (H), a qubit initialized in state |0⟩ is transformed into superposition state:

\[
\frac{1}{\sqrt{2}} (|0⟩ + |1⟩)
\]

This places the qubit into a probabilistic combination of both states simultaneously.

---

### 🔹 Entanglement

Applying a Controlled-NOT (CNOT / CX) gate entangles the two qubits, producing the Bell State:

\[
\frac{1}{\sqrt{2}} (|00⟩ + |11⟩)
\]

This means:

- Measuring one qubit instantly determines the state of the other.
- The two qubits behave as a single correlated quantum system.

---

### 🔹 Quantum Measurement

When measured over 1000 simulation shots, the expected output distribution is approximately:

```python
{'00': ~500, '11': ~500}
```

The outcomes `01` and `10` never appear due to entanglement correlations.

---

## 🧾 Code Explanation (bell_state_gates.py)

### 1️⃣ Circuit Initialization

```python
qc = QuantumCircuit(2, 2)
```

Creates:
- 2 quantum bits
- 2 classical bits for storing measurement results

---

### 2️⃣ Superposition Creation

```python
qc.h(0)
```

Applies the Hadamard gate to qubit 0, placing it into superposition.

---

### 3️⃣ Entanglement

```python
qc.cx(0, 1)
```

- Qubit 0 → Control  
- Qubit 1 → Target  

This operation entangles the two qubits.

---

### 4️⃣ Measurement

```python
qc.measure([0, 1], [0, 1])
```

Maps quantum states to classical bits.

---

### 5️⃣ Simulation

The circuit is:

- Transpiled for the backend
- Executed using a simulator
- Run for 1000 shots

---

## 🛠 Tech Stack

- Python 3.x
- Qiskit
- BasicSimulator Backend

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/pavithra07-git/My-Learning-joruney.git
cd your-repo-name
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Program

```bash
python bell_state_gates.py
```

You will see:

- The quantum circuit printed in the console
- Measurement results from simulation

---

## 🎯 Learning Outcomes

Through this project, I strengthened my understanding of:

- Quantum Superposition
- Quantum Gate Operations
- Entanglement Mechanics
- Quantum Measurement Collapse
- Circuit Simulation in Qiskit

---

## 🚀 Future Enhancements

Planned next steps:

- Visualizing state vectors
- Bloch sphere representation
- Multi-qubit entangled states
- Quantum teleportation simulation
- Running on real quantum hardware

---

## 🌌 About This Repository

This project is part of my structured journey into Quantum Computing.

I am actively exploring:

- Quantum algorithms
- Quantum information theory
- Hybrid classical–quantum systems

⚛️ This repository represents foundational experimentation toward advanced quantum applications.
