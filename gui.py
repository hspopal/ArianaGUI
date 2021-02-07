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

database_dir = '/Users/haroonpopal/Google_Drive/misc/ariana/database_management/'
os.chdir(database_dir)


# Import data
database = pd.read_csv('test_database.csv')

cd = database.iloc[0]
notes_dict = ast.literal_eval(cd['notes'])
notes = list(notes_dict.items())

class ClientProfile:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("some application")
        #header = Frame(win, bg='green', height=30)
        #header.pack(fill='both') #, side='top')
        ci_sec = tk.Frame()
        self.cihead=tk.Label(ci_sec, text='Contact Information')
        self.ci1=tk.Label(ci_sec, text='Name: '+cd['last_name']+', '+cd['first_name'])
        self.ci2=tk.Label(ci_sec, text='Date of Birth: '+cd['dob'])
        self.ci3=tk.Label(ci_sec, text='Phone: '+cd['phone'])
        self.ci4=tk.Label(ci_sec, text='Email: '+cd['email'])
        
        #ci_sec.pack(side='left')
        ci_sec.grid(row=0, column=0)
        self.cihead.pack(side='top', padx=5, pady=5)
        self.ci1.pack(anchor='w')
        self.ci2.pack(anchor='w')
        self.ci3.pack(anchor='w')
        self.ci4.pack(anchor='w')
        
        
        pi_sec = tk.Frame()
        self.pihead=tk.Label(pi_sec, text='Policy Information')
        self.pi1=tk.Label(pi_sec, text='Company: '+cd['company'])
        self.pi2=tk.Label(pi_sec, text='Policy #: '+str(cd['policy_num']))
        self.pi3=tk.Label(pi_sec, text='Effecitve Date: '+cd['eff_date'])
        self.pi4=tk.Label(pi_sec, text='Experation Date: '+cd['exp_date'])
        self.pi5=tk.Label(pi_sec, text='Premium: '+cd['premium'])
        
        #pi_sec.pack(side='left', padx=10)
        pi_sec.grid(row=0, column=1)
        self.pihead.pack(side='top', padx=5, pady=5)
        self.pi1.pack(anchor='w')
        self.pi2.pack(anchor='w')
        self.pi3.pack(anchor='w')
        self.pi4.pack(anchor='w')
        self.pi5.pack(anchor='w')
        
        
        notes_sec = tk.Frame()
        self.nehead=tk.Label(notes_sec, text='Notes and Events')
        notes_date = []
        notes_info = []
        for i in range(len(notes)):
            notes_date.append(tk.Label(notes_sec, text=str(notes[i][0])+': '))
            notes_date[i].grid(row=i, column=0)
            notes_info.append(tk.Label(notes_sec, text=notes[i][1]))
            notes_info[i].grid(row=i, column=1)
        self.nee=tk.Entry(notes_sec)
        
        #notes_sec.pack(anchor='s', fill='x', expand='yes')
        notes_sec.grid(row=1, columnspan=2, sticky="ew")
        self.nee.grid(row=i+1)

        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.mainloop()

ClientProfile()
#window=tk.Tk()
#mywin=ClientProfile(window)
#window.title('Ariana Insurance')
#window.geometry("400x300+10+10")
#window.mainloop()







