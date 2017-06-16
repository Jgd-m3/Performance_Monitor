import socket, psutil
from urllib.request import urlopen
from json import load
import pymysql
import ssl

# This restores the same behavior as before.
import ssl

# This restores the same behavior as before.

"""
a = psutil.disk_partitions()
arr = []
for i in a:
	if (i.opts).find('local') != -1:
		arr.append(i.mountpoint)
		print (i)

for j in arr:
	print(psutil.disk_usage(j))



b = psutil.disk_usage('/')
print ('nanana' + str(b))


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
context = ssl._create_unverified_context()
b =  load(urlopen('http://jsonip.com', context=context))['ip']

# print(type(load(urlopen('https://api.ipify.org?format=json'))['ip']))
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


con = pymysql.connect(host = '192.168.1.81', user='managex',
                    passwd ='M1dTYG73Fl', db = 'tfc_monitor')

cursor = con.cursor()
cursor.execute('select * from ram_stat')
for x in cursor.fetchall():
    print(x)


cursor.close()
con.close()
"""