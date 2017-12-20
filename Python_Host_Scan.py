#!"C:\Programs\Python\Python36-32\python.exe"

import cgi,cgitb

import tkinter as tk

class Python_Host_Scanner:

	def __init__(self):						#draw the first interface
		
		print("Content-type:text/html\r\n\r\n")
		print ('<html>')
		print ('<head>')
		print('<style>table,th,td{border: 1px solid black;}form{height:100%;}</style>')
		print ('<title>Host Scanner</title>')
		print ('</head>')
		print ('<body>')
		print('<form action="Scanning_Update.py" method="post">')
		print ('<h2 style = "color:#c49c1b;margin-left:700px">WELCOME TO PYTHON HOST SCANNER</h2>')	
		print('<table style = "margin-left:400px"><tr><th style = "width:300px">HOST IP:</th><th style = "width:700px"><input type = "text" name = "ip_address"></input></th></tr><tr><td style = "width:300px;" colspan = "2"><input type = "submit" value = "SCAN"></input></td></tr></table>')
		print('</form>')
		print ('</body>')
		print ('</html>')

pt = Python_Host_Scanner();
