from identificator.Login import Login
import bcrypt
from utils import Encryptor

log = Login('nana.m3')

blabla = bcrypt.hashpw(b'jijiji', bcrypt.gensalt(8))

bleble = bcrypt.hashpw(b'jijiji', bcrypt.gensalt(8))

print(bcrypt.checkpw(b'jijiji', bleble))

print(Encryptor.Crypt().comprove('jijiji', blabla.decode('utf-8')))


