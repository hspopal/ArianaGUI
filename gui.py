#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:43:00 2021

@author: haroonpopal
"""

import tkinter as tk
import pandas as pd
import os
import ast
from PIL import Image, ImageTk
from datetime import date
import json
import numpy as np



database_dir = '/Users/Administrator/Google_Drive/misc/ariana/ArianaGUI/'
os.chdir(database_dir)


# Import data
database = pd.read_csv('../vFWAM82O - master-book.csv')
database = database.astype(str)

#client = database.iloc[0]
#notes_dict = ast.literal_eval(client['notes'])
#notes = list(notes_dict.items())



LARGEFONT =("Verdana", 35) 

class tkinterApp(tk.Tk): 
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs)
		
		self.database = database
		
		# creating a container 
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (StartPage, ClientDatabase, ClientProfile): 

			frame = F(container, self) 
			
			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 
			
			frame.grid(row = 0, column = 0, sticky ="nsew") 
			
		self.show_frame(StartPage) 

	# To display the current frame passed as parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		
	def get_page(self, page_class):
		return self.frames[page_class]




# first window frame startpage 
class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		
		
		image = Image.open("../logo.png")
		photo = ImageTk.PhotoImage(image)
		
		label = tk.Label(self, image = photo)
		label.image = photo
		label.grid(row=0)


		## button to show frame 2 with text layout2 
		button1 = tk.Button(self, text ="Clientele Database", 
		command = lambda : controller.show_frame(ClientDatabase)) 
	
		# putting the button in its place by 
		# using grid 
		button1.grid(row = 2, padx = 10, pady = 10)
		
		

class ClientDatabase(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		title = tk.Label(self, text ="Clientele Database", font = LARGEFONT) 
		title.grid(row = 0, columnspan=2, sticky="ew", padx = 10, pady = 10) 
		
		clients_cell = []
		clients_pols = []
		for i in range(len(database)):
			self.db_sel = i
			self.client = database.iloc[i]
			clients_cell.append(tk.Label(self, 
										 text=self.client['Card Name']))
			clients_cell[i].grid(row=i+1, column=0)
			clients_pols.append(tk.Button(self, text=self.client['Type'],
										  command = lambda: self.load_client_info(self.client)))
			clients_pols[i].grid(row=i+1, column=1)
			#if np.isnan(self.client['Notes']):
			if self.client['Notes'] == 'nan':
				notes_dict = {}
			else:
				notes_dict = ast.literal_eval(self.client['Notes'])
			self.notes = notes_dict
		
	def load_client_info(self, client):
		#client = database.iloc[0]
		
		#return client, self.db_sel
		self.controller.show_frame(ClientProfile)



class ClientProfile(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.response_entries = []
		#self.client = client
		self.notes_dict = {}
		page_ClientDatabase = self.controller.get_page(ClientDatabase)
		self.client = page_ClientDatabase.client
		self.notes = page_ClientDatabase.notes
		self.db_sel = page_ClientDatabase.db_sel
		
		self.client_page()
		
	def client_page(self):
		title = tk.Label(self, text ="Client Profile", font = LARGEFONT) 
		title.grid(row = 0, columnspan=2, sticky="ew", padx = 10, pady = 10) 

		ci_sec = tk.Frame(self, bd=2, relief='solid')
		self.cihead=tk.Label(ci_sec, text='Contact Information')
		self.ci1=tk.Label(ci_sec, text='Name: '+self.client['Card Name'])
		#self.ci2=tk.Label(ci_sec, text='Date of Birth: '+self.client['dob'])
		self.ci3=tk.Label(ci_sec, text='Phone: '+str(self.client['Phone']))
		self.ci4=tk.Label(ci_sec, text='Email: '+str(self.client['Email']))
		
		ci_sec.grid(row=1, column=0, sticky="ns")
		self.cihead.grid()
		self.ci1.grid()
		#self.ci2.grid()
		self.ci3.grid()
		self.ci4.grid()
		
		
		pi_sec = tk.Frame(self, bd=2, relief='solid')
		self.pihead=tk.Label(pi_sec, text=self.client['Type']+' Policy Information')
		self.pi1=tk.Label(pi_sec, text='Company: '+self.client['Company'])
		self.pi2=tk.Label(pi_sec, text='Policy #: '+str(self.client['Policy #']))
		self.pi3=tk.Label(pi_sec, text='Effecitve Date: '+self.client['Effective Date'])
		self.pi4=tk.Label(pi_sec, text='Experation Date: '+self.client['Expiration Date'])
		self.pi5=tk.Label(pi_sec, text='Premium: '+self.client['Premium'])
		
		pi_sec.grid(row=1, column=1)
		self.pihead.grid()
		self.pi1.grid()
		self.pi2.grid()
		self.pi3.grid()
		self.pi4.grid()
		self.pi5.grid()
		
		
		notes_sec = tk.Frame(self)
		self.nehead=tk.Label(notes_sec, text='Notes and Events')
		notes_date = []
		notes_info = []
		#notes = self.client['notes']
		temp_dates = list(self.notes.keys())
		temp_notes = list(self.notes.values())
		i = 0
		for i in range(len(self.notes)):
			#notes_date.append(tk.Label(notes_sec, text=str(self.notes[i][0])+': '))
			notes_date.append(tk.Label(notes_sec, text=str(temp_dates[i])))
			notes_date[i].grid(row=i, column=0, sticky='w')
			#notes_info.append(tk.Label(notes_sec, text=self.notes[i][1]))
			notes_info.append(tk.Label(notes_sec, text=str(temp_notes[i])))
			notes_info[i].grid(row=i, column=1, stick='w')
		
		self.nee=tk.Entry(notes_sec)
		self.response_entries.append(self.nee)
		
		self.save_button = tk.Button(notes_sec, text='Save note', command=lambda: self.save_note())
		
		notes_sec.grid(row=2, columnspan=2, sticky="ew")
		self.nee.grid(row=i+1)
		self.save_button.grid(row=i+1, column=1)
		
	def save_note(self):
		today = date.today()
		d1 = today.strftime("%m/%d/%Y")
		self.notes[d1] = self.response_entries[0].get()
		database.loc[self.db_sel, ('Notes')] = json.dumps(self.notes)
		print(database.iloc[self.db_sel]['Notes'])
		
		database.to_csv('../test_database.csv', index=False)
		


# Driver Code 
app = tkinterApp() 
app.title('Ariana Insurance')
app.mainloop() 







#ClientProfile()
#window=tk.Tk()
#mywin=ClientProfile(window)
#window.title('Ariana Insurance')
#window.geometry("400x300+10+10")
#window.mainloop()







