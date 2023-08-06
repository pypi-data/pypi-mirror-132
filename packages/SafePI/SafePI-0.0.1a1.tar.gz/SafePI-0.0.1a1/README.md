#  SafePI

A PyPi package to demonstrate Python code distribution in a safe and automated way

## Steps
1. Make a package with file structure like this demo package
2. The src folder contains source code of the normal Python package project
3. The src/libs contains necessary *.pyd(*.so) files
4. The `libs_root.py` must be included at the head of py files where some pyd module is called.
5. The `src_cython` folder is the Cython files needed to protect and compile as pyd files.
6. The `build_pakcage.py` in the root and `build_cython_libs.py` in the src_cython are automated scripts respectively. 
7. Please see examples folder to see how to test a function from the PyPI package where the code is compiled and protected.

## Functions

You cannot find the source code of *Person.py* in this package, which prevents code theft.

```python
from safepi.World import greet_times
# This function's algorithm is within a .pyd (.so in Linux) file compiled by Cython. 
# The source code cannot be found in the package and is therefore protected.
greet_times(n=5)
```

`build_package.py`: rapidly build Cython files, PyPI package and upload the package to PyPI website quickly. (your upload token is required!)

`src_cython/build_cython_libs.py`: Rapidly build Cython files and deploy all `*.pyd` files to to `src/libs' folder

## License
The `SafePI` project is provided by [Donghua Chen](https://github.com/dhchenx/umls-graph). 
