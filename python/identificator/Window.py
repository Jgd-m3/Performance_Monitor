#probando PyQt

import sys
from tkinter import *
from tkinter import messagebox
from utils import Connection



class My_window:

	#definir la funcion que llamaremos
	def ok_button(self):
		#TO-DO EVERYTHING TO LOGIN THE USR
		
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
		#pwd sera last_name en la bbdd del curro
		select = "select id from users where nick = '{}' and pass = '{}'".format(usr,pwd)
		
		conn = Connection.DataBase()
		try:
			conn.get_connection()

			data = conn.get_unique_id(select)
			
		finally: conn.close_connection()

		return data
		

	def signup_insert(self, usr, pwd):
		query = "insert into users(nick, pass) values('{}', '{}')".format(usr,pwd)
		num = 0
		conn = Connection.DataBase()
		try:
			conn.get_connection()

			num = conn.insert_into(query)
			
		finally: conn.close_connection()
		
		return num

	def are_input_correct(self):
		name_user = self.check_this_input(self.entrada_usr, 100)
		pass_user = self.check_this_input(self.entrada_pwd, 100)

		return name_user,pass_user

	def check_this_input(self, inp, max_len):
		st = inp.get()
		st = st.strip()
		return st if len(st) > 0 and len(st) < max_len else None


	# atributes : window, parent, mode, entrada_usr entrada_pwd
	def __init__(self, parent, login = False):
		#creamos ventana
		self.window = Tk()
		self.parent = parent
		self.mode = login
		#tamanyo('ancho x alto + posx + posy')
		self.window.geometry('500x300+100+100')
		str_mode = 'Login' if self.mode else 'Sign Up'
		self.window.title(str_mode)

		#etiqueta grid(fila y columna)
		lbl_usr = Label(self.window, text='Usuario: ').grid(row= 2, column =2, sticky=W)
		lbl_pwd = Label(self.window, text='Password: ').grid(row=4, column=2, sticky=W)


		#txtfield
		self.entrada_usr = StringVar()
		self.entrada_pwd = StringVar()
		txt_usr = Entry(self.window, textvariable = self.entrada_usr).grid(row =2, column =3)
		txt_pwd = Entry(self.window, show = '*', textvariable = self.entrada_pwd).grid(row =4, column =3)



		bnt_login = Button(self.window, text=str_mode, width=10, command=self.ok_button).grid(row=10, column=2)




		#inicializamos el procesamiento - solo windows
		self.window.mainloop()



#end window