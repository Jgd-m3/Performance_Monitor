#!/usr/bin/env python3

## script de testeo   -  TO-DELETE

import psutil, codecs, platform, pymysql, time
import urllib.request
import Connection

conn= Connection.DataBase()
nana = conn.get_unique_id("select type_net from net_details_stat where ref_pc = 11 and type_net = 'isatap.{F454A02B-F3EE-4D03-9F36-B5FDFF922974}'")

print(nana)

"""
nanana = codecs.open('rdo_net.txt', 'a', 'utf-8')
# nanana.write(codecs.BOM_UTF8)


count1 = psutil.net_io_counters()
print(count1)
nanana.write('METHOD: net_io_counters(False) ------------------------ \n')
nanana.write('{}\n\n'.format(count1))
print('--------------------')


counters = psutil.net_io_counters(True) #if True es de cada red
nanana.write('METHOD: net_io_counters(True) ------------------------ \n')
for x in counters:
    nanana.write('{}\n'.format(x))
    nanana.write('\t{}\n'.format(counters[x]))

print ('--------------------------------')
print('\n')

"""
"""
connections = psutil.net_if_addrs()
nanana.write('\nMETHOD: net_if_addrs() ----------------------------\n')
for i in connections:
    nanana.write('{}\n'.format(i))
    for y in connections[i]:
        nanana.write('\t - {}\n'.format(y))
    # print(connections[i])

items = psutil.net_if_addrs().items()
for z in items:
    print(z)

stats = psutil.net_if_stats() #NO SABES NI LO QUE ES...
for i in stats:
    print(i)
    print(stats[i])

print('--------------------')

lala = psutil.net_connections('inet4')

for y in lala:
    print(y)

"""
# print(platform.processor()) # tipo de procesador
# print(platform.machine()) # tipo maquina
# print(platform.architecture())
# print(platform.system())
# print(platform.version())
# print(platform.platform())
# print(platform.release())
# print(platform.uname())


"""
conn = pymysql.connect(
    host = 'iesmaestre.sytes.net', user='monitor',
    passwd ='TFC_Monitor_2017!', db ='tfc_monitor'
)

# cursor = conn.cursor()
#
# cursor.execute(
#     "insert into pcs(ref_user, mac) values(-1, 'MAC_TRY_1')"
# )

# conn.commit()
conn.close()
print('finish')

i = 0
print(0)
i +=1
a = ['akunnaMatata']
for i in range(i,4):
    a.append('akunnaMatata')

print( ",".join(a))


print (time.strftime("%Y/%m/%d %H:%M:%S").__class__)


print(psutil.disk_partitions(True))


print('c: - {}'.format(psutil.disk_usage('c:\\')))
print('d: - {}'.format(psutil.disk_usage('d:\\')))
"""

print('.................................')
"""
 con = pymysql.connect(host = 'iesmaestre.sytes.net', user='monitor',
                    passwd ='TFC_Monitor_2017!', db = 'tfc_monitor')


con = pymysql.connect(host = '127.0.0.1', user='managex1',
                    passwd ='M1dTYG73Fl', db = 'tfc_monitor')
cursor = con.cursor()
cursor.execute('select * from ram_stat')
for x in cursor.fetchall():
    print(x)


cursor.close()
con.close()



cosa = psutil.process_iter()

print(cosa.__str__())

for i in cosa:
    print(i.name())
"""


#WRITING THE FILE
import base64

nana = open('testbyte.aa', 'wb')

cabesera = '[Cabesera Cabesona]:m3'.encode('utf-8')
print(len(cabesera))


uid = 15

uid_bin = uid.to_bytes(16, byteorder='big', signed=True) #tamaño de la cantidad de bytes(16 en el que codificamos un numero)


name = 'nombresito'
bin_name = name.encode('utf-8')
bin_name_array =bytearray(bin_name)

while( len(bin_name_array)< 200):
    bin_name_array.insert(0, ord('*'))


password = 'paszzZZZzZzzzzworsitomio!!AAA'
bin_pwd = password.encode('utf-8')
bin_pwd_array = bytearray(bin_pwd)


while(len(bin_pwd_array) < 128):
    bin_pwd_array.insert(0, ord('X'))
"""
nana.write(cabesera)
nana.write(uid_bin)
nana.write(bin_name_array)
"""

code64  = base64.encodebytes(bin_pwd_array)

print(len(bin_pwd_array))
print(len(code64))

nana.write(code64)
nana.close()
#READING FILE:

nanana = open('testbyte.aa', 'rb')
st = nanana.read(203)
print(base64.decodebytes(st).decode('utf-8').strip('X'))
nanana.close()
"""
#cabesera size = 22
nanana.seek(0)
cabesera = nanana.read(22)

print(cabesera.decode('utf-8'))
uid = nanana.read(16)
recovered_uid= int.from_bytes(uid, byteorder='big', signed=True)
print(recovered_uid)
# nanana.seek(38)
user = nanana.read(200)
print(user.decode('utf-8').strip('*'))
pwd = nanana.read(200)
print(pwd.decode('utf-8').strip('X'))

nanana.close()

recovered_uid= int.from_bytes(uid_bin, byteorder='big', signed=True) #decodificacion de los bytes en integer
print(recovered_uid)

print(bin_array)
text = bin_array.decode('utf-8').strip()
print(text)
"""