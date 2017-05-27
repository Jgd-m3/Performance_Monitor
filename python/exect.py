import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

setup ( name = 'monitor',
        version = '0.03',
        description = 'Program to do the monitorization of the performance of a computer',
        executables = [Executable('Main.py')],)