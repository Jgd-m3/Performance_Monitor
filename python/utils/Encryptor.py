import bcrypt

class Crypt:

    def __init__(self):
        pass

    def encrypt(self, string):
        psw = bcrypt.hashpw(string.encode('utf-8'), bcrypt.gensalt(4))
        return psw.decode('utf-8')


    def comprove(self, string, hash):
        return bcrypt.checkpw(string.encode('utf-8'), hash.encode('utf-8'))
