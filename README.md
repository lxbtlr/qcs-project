# TODO:
- [ ] Make simple database of error data across all backends 
- [ ] Create shared representation from qmetal output to hotspot input
    - [ ] try not to make a full parser for this
- [ ] look for simpliest implementation of workflow


## Reconciling Quantum system decay 
Using class simulation tooling to augment Mapomatic error mapping passes.

### high-level 
- Qiskit Metal, generate device file (gds>?)
- HotSpot, implement device thermal simulation
    - Model dilution env.
    - Generate a steady state temperature


# NOTES:
## MAPOTMATIC:

### Cost function / Error Representations

[default cost function](https://github.com/qiskit-community/mapomatic/blob/bd8e5d7254dadaed2f576143acbd62cae138578d/mapomatic/layouts.py#L215-L250)

### [Get Error Information](https://github.com/Qiskit/qiskit/blob/ff15ce40479324449ec8ad8205c90d2a7b02fb11/qiskit/visualization/gate_map.py#L1385C9-L1432C21)(implemented in `qiskit.visualization.gate\_map.py`)

## QISKIT METAL
- [ ] Get pyaedt working
- [ ] find a way to use the gui over vnc

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

- [x] learn how to run a steady state simulation in hotspot so we can pipe that into the init file
    - Throw a `-steady_file <fname>` onto the `run.sh`
- [ ] Figure out a clean way to translate qmetal to hotspot


### Examples explained
># Example 1
>This is a simulation of running gcc on a floorplan similar to an Alpha EV6 processor using HotSpot's block model.
># Example 2
>This is the same simulation as Example 1, except we use HotSpot's grid model instead.
># Example 3
>In this example, we run a simple 3D simulation. We also demonstrate in this simulation how some of HotSpot's included scripts can be used to generate heat maps.

### [Layer configuration file \*.lcf](https://github.com/uvahotspot/HotSpot/wiki/File-Types#layer-configuration-file-lcfhttps://github.com/uvahotspot/HotSpot/wiki/File-Types#layer-configuration-file-lcfhttps://github.com/uvahotspot/HotSpot/wiki/File-Types#layer-configuration-file-lcfhttps://github.com/uvahotspot/HotSpot/wiki/File-Types#layer-configuration-file-lcfhttps://github.com/uvahotspot/HotSpot/wiki/File-Types#layer-configuration-file-lcfhttps://github.com/uvahotspot/HotSpot/wiki/File-Types#layer-configuration-file-lcf)
#### default
> Without a layer configuration file, HOTSPOT models the input chip as four layers: 
> - a user-specified layer described by a floor plan
> - a thermal interface material
> - a heat spreader layer
> - and a heat sink layer

**if layer conf specified, layers ordered top to bottom**
>  "list each layer in order from the topmost layer (the layer adjacent to the heat spreader) to the bottommost layer (the layer farthest from the heat spreader)."

### [Floorplan file \*.flp](https://github.com/uvahotspot/HotSpot/wiki/File-Types#floorplan-files-flp)

### [Power Trace File \*.ptrace](https://github.com/uvahotspot/HotSpot/wiki/File-Types#power-trace-file-ptrace)

### [Materials file \*.materials](https://github.com/uvahotspot/HotSpot/wiki/File-Types#materials-file-materials)




