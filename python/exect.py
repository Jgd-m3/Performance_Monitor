#!/usr/bin/env python3

import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

includes = []
include_files = [r"C:\Program Files\Python36\DLLs\tcl86t.dll", \
                 r"C:\Program Files\Python36\DLLs\tk86t.dll"]

setup(name='monitor',
      version='0.03',
      description='Program to do the monitorization of the performance of a computer',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=[Executable('Main.py')], )