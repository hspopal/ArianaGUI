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



database_dir = '/Users/Administrator/Google_Drive/misc/ariana/ArianaGUI/'
os.chdir(database_dir)


# Import data
database = pd.read_csv('../test_database.csv')

#client = database.iloc[0]
#notes_dict = ast.literal_eval(client['notes'])
#notes = list(notes_dict.items())



LARGEFONT =("Verdana", 35) 

class tkinterApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs) 
		
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

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont):
		frame = self.frames[cont] 
		frame.tkraise() 



# first window frame startpage 
class StartPage(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        
        
        #image = Image.open("../logo.png")
        #photo = ImageTk.PhotoImage(image)
        
        #label = tk.Label(self, image = photo)
        #label.image = photo
        #label.grid(row=0)


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
            client=database.iloc[i]
            clients_cell.append(tk.Label(self, 
                                         text=client['last_name']+', '+client['first_name']))
            clients_cell[i].grid(row=i+1, column=0)
            clients_pols.append(tk.Button(self, text=client['policy_type'],
                                          command = lambda: self.load_client_info(client)))
            clients_pols[i].grid(row=i+1, column=1)
        
    def load_client_info(self, client):
        self.controller.show_frame(ClientProfile(self.controller, client))
        client = database.iloc[0]
        notes_dict = ast.literal_eval(client['notes'])
        notes = list(notes_dict.items())
        return client, self.db_sel



class ClientProfile(tk.Frame):
    
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        self.response_entries = []
        self.client = client
        self.notes_dict = {}
        
    def client_page(self):
        title = tk.Label(self, text ="Client Profile", font = LARGEFONT) 
        title.grid(row = 0, columnspan=2, sticky="ew", padx = 10, pady = 10) 

        ci_sec = tk.Frame(self, bd=2, relief='solid')
        print(self.client)
        self.cihead=tk.Label(ci_sec, text='Contact Information')
        #self.ci1=tk.Label(ci_sec, text='Name: '+self.client['last_name']+', '+self.client['first_name'])
        #self.ci2=tk.Label(ci_sec, text='Date of Birth: '+self.client['dob'])
        #self.ci3=tk.Label(ci_sec, text='Phone: '+self.client['phone'])
        #self.ci4=tk.Label(ci_sec, text='Email: '+self.client['email'])
        
        ci_sec.grid(row=1, column=0, sticky="ns")
        self.cihead.grid()
        #self.ci1.grid()
        #self.ci2.grid()
        #self.ci3.grid()
        #self.ci4.grid()
        
        
        pi_sec = tk.Frame(self, bd=2, relief='solid')
        #self.pihead=tk.Label(pi_sec, text=self.client['policy_type']+' Policy Information')
        #self.pi1=tk.Label(pi_sec, text='Company: '+self.client['company'])
        #self.pi2=tk.Label(pi_sec, text='Policy #: '+str(self.client['policy_num']))
        #self.pi3=tk.Label(pi_sec, text='Effecitve Date: '+self.client['eff_date'])
        #self.pi4=tk.Label(pi_sec, text='Experation Date: '+self.client['exp_date'])
        #self.pi5=tk.Label(pi_sec, text='Premium: '+self.client['premium'])
        
        pi_sec.grid(row=1, column=1)
        #self.pihead.grid()
        #self.pi1.grid()
        #self.pi2.grid()
        #self.pi3.grid()
        #self.pi4.grid()
        #self.pi5.grid()
        
        
        notes_sec = tk.Frame(self)
        self.nehead=tk.Label(notes_sec, text='Notes and Events')
        notes_date = []
        notes_info = []
        #notes = client['notes']
        #for i in range(len(notes)):
        #    notes_date.append(tk.Label(notes_sec, text=str(notes[i][0])+': '))
        #    notes_date[i].grid(row=i, column=0, sticky='w')
            #notes_info.append(tk.Label(notes_sec, text=notes[i][1]))
            #notes_info[i].grid(row=i, column=1, stick='w')
        
        self.nee=tk.Entry(notes_sec)
        self.response_entries.append(self.nee)
        
        self.save_button = tk.Button(notes_sec, text='Save note', command=self.save_note)
        
        notes_sec.grid(row=2, columnspan=2, sticky="ew")
        #self.nee.grid(row=i+1)
        #self.save_button.grid(row=i+1, column=1)
        
    def save_note(self):
        today = date.today()
        d1 = today.strftime("%m/%d/%Y")
        self.notes_dict[d1] = self.response_entries[0].get()
        database.loc[self.db_sel]['notes'] = self.notes_dict
        print(database.loc[self.db_sel]['notes'])
        


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







