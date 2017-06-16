from uuid import getnode as get_mac
import psutil, socket, platform, ssl
from psutil import cpu_count as num_cpus
from urllib.request import urlopen
from json import load
from utils import Connection

class Base:

    def register_pc(self ):
        """
        Method to register the pc
        :return: id of pc
        """
        
        conn = Connection.DataBase()

        sql = "Insert into pcs(ref_user, mac, pc_name) values({},'{}', '{}')".format(self.num_user, self.mac,
                                                                                     self.pc_name)

        conn.insert_into(sql)
       
        sql = "select id from pcs where ref_user={} and mac = '{}' and pc_name = '{}'".format(
                                                                                    self.num_user, self.mac, self.pc_name)
        rlt = conn.get_unique_id(sql)

        sql = "INSERT INTO pc_data VALUES({}, {},'{}',{},{},'{}','{}', {}, '{}','{}')".format(
                rlt, self.memory, self.cpu_name, self.cores, self.threads, self.so, self.so_name,
                self.hdd, self.ip_priv, self.ip_pub)
        conn.insert_into(sql)


        return rlt

    def update_pc(self, n_pc):
        """
        Method to update the pc Data
        :param n_pc: id of pc
        :return: 
        """
        conn = Connection.DataBase()

        sql = "UPDATE pc_data SET "
        sql += "ram = {}, cpu_name = '{}', cores = {}, threads = {}, so = '{}', so_v = '{}',".format(
            self.memory, self.cpu_name, self.cores, self.threads, self.so, self.so_name)
        sql += " hdd= {}, ip_priv='{}', ip_pub = '{}'".format(
            self.hdd, self.ip_priv, self.ip_pub)
        sql += 'where ref_pc = {}'.format(n_pc)
        conn.insert_into(sql)


    def __init__(self, num_user):
        """
        Constructor of the object Base
        :param num_user: Id of user
        """
        self.num_user = num_user
        self.cores = num_cpus(False)
        self.threads = num_cpus()
        self.pc_name = socket.gethostname()
        self.ip_priv = socket.gethostbyname(self.pc_name)
        self.so = platform.system()
        if self.so is None or self.so == '':
            self.so = self.get_so()

        self.memory = psutil.virtual_memory().total
        self.cpu_name = platform.processor()
        self.so_name = platform.platform()
        self.hdd = self.get_hd_size()
        self.mac = self.get_mac_format(hex(get_mac()))
        context = ssl._create_unverified_context()
        try:
            self.ip_pub = load(urlopen('http://jsonip.com', context=context))['ip']
        except:
            self.ip_pub = 'xxx.xxx.xxx.xxx'


    def get_data_id(self):
        """
        Method to get the id of the pc
        :return: id of pc
        """
        sql = "select id from pcs where ref_user = {} and mac = '{}' and pc_name = '{}'".format(self.num_user,
                                                                                self.mac, self.pc_name )

        conn = Connection.DataBase()

        id_pc = conn.get_unique_id(sql)
        return id_pc

    def get_hd_size(self):
        """
        method to get the total HD size
        :return: size of HD in bytes
        """
        rdo = 0
        for n in psutil.disk_partitions():
            if (n.opts).find('fixed') != -1 or (n.opts).find('local') != -1:

                rdo += int(psutil.disk_usage(n.mountpoint.replace('\\','/')).total)
        return rdo

    def get_mac_format(self, input):
        """
        method to get the mac address with legible format
        :param input: mac
        :return: mac in hex
        """
        input = input[2:].upper()
        n = []

        for i in range(len(input)):
            if i % 2 == 0:
                n.append('-')
            n.append(input[i:i + 1])

        return ''.join(n)[1:]

    def get_so(self):
        """
        method to get the SO's name
        :return: name of SO
        """
        if psutil.WINDOWS:
            return 'Windows'
        elif psutil.LINUX:
            return 'Linux'
        elif psutil.OSX:
            return 'OSX'
        elif psutil.BSD:
            return 'BSD'
        elif psutil.FREEBSD:
            return 'FreeBDS'
        elif psutil.OPENBSD:
            return 'OPENBSD'
        elif psutil.SUNOS:
            return 'SunOS'
        else:
            return 'Other OS'

