from tkinter import Tk, messagebox
from identificator import Window
from utils import Connection, Encryptor
import time, base64


class Login:
	"""
	Class Login to get the user ID, name and pw and save it in a file
	"""

	def __init__(self, path):
		"""
		constructor
		:param path: 
		"""
		self.path = path
		self.usr = None
		self.pwd = None
		self.id = None


	def select_user(self,usr, pwd, id = None ):

		if usr and pwd and id:
			return id

		select = "select id, username, password from users where username = '{}'".format(usr)

		conn = Connection.DataBase()
		try:
			data = conn.get_data(select)
		finally:
			pass

		if len(data) == 0:
			return None

		crypt = Encryptor.Crypt()
		data = data[0]
		return data[0] if crypt.comprove(pwd, data[2]) else -2

	def signup_insert(self, usr, pwd):
		"""
		method to sign up a new user, in the DB
		:param usr: username 
		:param pwd: password of the user
		:return: number of rows inserted, it should be 1
		"""
		pwd = Encryptor.Crypt().encrypt(pwd)
		query = "insert into users(username, password) values('{}', '{}')".format(usr, pwd)
		num = 0
		conn = Connection.DataBase()
		try:
			num = conn.insert_into(query)
		finally:
			pass

		return num


	def register_user(self):

		while True:
			root = Tk()
			root.withdraw()
			answer = messagebox.askyesno('Question?', 'Have you got an Account??')
			root.destroy()

			time.sleep(0.2)
			Window.My_window(self, login = answer)

			idd = self.select_user(self.usr, self.pwd, self.id)
			if idd:
				break

		self._save_data(idd, self.usr, self.pwd)
		

	def _save_data(self, id, usr, pwd):

		with open(self.path, 'wb') as file_output:
			header = '[Cabesera Cabesona]:m3'.encode('utf-8')
			uid_bin = id.to_bytes(16, byteorder='big', signed=True)

			bin_name_array = bytearray(usr.encode('utf-8'))
			bin_pwd_array =  bytearray(pwd.encode('utf-8'))

			while (len(bin_name_array) < 128):
				bin_name_array.insert(0, ord('*'))

			while (len(bin_pwd_array) < 128):
				bin_pwd_array.insert(0, ord('x'))

			file_output.write(header)
			file_output.write(uid_bin)
			file_output.write(base64.encodebytes(bin_name_array))
			file_output.write(base64.encodebytes(bin_pwd_array))


	def set_user_info(self, usr, pwd, id):
		self.usr = usr
		self.pwd = pwd
		self.id = id