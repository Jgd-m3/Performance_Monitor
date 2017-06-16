#probando PyQt

import sys
from tkinter import *
from tkinter import messagebox
from tkinter import font


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
			messagebox.showinfo('ERROR', 'Your user doesn`t exist')
			self.window.destroy()
		elif uid == -2:
			messagebox.showinfo('ERROR', 'That password is incorrect')
			self._clean_inputs()
		elif uid == -3:
			messagebox.showinfo('ERROR', 'That user is already registered')
			self._clean_inputs(True)
		else:
			messagebox.showinfo('SUCCESS', 'Login Success {}'.format(usr))
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
		self.window.resizable(FALSE, FALSE)
		self.parent = parent
		
		self.mode = login
		#tamanyo('ancho x alto + posx + posy')
		self.window.geometry('600x500+300+200')
		str_mode = 'Login' if self.mode else 'Sign Up'
		self.window.title('Smart Monitor')
		self.window.config(bg='#000', padx=25, pady=25)

		try:
			pic = PhotoImage(file='./assets/SML.png')
		except:
			pic = PhotoImage(file='./assets/SML.gif')

		# lbl_pic = Label(self.window, image=pic)
		# lbl_pic.photo = pic
		# lbl_pic.pack()
		container= Label(self.window, height=200, bg='#e6324b')
		photo = Label(container, height=180, width=200, image=pic, bg='#000').pack()
		container.place(x=200, y=10)
		container.pack()
		# photo.replace()
		helvfont = font.Font(family="Helvetica", size=10, weight="bold")
		title = Label(self.window, font=helvfont, text=str_mode.upper(), width=19, bg='#000' , fg='#e6324b').place(x=180, y=225)
		#etiqueta grid(fila y columna)
		lbl_usr = Label(self.window, text='User: ', bg='#000', font=helvfont, fg='#e6324b').place(x=125, y=280)
		lbl_pwd = Label(self.window, text='Pass: ', bg='#000', font=helvfont, fg='#e6324b').place(x=125, y=320)


		#txtfield
		self.entrada_usr = StringVar()
		self.entrada_pwd = StringVar()
		self.txt_usr = Entry(self.window, textvariable = self.entrada_usr)
		self.txt_pwd = Entry(self.window, show = '*', textvariable = self.entrada_pwd)
		self.txt_usr.place(x=220, y=280)
		self.txt_pwd.place(x=220, y=320)
		bnt_login = Button(self.window, text=str_mode, font=helvfont, width=19, command=self.ok_button,fg='#fff', bg='#e6324b').place(x=180, y=390)

		self.window.mainloop()

#end window