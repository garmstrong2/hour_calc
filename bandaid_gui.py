from tkinter import *

class bandaid_app(Tk):
	def __init__(self, onsubmit):
		super().__init__()
		self.onsubmit = onsubmit
		self.canvas = Canvas(self)
		self.frame = bandaid_frame(self)
		self.entries = self.frame.entries
		self.geometry('1275x675')
		self.title('BANDAID')
		self.bind_all("<MouseWheel>", self.mouse_scroll)
		self.init_canvas()

	def init_canvas(self):
		right_scrollbar = Scrollbar(self, orient=VERTICAL, command = self.canvas.yview)
		bottom_scrollbar = Scrollbar(self, orient=HORIZONTAL, command = self.canvas.xview)
		right_scrollbar.pack(side=RIGHT, fill=Y)
		bottom_scrollbar.pack(side=BOTTOM, fill=X)
		self.canvas.configure(scrollregion = (0, 0, 2000, 2000), yscrollcommand = right_scrollbar.set, 
			xscrollcommand = bottom_scrollbar.set)
		self.canvas.pack(side=TOP, fill=BOTH, expand=1)
		self.canvas.create_window((0,0), window=self.frame, anchor=NW, tags='self.frame')

	def mouse_scroll(self, event):
		if event.delta:
			self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
		else:
			if event.num == 5:
				move = 1
			else:
				move = -1

			self.canvas.yview_scroll(move, "units")
		
class bandaid_frame(Frame):

	def __init__(self, master):
		Frame.__init__(self)
		self.entries = {}
		self.init_window()
		
	def init_window(self):
################################################## Styles ###################################################
		h1 = ('Times', 18, 'bold')
		h2 = ('Times', 14, 'bold')
		p = ('Arial', 12)
		red = '#ff0000'
		gray = '#aaa'
		light_gray = '#bbb'

################################################## Divs #####################################################
		left_frame = Frame(self, bg=red)
		left_frame.grid(row=0, column=0, ipady=14)
		right_frame = Frame(self)
		right_frame.grid(row=0, column=1, ipady=3)

		left_top = Frame(left_frame, bg=red)
		left_top.grid(row=0, column=0, sticky=W)
		left_center = Frame(left_frame, bg=gray)
		left_center.grid(row=1, column=0, sticky=W, ipadx=210)
		left_bottom = Frame(left_frame, bg=red)
		left_bottom.grid(row=2, column=0, sticky=W)

		left_top_1 = Frame(left_top, bg=red)
		left_top_1.grid(row=0, column=0, sticky=W)
		left_top_2 = Frame(left_top, bg=red)
		left_top_2.grid(row=1, column=0, sticky=W)

		left_bottom_1 = Frame(left_bottom, bg=red)
		left_bottom_1.grid(row=0, column=0, sticky=W)
		left_bottom_2 = Frame(left_bottom, bg=red)
		left_bottom_2.grid(row=1, column=0, sticky=W)
		left_bottom_3 = Frame(left_bottom, bg=red)
		left_bottom_3.grid(row=2, column=0, sticky=W)
		left_bottom_4 = Frame(left_bottom, bg=red)
		left_bottom_4.grid(row=3, column=0, sticky=W)
		left_bottom_5 = Frame(left_bottom, bg=red)
		left_bottom_5.grid(row=4, column=0, sticky=W)
		left_bottom_6 = Frame(left_bottom, bg=red)
		left_bottom_6.grid(row=5, column=0, sticky=W)
		left_bottom_7 = Frame(left_bottom, bg=red)
		left_bottom_7.grid(row=6, column=0, sticky=W)

		right_top = Frame(right_frame)
		right_top.grid(row=0, column=0, sticky=W)
		right_center = Frame(right_frame)
		right_center.grid(row=1, column=0, sticky=W)
		right_bottom = Frame(right_frame)
		right_bottom.grid(row=2, column=0, sticky=W)

		right_top_1 = Frame(right_top, bg=gray)
		right_top_1.grid(row=0, column=0, sticky=W, ipadx=180)
		right_top_2 = Frame(right_top, bg=gray)
		right_top_2.grid(row=1, column=0, sticky=W, ipadx=170)
		right_top_3 = Frame(right_top, bg=gray)
		right_top_3.grid(row=2, column=0, sticky=W, ipadx=190)

		right_center_1 = Frame(right_center, bg=light_gray)
		right_center_1.grid(row=0, column=0, sticky=W, ipadx=175)
		right_center_2 = Frame(right_center, bg=gray)
		right_center_2.grid(row=1, column=0, sticky=W, ipadx=178)
		right_center_3 = Frame(right_center, bg=gray)
		right_center_3.grid(row=2, column=0, sticky=W, ipadx=150)
		right_center_4 = Frame(right_center, bg=gray)
		right_center_4.grid(row=3, column=0, sticky=W, ipadx=83)
		right_center_5 = Frame(right_center, bg=gray)
		right_center_5.grid(row=4, column=0, sticky=W, ipadx=171)
		right_center_6 = Frame(right_center, bg=gray)
		right_center_6.grid(row=5, column=0, sticky=W, ipadx=144)
		right_center_7 = Frame(right_center, bg=gray)
		right_center_7.grid(row=6, column=0, sticky=W, ipadx=20)

		right_bottom_1 = Frame(right_bottom)
		right_bottom_1.grid(row=0, column=0, sticky=W)
		right_bottom_2 = Frame(right_bottom, bg=gray)
		right_bottom_2.grid(row=1, column=0, sticky=W, ipadx=140)
		right_bottom_3 = Frame(right_bottom)
		right_bottom_3.grid(row=2, column=0, sticky=E)

