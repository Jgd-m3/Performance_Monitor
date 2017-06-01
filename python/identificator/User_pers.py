#test guardar usuario en archivo .txt
import os.path as path, base64
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
			log = Login.login(self.file_string)
			log.register_user()

		with open(self.file_string, 'rb') as file_input:
			# file_input.seek(0)
			# header = file_input.read(22)    # I don't use the header yet
			file_input.seek(22)

			uid = file_input.read(16)
			recovered_uid = int.from_bytes(uid, byteorder='big', signed=True)

			user = base64.decodebytes(file_input.read(175))
			usr_decode = user.decode('utf-8').strip('*')
			pwd = base64.decodebytes(file_input.read(175))
			pwd_decode = pwd.decode('utf-8').strip('x')

		print('id:{}\nuser:{}\npass:{}'.format(recovered_uid,usr_decode,pwd_decode))

		return recovered_uid


	def __init__(self, path):
		"""
		Constructor of the User object
		:param path: path of the file to load the data
		"""
		self.file_string = path










