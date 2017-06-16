"""
from identificator.Login import Login
import bcrypt
from utils import Encryptor as encr

blabla = encr.Crypt().encrypt('nanana')

nene = encr.Crypt().comprove('nanana', blabla)
print(nene)
print(blabla)

"""

from identificator import Window
import psutil as ps
from urllib.request import urlopen
from json import load
import ssl
from tkinter import Tk, messagebox
class Test:

    def __init__(self):
        pass


    def start(self):
        # lalala = ps.virtual_memory().total
        # print('mio------------------')
        # print (lalala)
        # print(str(round(lalala/2**30,2))+"GB")
        #
        # ram_bacho = 8452886528
        # hd_b = 999625322496
        # print('bacho ------------------')
        # print(ram_bacho)
        # print('ram bacho: {}GB / HD : {}GB'.format(round(ram_bacho/(2**30),2),round(hd_b/2**30,2)))
        win = Window.My_window(self, login= True)

        # context = ssl._create_unverified_context()
        #
        # try:
        #     self.ip_pub = load(urlopen('http://jsonip.com', context=context))['ip']
        # except:
        #     self.ip_pub = 'xxx.xxx.xxx.xxx'
        # print(self.ip_pub)

Test().start()