########################################## Directory Description #################################################
		Label(left_top_1, text='\nDirectory', bg=red, justify=LEFT, fg='white', 
			font=h1).grid(row=0, column=0, sticky=W)
		Label(left_top_2, text=('\nEnter the working directory that this code is operating from and ' +
			'the name of the base case file \nthat you will be working from (make ' +
			'sure that the file is in this working directory)\n')
			, bg=red, justify=LEFT, fg='white', font=p).grid(row=0, column=0, sticky=W)
################################ Flow Conditions and Boundary Description #########################################
		Label(left_bottom_1, text='\nFlow Conditions and Boundary Conditions', bg=red, fg='white', justify=LEFT, 
			font=h1).grid(row=0, column=0)
		Label(left_bottom_2, text='\nEntering info into text boxes', bg=red, fg='white', justify=LEFT, 
			font=h2).grid(row=0, column=0)
		Label(left_bottom_3, text=('\nFor each text box shown enter the values that ' +
			'you obtained from Fluent. You do not need to enter\nthe commands as these have ' +
			'already been hard coded. All you need are the specific boundary\nconditions, ' +
			'the names of the faces you are applying the boundary conditions to, and any ' +
			'of the\noptions declared in the Conditions. '), 
			bg=red, justify=LEFT, fg='white', font=p).grid(row=0, column=0)
		Label(left_bottom_4, text='\nAdditional geometry information for inlet boundary conditions', bg=red, fg='white',
			justify=LEFT, font=h2).grid(row=0, column=0)
		Label(left_bottom_5, text='\nWrite yes terms as "y" and no terms as "n" Instead of ' +
			'typing in the desired velocity, type in the \nword "vel" the code is set up to  ' +
			'recognize this value and insert your velocity terms correctly from\nthe csv file. ', bg=red, fg='white', 
			justify=LEFT, font=p).grid(row=0, column=0)
################################### Convergence Criteria Description #############################################
		Label(left_bottom_6, text='\nConvergence Criteria', bg=red, fg='white', font=h1).grid(row=2, column=0)
		Label(left_bottom_7, text='\nEnter convergence criteria in ' +
			'scientific notation (1e-3, 1e-6...etc). For number of iterations just\nenter ' +
			'the maximum number of iterations that you want to run. When you are finished, ' + 
			'double\ncheck to amke sure everything is correct and the hit the "Execute" ' +
			'button to generate the script', bg=red, fg='white', font=p, justify=LEFT).grid(row=3, column=0)

