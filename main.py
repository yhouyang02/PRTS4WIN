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

# Local Support
import functionals as fun



window = tk.Tk()
window.title("PRTS")
window.geometry("900x360")

# [Experience Calculator]

'''
Windows Widgets
'''
# Promotion
lb_pro = tk.Label(window, text="Promotion Stage")
lb_pro.place(x=30, y=30)

promotion_rb=tk.IntVar()
rb_pro0 = tk.Radiobutton(window, text='0', variable=promotion_rb, value='0')
rb_pro0.place(x=150, y=30)
rb_pro1 = tk.Radiobutton(window, text='1', variable=promotion_rb, value='1')
rb_pro1.place(x=200, y=30)
rb_pro2 = tk.Radiobutton(window, text='2', variable=promotion_rb, value='2')
rb_pro2.place(x=250, y=30)

#Initial Level
lb_leveli = tk.Label(window, text="Initial Level")
lb_leveli.place(x=30, y=60)
e_leveli = tk.Entry(window, width=10)
e_leveli.place(x=150, y=60)


#Final Level
lb_levelf = tk.Label(window, text="Final Level")
lb_levelf.place(x=30, y=90)
e_levelf = tk.Entry(window, width=10)
e_levelf.place(x=150, y=90)


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
lb_exp.place(x=320, y=70)

lb_lmd = tk.Label(window, height=1, width=12, text='LMD')
lb_lmd.place(x=320, y=90)

b_exp = tk.Button(window, text='Calculate Exp', command=cal_explmd)
b_exp.place(x=320, y=30)

# edit background photo
canvas = tk.Canvas(window, height=300, width=400)
image_file = tk.PhotoImage(file= 'timg.gif')
image = canvas.create_image(200, 150, image=image_file)
canvas.place(x=450, y=20)



window.mainloop()
