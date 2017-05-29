#test guardar usuario en archivo .txt
import os.path as path
from identificator import Login

class User:

	def give_me_uid(self):

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
		self.file_string = path










