#!"C:\Programs\Python\Python36-32\python.exe"

import cgi,cgitb
# import HostScannerDAL as HSD
import GUI_Display as GD
import threading
import socket
import sqlite3
from tkinter import *
from tkinter.ttk import *
root =""


class Switch_Result:
	def __init__(self):
		
		form = cgi.FieldStorage()
		self.ip_addr = ""
		self.hostname = ""
		self.lastScanId = ""
		if form.getvalue('ipaddr'):									#get the ip address from Scanning_Update.py
			self.ip_addr = form.getvalue('ipaddr')
			tupleone = socket.gethostbyaddr(str(self.ip_addr))
			self.hostname = tupleone[0]
			self.lastScanId = form.getvalue('scanid')
		print('<h2 style = "margin-left:600px">RESULT PAGE</h2>')
		print('<table><tr><th>SCAN_ID:</th><th>PORT_NUMBER</th><th>IS_OPEN</th><th style = "padding:0px 70px">SCAN_TIME</th></tr>')
		t = threading.Thread(target=self.CGUI)						#make the thread
		t.start()
		self.Switch_Results()


	def Switch_Results(self):
		
		db = sqlite3.connect('HostScanner.db')						#connect the database
		c = db.cursor()
		for row in c.execute('SELECT * FROM Scan WHERE ScanId = ?',(self.lastScanId,)):			#get the scantime
			scantime = row[2]
		for row in c.execute('SELECT * FROM PortStatus WHERE ScanId = ?',(self.lastScanId,)):	#draw the table of port status
			print('<tr style = "border-style:none"><td>' + str(row[0]) + '</td>')
			print('<td>' + str(row[1]) + '</td>')
			print('<td>' + str(row[2]) + '</td>')
			print('<td>' + str(scantime) + '</td></tr>')
			# print('<div style = "display:block;font-size:20px">')
			# print('<p style = "display:inline-block">'+ str(row[0]) +'</p>')
			# print('<p style = "display:inline-block">'+ str(row[1]) +'</p>')
			# print('<p style = "display:inline-block">'+ str(row[0]) +'</p>')
			# print('</div>')
		print('</table>')
		db.commit()

	def CGUI(self):	
		self.GDD = GD.ResultsDialog(self.ip_addr, self.hostname)
print("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Scanning</title>')
print('<style>table, th, td {border: 1px solid black}</style>')
print ('</head>')
print ('<body>')		
switch_res = Switch_Result()
print ('</body>')
print ('</html>')



