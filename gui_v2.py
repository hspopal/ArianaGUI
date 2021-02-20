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
   
    def client_table(self): 
        scrollbarx = tk.Scrollbar(tk.TableMargin, orient='HORIZONTAL')
        scrollbary = tk.Scrollbar(tk.TableMargin, orient='VERTICAL')
        tree = tk.Treeview(tk.TableMargin, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side='RIGHT', fill='Y')
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side='BOTTOM', fill='X')
        tree.heading('Firstname', text="Firstname", anchor='W')
        tree.heading('Lastname', text="Lastname", anchor='W')
        tree.heading('Address', text="Address", anchor='W')
        tree.column('#0', stretch='NO', minwidth=0, width=0)
        tree.column('#1', stretch='NO', minwidth=0, width=200)
        tree.column('#2', stretch='NO', minwidth=0, width=200)
        tree.column('#3', stretch='NO', minwidth=0, width=300)
        tree.pack()
            
        
        for i in range(len(database)):
            firstname = row['firstname']
            lastname = row['lastname']
            address = row['address']
            tree.insert("", 0, values=(firstname, lastname, address))

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







