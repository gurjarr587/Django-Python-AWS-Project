#!"C:\Programs\Python\Python36-32\python.exe"

import cgi#,cgitb
import socket
# import HostScannerDAL as HSD
import threading
import sqlite3
from time import gmtime, strftime
class Helper_Python_Host_Scanner():
	def __init__(self):														#the construct function and get hostname and ip from Python_Host_Scan.py

		form = cgi.FieldStorage()
		if form.getvalue('ip_address'):
			self.ip_addr = form.getvalue('ip_address')
			tupleone = socket.gethostbyaddr(str(self.ip_addr))
			self.hostname = tupleone[0]
			self.scan_StartTime = strftime("%a %b %d %H:%M:%S %Y", gmtime())


	def update_host_name(self):												#present the hostname and ip
		print('<form action="Switch_Results.py" method="post">')
		print('<h3 style = "margin-left:600px">SCANNING PAGE</h3>')
		print('<input type = "hidden" name = "ipaddr" value =' + str(self.ip_addr) + '></input>')

		print('<p>Received Host ID =' + '<span>' + str(self.ip_addr) + '</span>' + '</p>')
		print ('<p name = "hostName"> Started scanning = '+ str(self.hostname) +' </p>')	
		self.start_scan()


	def start_scan(self):													#start the scan
		self.Create_Host()
		self.scan_port(120,135)
		self.Create_Scan()


	def Create_Host(self):														#create HOST table
		db = sqlite3.connect('HostScanner.db')
		c = db.cursor()
		host_name = str(self.hostname)											#get hostname
		host_ip = str(self.ip_addr)												#get ip address
		ip_exits = False
		for row in c.execute('SELECT * FROM HOST'):
			if row[2] == host_ip:												#if ip address exists in HOST table
				ip_exits = True
				self.getHostid = row[0]
				break
		if ip_exits == False:														#if ip address doesn't exist in HOST table
			c.execute('''INSERT INTO HOST(HostName, HostIP) VALUES(?,?)''', (host_name, host_ip))
			c.execute('''SELECT * FROM HOST ORDER BY HostId DESC LIMIT 1''')
			result = c.fetchone()
			self.getHostid = result[0]												#get the host id
			db.commit()



	def Create_Scan(self):														#Create Scan Table
		
		db = sqlite3.connect('HostScanner.db')
		c = db.cursor()
		c.execute('''INSERT INTO Scan(HostId,ScanStartTime,ScanEndTime) VALUES(?,?,?)''', (self.getHostid, self.scan_StartTime, self.scan_EndTime))
		db.commit()
		


	def scan_port(self,min_port,max_port):										#present the port information
		for port in range(min_port,max_port):
			print('<p>Scanning port number ' + str(port) + ' for given Host -->' + str(self.ip_addr) + '</p>')
		
		print('<p>Finished Scanning</p>')
		print('<input type = "submit" value = "View Results"></input>')
		
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)					#create the socket
		db = sqlite3.connect('HostScanner.db')									#connect the database
		c = db.cursor()
		c.execute('''SELECT * FROM Scan ORDER BY ScanId DESC LIMIT 1''')
		result = c.fetchone()
		self.getScanId = result[0]

		
		print('<input type = "hidden" name = "scanid" value = "' + str(result[0]) + '"></input>')
		print('</form>')

		for port in range(min_port,max_port):									#scan the ports
			result = s.connect_ex((self.ip_addr, port))
			

			if result == 0:														#if the port is opened
			    c.execute('''INSERT INTO PortStatus(ScanId,PortNumber,IsPortOpen) VALUES(?,?,?)''', (self.getScanId,port,True))

			else:
				c.execute('''INSERT INTO PortStatus(ScanId,PortNumber,IsPortOpen) VALUES(?,?,?)''', (self.getScanId,port,False))
			db.commit()	    
		s.close()
		self.scan_EndTime = strftime("%a %b %d %H:%M:%S %Y", gmtime())

print("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Scanning</title>')
print ('</head>')
print ('<body>')

hphs = Helper_Python_Host_Scanner()
hphs.update_host_name()


print ('</body>')
print ('</html>')