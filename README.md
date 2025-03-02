## Reconciling Quantum system decay 
Using class simulation tooling to augment Mapomatic error mapping passes.

### high-level 
- Qiskit Metal, generate device file (gds>?)
- HotSpot, implement device thermal simulation
    - Model dilution env.
    - Generate a steady state temperature


# NOTES:
## QISKIT METAL
I have had some much trouble getting this library to work:
### pyaedt 
(python ansys lib) would not build but using
```bash
$ mkdir wheel
$ cd wheel && wget https://github.com/ansys/pyaedt/releases/download/v0.6.46/PyAEDT-v0.6.46-wheelhouse-Linux-3.10.zip
$ unzip PyAEDT-v0.6.46-wheelhouse-Linux-3.10.zip  
```
followed by a:
```
$ pip install --no-cache-dir --no-index --find-links=/pool/alexb/qcs/wheel/  pyaedt==0.6.46
```
fixed this issue.

## HOTSPOT
># Example 1
>This is a simulation of running gcc on a floorplan similar to an Alpha EV6 processor using HotSpot's block model.
># Example 2
>This is the same simulation as Example 1, except we use HotSpot's grid model instead.
># Example 3
>In this example, we run a simple 3D simulation. We also demonstrate in this simulation how some of HotSpot's included scripts can be used to generate heat maps.
