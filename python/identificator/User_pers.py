#test guardar usuario en archivo .txt
import os.path as path
from identificator import Login

class User:
	"""
	Class to retrieve the information of the user. If the user is saved it load directly.
	if not, it open the registration/login user (this only should happen the first time you use the program)
	"""

	def get_uid(self):
		"""
		Method to get the user ID
		:return: user ID
		"""

		if not path.exists(self.file_string):
			nana = Login.login(self.file_string)
			nana.register_user()

		data =[]

		with open(self.file_string, 'r') as file_input:

			for i, line in enumerate(file_input):
				if i == 0:
					print('la cabecera es: {}'.format(line))
				if i == 1:
					data.append(int(line))
				if i == 2 or i == 3:
					data.append(str(line).strip())

		print('id:{}\nuser:{}\npass:{}'.format(data[0],data[1],data[2]))

		return int(data[0])

	def __init__(self, path):
		"""
		Constructor of the User object
		:param path: path of the file to load the data
		"""
		self.file_string = path










