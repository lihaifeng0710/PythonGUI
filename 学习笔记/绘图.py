from qiskit import *
# For Jupyter Notebooks:%config InlineBackend.figure_format = 'svg' # Makes the images look nice
qc = QuantumCircuit()
qr = QuantumRegister(2,'qreg')
qc.add_register( qr )
qc.h(qr[0])
qc.cx(qr[0], qr[1])