################################################# Entry Labels ##################################################
		Label(left_center, text='Number of Nodes', bg=gray, font='bold').grid(row=0, column=0, sticky=W, ipady=10)
		Label(right_top_1, text='Working Home', font='bold', bg=gray).grid(row=0, column=0, sticky=W, ipady=10)
		Label(right_top_2, text='Working Directory', font='bold', bg=gray).grid(row=0, column=0, sticky=W, ipady=10)
		Label(right_top_3, text='Base Case', font='bold', bg=gray).grid(row=0, column=0, sticky=W, ipady=10)
		Label(right_center_1, text='Number of Cores', font='bold', bg=light_gray).grid(row=3, column=0, sticky=W, ipady=10)
		Label(right_center_2, text='Inlet Face Name', font='bold', bg=gray).grid(row=4, column=0, sticky=W, ipady=10)
		Label(right_center_3, text='Inlet Boundary Condition', font='bold', bg=gray).grid(row=5, column=0, sticky=W, ipady=10)
		Label(right_center_4, text='Additional Geometry Information for Inlet BC', font='bold', bg=gray).grid(row=6, column=0, 
			sticky=W, ipady=10)
		Label(right_center_5, text='Outlet Face Name', font='bold', bg=gray).grid(row=7, column=0, sticky=W, ipady=10)
		Label(right_center_6, text='Outlet Boundary Condition', font='bold', bg=gray).grid(row=8, column=0, sticky=W, ipady=10)
		Label(right_center_7, text='Additional Geometry Information for Outlet Boundary Condition', font='bold', 
			bg=gray).grid(row=9, column=0, sticky=W, ipady=10)
		Label(right_bottom_1).grid(row=0, ipady=10)
		Label(right_bottom_1).grid(row=1, ipady=10)
		Label(right_bottom_2, text='Enter Convergence Criteria', font='bold', bg=gray).grid(row=0, column=0, sticky=W, ipady=10)
		Label(right_bottom_2, text='Enter Number of Iterations', font='bold', bg=gray).grid(row=1, column=0, sticky=W, ipady=10)

################################################### Entries ####################################################
		self.entries['work_home'] = Entry(right_top_1)
		self.entries['work_home'].grid(row=0, column=1)
		
		self.entries['work_dir'] = Entry(right_top_2)
		self.entries['work_dir'].grid(row=0, column=1)

		self.entries['base_case'] = Entry(right_top_3)
		self.entries['base_case'].grid(row=0, column=1)

		self.entries['nodes'] = Entry(left_center)
		self.entries['nodes'].grid(row=0, column=1)

		self.entries['cores'] = Entry(right_center_1)
		self.entries['cores'].grid(row=3, column=1)

		self.entries['inlet_name'] = Entry(right_center_2)
		self.entries['inlet_name'].grid(row=4, column=1)

		self.entries['inlet_bc'] = Entry(right_center_3)
		self.entries['inlet_bc'].grid(row=5, column=1)

		self.entries['inlet_geo'] = Entry(right_center_4)
		self.entries['inlet_geo'].grid(row=6, column=1)

		self.entries['outlet_name'] = Entry(right_center_5)
		self.entries['outlet_name'].grid(row=7, column=1)

		self.entries['outlet_bc'] = Entry(right_center_6)
		self.entries['outlet_bc'].grid(row=8, column=1)

		self.entries['outlet_geo'] = Entry(right_center_7)
		self.entries['outlet_geo'].grid(row=9, column=1)

		self.entries['conv_crit'] = Entry(right_bottom_2)
		self.entries['conv_crit'].grid(row=0, column=1)

		self.entries['iterations'] = Entry(right_bottom_2)
		self.entries['iterations'].grid(row=1, column=1)

		#Label(right_bottom_3).grid(row=0)
		submitButton = Button(right_bottom_3, text='Submit', font='bold', padx=20, bg=gray, command=self.submit)
		submitButton.grid(row=1, pady=10, padx=20)
		
	def client_quit(self):
		exit()

	def print_entries(self):
		names = ['work_home', 'work_dir', 'base_case', 'nodes', 'cores', 'inlet_name', 'inlet_bc', 'inlet_geo', 
			'outlet_name', 'outlet_bc', 'outlet_geo', 'conv_crit', 'iterations']
		for i in range(0, len(names)):
			print(self.entries[names[i]].get())

	def submit(self):
		names = ['work_home', 'work_dir', 'base_case', 'nodes', 'cores', 'inlet_name', 'inlet_bc', 'inlet_geo', 
			'outlet_name', 'outlet_bc', 'outlet_geo', 'conv_crit', 'iterations']
		inputs = {}
		for i in range(0, len(names)):
			inputs[names[i]] = self.entries[names[i]].get()
		self.master.onsubmit(inputs)


def main():
	app = bandaid_app(print)
	app.mainloop()

if __name__ == "__main__":
	main()