#Packages
import tkinter as tk
import tkinter.messagebox as msg
import pickle
import xlrd # prerequisite of pandas
import pandas as pd
import tkinter.ttk as ttk

# Local Support
import functionals as fun
from Operator import *
from Log import *
from Base import *

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PRTS")
        self.geometry("900x450")

        #Elite level
        self.lb_pro = tk.Label(self, text="Elite")
        self.lb_pro.place(x=30, y=120)

        #Initial Level
        self.lb_leveli = tk.Label(self, text="Initial Level")
        self.lb_leveli.place(x=30, y=150)
        self.e_leveli = tk.Entry(self, width=10)
        self.e_leveli.place(x=150, y=150)

        #Final Level
        self.lb_levelf = tk.Label(self, text="Final Level")
        self.lb_levelf.place(x=30, y=180)
        self.e_levelf = tk.Entry(self, width=10)
        self.e_levelf.place(x=150, y=180)

        #Developers
        self.lb_developer = tk.Label(self, text="Developers: Henry Ouyang, Scott Xu")
        self.lb_developer.place(x=675, y=420)

        #Background
        canvas = tk.Canvas(self, bg='blue', height=300, width=400)
        image_file = tk.PhotoImage(file='timg.gif')
        image = canvas.create_image(200, 150, image=image_file)
        canvas.place(x=450, y=110)

        #EXP and LMD
        self.exp_sum = tk.IntVar()
        self.lmd_sum = tk.IntVar()

        self.lb_exp = tk.Label(self, height=1, width=12, text='EXP')
        self.lb_exp.place(x=320, y=160)

        self.lb_lmd = tk.Label(self, height=1, width=12, text='LMD')
        self.lb_lmd.place(x=320, y=180)

        self.b_exp = tk.Button(self, text='Calculate', command=self.cal_explmd) # (ERROR)command not defined
        self.b_exp.place(x=320, y=120)

        #Elite
        self.promotion_rb=tk.IntVar()
        self.rb_pro0 = tk.Radiobutton(self, text='0', variable=self.promotion_rb, value='0')
        self.rb_pro0.place(x=150, y=120)
        self.rb_pro1 = tk.Radiobutton(self, text='1', variable=self.promotion_rb, value='1')
        self.rb_pro1.place(x=200, y=120)
        self.rb_pro2 = tk.Radiobutton(self, text='2', variable=self.promotion_rb, value='2')
        self.rb_pro2.place(x=250, y=120)

        #Menu
        self.menubar = tk.Menu(self)
        self.openmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=self.openmenu)
        self.openmenu.add_command(label='Operator', command=self.new_operator)
        self.openmenu.add_command(label='Log', command=self.new_log)
        self.openmenu.add_command(label='Base', command=self.new_base)
        self.openmenu.add_separator()
        self.openmenu.add_command(label='Exit',command=self.exit_window)

        self.searchmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Search', menu=self.searchmenu)
        self.searchmenu.add_command(label='Operator')
        self.searchmenu.add_command(label='Wears')
        self.searchmenu.add_command(label='Materials')

        self.config(menu=self.menubar)

    def exit_window(self):
        exit_flag = msg.askyesno(title='Exit Program', message='Are you sure you want to exit PRTS?')
        if exit_flag == 1:
            self.destroy()

    def cal_explmd(self):
        flag = 0
        try:
            var_leveli = int(self.e_leveli.get())
            var_levelf = int(self.e_levelf.get())
            flag = 1
        except Exception as e:
            msg.showwarning(title='Input Error', message='Please complete your input.')
            flag = 0
        promotion_stage = self.promotion_rb.get()
        if flag == 1:
            if  var_leveli <= var_levelf:
                try:
                    self.lb_exp.configure(text='EXP = '+str(fun.exp_needed(var_leveli, var_levelf, promotion_stage)))
                    self.lb_lmd.configure(text='LMD = '+str(fun.lmd_needed(var_leveli, var_levelf, promotion_stage)))
                except Exception as e:
                    if promotion_stage == 0:
                        msg.showwarning(title='Input Error', message='Please enter integers between 1 and 50.')
                    if promotion_stage == 1:
                        msg.showwarning(title='Input Error', message='Please enter integers between 1 and 70.')
                    if promotion_stage == 2:
                        msg.showwarning(title='Input Error', message='Please enter an integer between 1 and 90.')
                    else:
                        msg.showwarning(title='Input Error', message='The initial level should be less than the final level.')
        

    def new_operator(self):
        op = Operator(self)
        self.wait_window(op)
        return

    def new_log(self):
        log = Log(self)
        self.wait_window(log)
        return

    def new_base(self):
        base = Base(self)
        self.wait_window(base)
        return

if __name__ == '__main__':
    main_app = MainApp()
    main_app.mainloop()

