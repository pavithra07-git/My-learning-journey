# bell_state_gates.py
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from qiskit import transpile

# 1. Initialize a Quantum Circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# 2. Apply a Hadamard gate (H) to qubit 0
# This puts qubit 0 into a superposition state
qc.h(0)

# 3. Apply a Controlled-NOT gate (CX)
# Qubit 0 is the control, Qubit 1 is the target. This creates entanglement.
qc.cx(0, 1)

# 4. Measure the qubits and map to classical bits
qc.measure([0, 1], [0, 1])

# Print the circuit diagram to the console
print("Quantum Circuit Diagram:")
print(qc.draw())

# 5. Simulate the circuit
backend = BasicSimulator()
t_qc = transpile(qc, backend)
job = backend.run(t_qc, shots=1000)
result = job.result()
counts = result.get_counts(qc)

print("\nMeasurement Results (1000 shots):")
print(counts)
