import sqlite3 as db
import time

class HostScannerDAL:
    def __init__(self):
        self.is_conn_open = False
        self.__connect_()
		
	def __connect_(self,dbname):
		'''
		Connect to database using the .db file provided
				
		'''
		# connect to the database
		# retrieve the values in form of db dictionary
		# create a new cursor
		self.dbname = dbname
		db = sqlite3.connect(self.dbname)
		c = db.cursor()
		db.commit()
			
	
	def read_host(self, host_ip, host_name=None):
		
		# CHECKS IF THE RECORD IS ALREADY PRESENT AND GIVES A VARIABLE
		
		# CHECK FOR THE FIRST TIME ENTRY
		self.host_ip = host_ip
		self.host_name = host_name
		form = cgi.FieldStorage()
		if form.getvalue('ip_address'):
			self.ip_addr = form.getvalue('ip_address')
			tupleone = socket.gethostbyaddr(str(self.ip_addr))
			self.read_host_result = tupleone[0]
		return read_host_result
	
	
	def create_host(self, host_ip, host_name):
	
		# Inserts default value if table is empty
		
		# Inserts max value +1 if table is not empty
		self.host_ip = host_ip
		self.host_name = host_name
		self.return_host_numb = host_ip
		return self.return_host_numb
	
	
	def create_scan(self, host_id):
		'''
		
		Creates the scan_id for each time the host scanner starts scanning the port-id's
		
		'''
		self.host_id = host_id
		db = sqlite3.connect('HostScanner.db')
		c = db.cursor()
		c.execute('''SELECT * FROM Scan ORDER BY ScanId DESC LIMIT 1''')
		result = c.fetchone()
		self.getScanId = result[0]
	
	def update_scan_end_time(self, scan_id):
		'''
		
		Update sthe SCAN table after the scanning is completed
		
		'''
		self.scan_id = scan_id
		db = sqlite3.connect('HostScanner.db')
		c = db.cursor()
		c.execute('''SELECT * FROM Scan ORDER BY ScanId DESC LIMIT 1''')
		result = c.fetchone()
		self.scantime = result[1]
	
	
	def __del__(self):
		self.__close_connection_()
	