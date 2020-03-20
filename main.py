'''
Project PRTS
Last Update: 20/03/18 03:00
'''

#Packages
import tkinter as tk
import tkinter.messagebox
import pickle
import xlrd # prerequisite of pandas
import pandas as pd
import tkinter.ttk as ttk

# Local Support
import functionals as fun



window = tk.Tk()
window.title("PRTS")
window.geometry("900x450")
lb_developer = tk.Label(window, text="Developers: Henry Ouyang, Scott Xu")
lb_developer.place(x=675, y=420)

# [Experience Calculator]

'''
Windows Widgets
'''
# Promotion
lb_pro = tk.Label(window, text="Promotion Stage")
lb_pro.place(x=30, y=120)

promotion_rb=tk.IntVar()
rb_pro0 = tk.Radiobutton(window, text='0', variable=promotion_rb, value='0')
rb_pro0.place(x=150, y=120)
rb_pro1 = tk.Radiobutton(window, text='1', variable=promotion_rb, value='1')
rb_pro1.place(x=200, y=120)
rb_pro2 = tk.Radiobutton(window, text='2', variable=promotion_rb, value='2')
rb_pro2.place(x=250, y=120)

#Initial Level
lb_leveli = tk.Label(window, text="Initial Level")
lb_leveli.place(x=30, y=150)
e_leveli = tk.Entry(window, width=10)
e_leveli.place(x=150, y=150)


#Final Level
lb_levelf = tk.Label(window, text="Final Level")
lb_levelf.place(x=30, y=180)
e_levelf = tk.Entry(window, width=10)
e_levelf.place(x=150, y=180)


#Calculate Experience and LungMen Dollars
exp_sum = tk.IntVar()
lmd_sum = tk.IntVar()
def cal_explmd():
    var_leveli=int(e_leveli.get())
    var_levelf=int(e_levelf.get())
    promotion_stage=promotion_rb.get()
    if var_leveli<=var_levelf:
    	try:
    		lb_exp.configure(text='EXP = '+str(fun.exp_needed(var_leveli, var_levelf, promotion_stage)))
    		lb_lmd.configure(text='LMD = '+str(fun.lmd_needed(var_leveli, var_levelf, promotion_stage)))
    	except Exception as e:
	    	if promotion_stage==0:
	    		tk.messagebox.showwarning(title='Input Error', message='Please enter integers between 1 and 50.')
	    	if promotion_stage==1:
	    		tk.messagebox.showwarning(title='Input Error', message='Please enter integers between 1 and 70.')
	    	if promotion_stage==2:
	    		tk.messagebox.showwarning(title='Input Error', message='Please enter an integer between 1 and 90.')
    else:
    	tk.messagebox.showwarning(title='Input Error', message='The initial level should be less than the final level.')
    
        
lb_exp = tk.Label(window, height=1, width=12, text='EXP')
lb_exp.place(x=320, y=160)

lb_lmd = tk.Label(window, height=1, width=12, text='LMD')
lb_lmd.place(x=320, y=180)

b_exp = tk.Button(window, text='Calculate Exp', command=cal_explmd)
b_exp.place(x=320, y=120)

# edit background photo
canvas = tk.Canvas(window, bg='blue', height=300, width=400)
image_file = tk.PhotoImage(file= 'timg.gif')
image = canvas.create_image(200, 150, image=image_file)
canvas.place(x=450, y=110)


# Menu

# Exit the program
def exit_window():
    exit_flag = tk.messagebox.askyesno(title='Exit Program', message='Are you sure you want to exit PRTS?')
    if exit_flag == 1:
        window.destroy()

# Create data for a new operator

def new_operator():
    window_new_operator = tk.Toplevel(window)
    window_new_operator.title("New Operator")
    window_new_operator.geometry("900x450")
    button_exit_newop = tk.Button(window_new_operator, text='Save', command=self.exit_new_operator)
    button_exit_newop.pack()

def exit_new_operator(self):
    self.destroy() ## 这里会报错 self is not defined 我也不知道怎么能够达到 按新的button_exit_newop按钮可以退出
    # 子界面（window_new_operator）然后主界面不变


menubar = tk.Menu(window)
openmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Open', menu=openmenu)
openmenu.add_command(label='Operator', command=new_operator)
openmenu.add_command(label='Log')
openmenu.add_command(label='Base')
openmenu.add_separator()
openmenu.add_command(label='Exit',command=exit_window)

searchmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Search', menu=searchmenu)
searchmenu.add_command(label='Operator')
searchmenu.add_command(label='Wears')
searchmenu.add_command(label='Materials')

window.config(menu=menubar)






window.mainloop()
