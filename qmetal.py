import qiskit_metal as metal
from qiskit_metal import designs, draw
from qiskit_metal.qlibrary.qubits.transmon_cross import TransmonCross


design = designs.DesignPlanar()
print(TransmonCross.get_template_options(design))
