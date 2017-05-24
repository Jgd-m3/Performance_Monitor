import socket, psutil
from urllib.request import urlopen
from json import load

import utils.Base_monitor as bs




"""
a = bs.Base(3)
print('aaaaaa')
id= a.get_data_id()
print(id)

if id is not None:
    a.update_pc(id)
else:
    a.register_pc()

"""
# result = a.update_pc(id)
""" ESTA ES LA BUSQUEDA DE LA IP PUBLICA Y EL NOMBRE DEL HOST(EQUIPO/USUARIO)
n = socket.gethostname()
direc = socket.gethostbyname(n)

print(n)
print(direc)
"""

b =  load(urlopen('http://jsonip.com'))['ip']

print(type(load(urlopen('http://jsonip.com'))['ip']))
print(b)

"""
def get_hd_size():
    rdo = 0
    for n in psutil.disk_partitions():
        if n[3].find('fixed') != -1:
            rdo += int(psutil.disk_usage(n[0]).total)
    return rdo

print(get_hd_size())
print(psutil.disk_usage('C:\\').total)

"""
