#probando PyQt

import sys
from tkinter import *
from tkinter import messagebox
from utils import Connection



class My_window:
	"""
	class My Window to sign up or login the first time that you use this program
	"""

	
	def ok_button(self):
		"""
		method to execute when the button Ok is pressed
		:return: 
		"""
		
		usr, pwd = self.are_input_correct()
		uid = None

		if not usr or not pwd:
			messagebox.showinfo('ERROR', 'Refill properly the fields')
			return

		if self.mode: 
			uid = self.login_select(usr, pwd)
		else: 
			num = self.signup_insert(usr, pwd)
			if num > 0:
				uid = self.login_select(usr, pwd)

		if uid is not None:
			messagebox.showinfo('holis', 'Has logeao HDP > {} < ¦ *{}* ¦ ID = "{}"'.format(usr, pwd, uid))
			self.parent.set_user_info(usr, pwd, uid)
			self.window.destroy()
		else:
			messagebox.showinfo('ERROR', 'Your user doesnt exist')
			self.window.destroy()


	def login_select(self, usr, pwd):
		"""
		method to search the user from the DB
		:param usr: username string
		:param pwd: password string
		:return: user id
		"""

		select = "select id from users where username = '{}' and password = '{}'".format(usr,pwd)
		
		conn = Connection.DataBase()
		try:
			conn.get_connection()

			data = conn.get_unique_id(select)
			
		finally: conn.close_connection()

		return data
		

	def signup_insert(self, usr, pwd):
		"""
		method to sign up a new user, in the DB
		:param usr: username 
		:param pwd: password of the user
		:return: number of rows inserted, it should be 1
		"""
		query = "insert into users(username, password) values('{}', '{}')".format(usr,pwd)
		num = 0
		conn = Connection.DataBase()
		try:
			conn.get_connection()

			num = conn.insert_into(query)
			
		finally: conn.close_connection()
		
		return num

	def are_input_correct(self):
		"""
		method to comprove the inputs, returning a tuple with the username and password
		:return: tuple (username, password)
		"""

		name_user = self.check_this_input(self.entrada_usr, 100)
		pass_user = self.check_this_input(self.entrada_pwd, 100)

		return name_user,pass_user

	def check_this_input(self, inp, max_len):
		"""
		auxiliar method to check the input data length
		:param inp: input box object
		:param max_len: length max
		:return: string with the content of the input, or None
		"""
		st = inp.get()
		st = st.strip()
		return st if len(st) > 0 and len(st) < max_len else None


	# atributes : window, parent, mode, entrada_usr entrada_pwd
	def __init__(self, parent, login = False):
		"""
		Constructor of My_window
		:param parent: the object that create the window
		:param login: boolean to know if it's a new user or a registered user
		"""
		#creamos ventana
		self.window = Tk()
		self.window.transient()
		self.parent = parent
		self.mode = login
		#tamanyo('ancho x alto + posx + posy')
		self.window.geometry('500x300+100+100')
		str_mode = 'Login' if self.mode else 'Sign Up'
		self.window.title(str_mode)

		#etiqueta grid(fila y columna)
		lbl_usr = Label(self.window, text='User: ').grid(row= 2, column =2, sticky=W)
		lbl_pwd = Label(self.window, text='Pass: ').grid(row=4, column=2, sticky=W)


		#txtfield
		self.entrada_usr = StringVar()
		self.entrada_pwd = StringVar()
		txt_usr = Entry(self.window, textvariable = self.entrada_usr).grid(row =2, column =3)
		txt_pwd = Entry(self.window, show = '*', textvariable = self.entrada_pwd).grid(row =4, column =3)



		bnt_login = Button(self.window, text=str_mode, width=10, command=self.ok_button).grid(row=10, column=2)




		#inicializamos el procesamiento - solo windows
		self.window.mainloop()



#end window