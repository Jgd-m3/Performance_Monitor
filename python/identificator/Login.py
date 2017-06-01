from tkinter import Tk, messagebox
from identificator import Window
import time, base64


class login():
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


	def select_user(self,usr, pwd, id):
		#TO-DO select to the DB to see if the user exists or you could insert it
		return id if usr and pwd and id else None


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