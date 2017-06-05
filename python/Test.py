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

class Test:

    def __init__(self):
        pass


    def start(self):

        win = Window.My_window(self, login= True)






Test().start()