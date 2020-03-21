import tkinter as tk

class Log(tk.Toplevel):
	def __init__(self, parent):
		super().__init__()
		self.parent = parent
		self.title("New Log")
		self.geometry("900x450")
		button_exit_newop = tk.Button(self, text='Save', command=self.exit_new_log)
		button_exit_newop.pack()
		
	def exit_new_log(self):
		self.destroy()