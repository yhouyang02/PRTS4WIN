import tkinter as tk

class Base(tk.Toplevel):
	def __init__(self, parent):
		super().__init__()
		self.parent = parent
		self.title("New Base")
		self.geometry("900x450")
		button_exit_newop = tk.Button(self, text='Save', command=self.exit_new_base)
		button_exit_newop.pack()
		
	def exit_new_base(self):
		self.destroy()