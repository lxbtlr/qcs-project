import numpy 
import qiskit
import matplotlib.pyplot 
import pandas
from datetime import datetime
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(instance="ibm-q/open/main")

TOKEN = ""

DATE = str(datetime.today())[:8].replace(":","-")

BACKENDS = ["ibm_kyiv","ibm_sherbrooke","ibm_brisbane"]

def get_backends():

    data = {}
    for be,c in enumerate(BACKENDS):
        backend = service.backend(be)

        fname = f"{backend.name[3:]}_{DATE}" 

        backend_data = ""
        for g in backend.properties.gates:
            backend_data = backend_data + f"{g.name},{g.qubits},{g.parameters[0].value},{g.parameters[0].unit},\n"
        data[fname] = backend_data
    return data


def get_device_info(backend):

    print(backend.name) 
    print(backend.coupling_map) # lets keep this incase we target other systems
    print(backend.processor_type) # same here
    print(backend.parametric_pulses) # same here
    pass

def save_data(data:dict):
    for name, val in data.items():

        with open(name+".csv", "w") as file:
            file.write(val)
    pass

def parse_data(data):
    pass

if __name__ == "__main__":
    
    data = get_backends()
    save_data(data)
