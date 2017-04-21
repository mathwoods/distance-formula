#!/usr/bin/env python

#****************************************************************************************
#Mathwoods - Distance Formula
#A small program that calculates the distance between two points on an XY plane
#Created by Mathwoods on November 22, 2016
#Last modified on December 9th, 2016
#****************************************************************************************

#DOMAIN LOGIC
import math 

def dist_formula(x1=0, y1=0, x2=0, y2=0):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)


#INPUT CHECK FUNCTIONS
def is_empty(str): 
	if len(str) == 0:
		return True
	else:
		return False

def is_float(str): 
	try:
		float(str)
		return True
	except ValueError:
		return False


#DATA FORMAT FUNCTIONS FOR OUTPUT (NOT NEEDED FOR THIS APP)


#USER INTERFACE
import Tkinter as tk
import tkFont 

class Application(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master, borderwidth=10)
		self.grid()
		
		self.win = self.winfo_toplevel()
		self.create_widgets()
		self.center_window()
		self.set_winontop()
		self.fix_winsize()
		self.kb_events()
			
		
	def create_widgets(self):
		#Note that all buttons have been disabled to take focus to make navigation
		#between entry fields faster with TAB/Shift-TAB
		#Enter automatically launches process_data anywhere in the window
			
		#Point A input
		self.label_pointA = tk.Label(self, text="Point A:")
		self.label_pointA.grid(sticky=tk.W, row=0, column=0, columnspan=2) 
		
		self.label_Xa = tk.Label(self, text="Xa:")
		self.label_Xa.grid(sticky=tk.W, row=1, column=0)
		
		self.input_Xa = tk.StringVar()
		self.entrytxt_Xa = tk.Entry(self, textvariable=self.input_Xa, width=30)
		self.entrytxt_Xa.focus()	#gives focus right away to Entry field 
		self.entrytxt_Xa.grid(row=1, column=1) 
		
		self.label_Ya = tk.Label(self, text="Ya:")
		self.label_Ya.grid(sticky=tk.W, row=2, column=0)
		
		self.input_Ya = tk.StringVar()
		self.entrytxt_Ya = tk.Entry(self, textvariable=self.input_Ya, width=30)
		self.entrytxt_Ya.grid(row=2, column=1) 
		
		#Point B input
		self.label_pointB = tk.Label(self, text="Point B:")
		self.label_pointB.grid(sticky=tk.W, row=3, column=0, columnspan=2) 
		
		self.label_Xb = tk.Label(self, text="Xb:")
		self.label_Xb.grid(sticky=tk.W, row=4, column=0)
		
		self.input_Xb = tk.StringVar()
		self.entrytxt_Xb = tk.Entry(self, textvariable=self.input_Xb, width=30)
		self.entrytxt_Xb.focus()	#gives focus right away to Entry field 
		self.entrytxt_Xb.grid(row=4, column=1) 
		
		self.label_Yb = tk.Label(self, text="Yb:")
		self.label_Yb.grid(sticky=tk.W, row=5, column=0)
		
		self.input_Yb = tk.StringVar()
		self.entrytxt_Yb = tk.Entry(self, textvariable=self.input_Yb, width=30)
		self.entrytxt_Yb.grid(row=5, column=1) 
		
		#Calculate button
		self.button_calc = tk.Button(self, text="Calculate", command=self.process_data, takefocus=0) 
		self.button_calc.grid(row=6, column=0, columnspan=2, pady=5)
		
		#output: label widget	
		self.output_text = tk.StringVar()
		self.output_text.set("???")
		self.label_output = tk.Label(self, textvariable=self.output_text, font=tkFont.Font(weight="bold"))
		self.label_output.grid(row=7, column=0, columnspan=2)
		
		#Clear button
		self.button_clear = tk.Button(self, text="Clear", command=self.clear, takefocus=0) 
		self.button_clear.grid(row=8, column=0, pady=5, sticky=tk.W)
		
		#Exit button
		self.button_exit = tk.Button(self, text = "Exit", command=self.quit, takefocus=0)
		self.button_exit.grid(row=8, column=1, sticky=tk.E)


	def process_data(self, *args): 
		#*args is an arbitrary argument list (use instead of evt)
		#Allows for Enter and mouse-click events to use this function
		
		#read input
		str_Xa = self.input_Xa.get()
		str_Ya = self.input_Ya.get()
		str_Xb = self.input_Xb.get()
		str_Yb = self.input_Yb.get()
		
		#check input if valid
		if is_empty(str_Xa) or is_empty(str_Ya) or is_empty(str_Xb) or is_empty(str_Yb):
			self.label_output.config(fg='red')
			self.output_text.set("Cannot compute - field(s) empty.")
			return
		
		if not (is_float(str_Xa) and is_float(str_Ya) and is_float(str_Xb) and is_float(str_Yb)):
			self.label_output.config(fg='red')
			self.output_text.set("Cannot compute - non-numeric input.")
			return
			
		#format input for processing (if necessary)
		flt_Xa, flt_Ya, flt_Xb, flt_Yb = float(str_Xa), float(str_Ya), float(str_Xb), float(str_Yb)
		
		#process input using separate domain function/object method
		ans = dist_formula(x1=flt_Xa, y1=flt_Ya, x2=flt_Xb, y2=flt_Yb)
		
		#format processs input for output (if necessary)
			
		#write output
		self.label_output.config(fg='blue')
		self.output_text.set("d(A,B)= %s units" % ans)
		

	def clear(self):
		#reset all input and output fields
		self.input_Xa.set("")
		self.input_Ya.set("")
		self.input_Xb.set("")
		self.input_Yb.set("")
		self.label_output.config(fg='black')
		self.output_text.set("???")
		
		#return focus to top input field
		self.entrytxt_Xa.focus()
		
		
	def set_winontop(self):
		self.win.after_idle(self.win.attributes, '-topmost', True)
		self.win.after(1000, self.win.attributes, '-topmost', False)
		
					
	def center_window(self):
		#necessary so as to get the latest win dimensions  
		self.win.update_idletasks()
		
		geo_string = self.win.geometry()
		w = self.win.winfo_width()
		h = self.win.winfo_height()
		
		ws = self.win.winfo_screenwidth()
		hs = self.win.winfo_screenheight()
		
		#math to get the coordinates to center the window
		x = (ws-w)/2
		y = (hs-h)/2
		
		#set geometry string; see Tkinter documentation
		self.win.geometry('%dx%d+%d+%d' % (w,h,x,y))
		
			
	def fix_winsize(self):
		self.win.resizable(width=False, height=False)
	
	
	def kb_events(self):
		self.win.bind("<Return>", self.process_data)
	
	
					
#MAIN THREAD	
app = Application()
win = app.winfo_toplevel()
app.master.title("MathWoods - Distance Formula")
app.mainloop()
