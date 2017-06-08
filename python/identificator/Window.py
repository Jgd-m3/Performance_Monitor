#probando PyQt

import sys
from tkinter import *
from tkinter import messagebox


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
			uid = self.parent.select_user(usr, pwd)
		else: 
			num = self.parent.signup_insert(usr, pwd)
			if num > 0:
				uid = self.parent.select_user(usr, pwd)
			else:
				uid = -3

		if uid is None:
			messagebox.showinfo('ERROR', 'Your user doesnt exist')
			self.window.destroy()
		elif uid == -2:
			messagebox.showinfo('ERROR', 'That password is incorrect')
			self._clean_inputs()
		elif uid == -3:
			messagebox.showinfo('ERROR', 'That user is already registered')
			self._clean_inputs(True)
		else:
			messagebox.showinfo('holis', 'Has logeao HDP > {} < '.format(usr))
			self.parent.set_user_info(usr, pwd, uid)
			self.window.destroy()


	def are_input_correct(self):
		"""
		method to comprove the inputs, returning a tuple with the username and password
		:return: tuple (username, password)
		"""

		name_user = self.check_this_input(self.entrada_usr, 100)
		pass_user = self.check_this_input(self.entrada_pwd, 72)

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

	def _clean_inputs(self, nanana = False):
		"""
		Method to clean the pass field or both fields of the Window
		:param nanana: boolean to indicate if the username field needs be cleaned or not
		"""
		if nanana:
			self.txt_usr.delete(0,END)
		self.txt_pwd.delete(0, END)

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
		self.window.geometry('500x300+300+300')
		str_mode = 'Login' if self.mode else 'Sign Up'
		self.window.title(str_mode)
		self.window.config(bg='black')

		
		pic = PhotoImage(file='SM.gif')
		lbl_pic = Label(self.window, image=pic)
		lbl_pic.photo = pic
		lbl_pic.pack()
		
		#etiqueta grid(fila y columna)
		lbl_usr = Label(self.window, text='User: ', bg='black', fg='white').grid(row= 2, column =2, sticky=W)
		lbl_pwd = Label(self.window, text='Pass: ', bg='black', fg='white').grid(row=4, column=2, sticky=W)

		#txtfield
		self.entrada_usr = StringVar()
		self.entrada_pwd = StringVar()
		self.txt_usr = Entry(self.window, textvariable = self.entrada_usr)
		self.txt_pwd = Entry(self.window, show = '*', textvariable = self.entrada_pwd)
		self.txt_usr.grid(row =2, column =3)
		self.txt_pwd.grid(row =4, column =3)

		bnt_login = Button(self.window, text=str_mode, width=10, command=self.ok_button).grid(row=10, column=2)

		self.window.mainloop()

#end window