import bcrypt

class Crypt:
    """
    Util class to encrypt the password
    """
    def __init__(self):
        """
        constructor of the object
        """
        pass

    def encrypt(self, string):
        """
        method to encrypt the password
        :param string: password of the user
        :return: password encoded
        """
        psw = bcrypt.hashpw(string.encode('utf-8'), bcrypt.gensalt(4))
        return psw.decode('utf-8')


    def comprove(self, string, hash):
        """
        method to compare one password with another encrypted
        :param string: password inserted by the user
        :param hash: password encrypted from the DB
        :return: boolean if the passwords are the same
        """
        return bcrypt.checkpw(string.encode('utf-8'), hash.encode('utf-8'))
