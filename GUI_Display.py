import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
import sqlite3
import cgi
# import HostScannerDAL as HSD
class ResultsDialog(tk.Frame):
	def __init__(self, host_ip, host_name):					#make the treeviews
		

		root = Tk()
		Frame.__init__(self, root)
		self.gui_init()
		self.grid(sticky = (N,S,W,E))
		root.grid_rowconfigure(0, weight = 1)
		root.grid_columnconfigure(0, weight = 1)
		root.mainloop()		
	def gui_init(self):										#draw the table with tkinnter
		
		db = sqlite3.connect('HostScanner.db')
		c = db.cursor()
		c.execute('''SELECT * FROM PortStatus ORDER BY ScanId DESC LIMIT 1''')
		result = c.fetchone()
		self.lastScanId = result[0]

		tv = Treeview(self)
		tv['columns'] = ('scanid','starttime', 'endtime', 'status')
		tv.column("#0", stretch=NO, minwidth=0, width=0)
		tv.heading('scanid', text='SCAN ID')
		tv.column('scanid', anchor='center', width=100)
		tv.heading('starttime', text='PORT NUMBER')
		tv.column('starttime', anchor='center', width=100)
		tv.heading('endtime', text='IS OPEN')
		tv.column('endtime', anchor='center', width=100)
		tv.heading('status', text='SCAN TIME')
		tv.column('status', anchor='center', width=100)
		tv.grid(sticky = (N,S,W,E))
		self.treeview = tv
		self.grid_rowconfigure(0, weight = 1)
		self.grid_columnconfigure(0, weight = 1)
		
		for row in c.execute('SELECT * FROM Scan WHERE ScanId = ?',(self.lastScanId,)):
			self.scantime = row[2]
		for row in c.execute('SELECT * FROM PortStatus WHERE ScanId = ?',(self.lastScanId,)):
			self.treeview.insert('', 'end', values=(row[0],row[1], row[2],self.scantime))
		db.commit()

	def __update_grd_(self):					#update the database
		db = sqlite3.connect('HostScanner.db')
		c = db.cursor()
		for row in c.execute('SELECT * FROM Scan WHERE ScanId = ?',(self.lastScanId,)):
			self.scantime = row[2]
		for row in c.execute('SELECT * FROM PortStatus WHERE ScanId = ?',(self.lastScanId,)):
			self.scanId = row[0]
			self.port_num = row[1]
			self.port_status = row[2]
# root = Tk()
# ResultsDialog("123", "234")
# root.mainloop()