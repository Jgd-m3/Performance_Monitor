## script de testeo   -  TO-DELETE

import psutil, codecs, platform, pymysql, time
import urllib.request
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
print(platform.processor()) # tipo de procesador
# print(platform.machine()) # tipo maquina
# print(platform.architecture())
print(platform.system())
# print(platform.version())
print(platform.platform())
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
"""


cosa = psutil.process_iter()

print(cosa.__str__())

for i in cosa:
    print(i.name())
