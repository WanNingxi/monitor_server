import SocketServer
import os


f = open('IP_address.txt')			#increase the monitor IP_address
address_list = []
while True:	
	IP_address = f.readline()
	address_list.append(IP_address)
	if len(IP_address) == 0:
		break




class MyTCPHandler(SocketServer.BaseRequestHandler):
	"""
	The RequestHandler class for our server.
	It is instantiated once per connection to the server, and must
	override the handle() method to implement communication to the
	client.
	"""

	def handle(self):
		#print self.client_address[0],address_list[1]			
		#print type(self.client_address[0]),type(address_list[1])
		

		#judge whether the IP_address is needed to monitor
		for i in range(0,3):
			if self.client_address[0] == address_list[i][:-2]:
				print 'This server is monitored by wanningxi'
				

				#write the monitor information into the 'monitor_information.html'
				while True:
					#os.chdir('/home/Reacher/python/')
					file_name = open('/home/Reacher/python/mysite/polls/templates/test.html','a')
		        		# self.request is the TCP socket connected to the client			
		        		self.data = self.request.recv(4096).strip()
					if not self.data:
						break
		        		print "{} wrote:".format(self.client_address[0])
					print self.data
					file_name.write(self.data)					
		       			# just send back the same data, but upper-cased
		        		self.request.sendall(self.data.upper())
				
				break
				file_name.close()		
			else: 
				print 'This server is not monitored by wanningxi'
				


		


if __name__ == "__main__":                                           
	HOST, PORT = '', 9998

	# Create the server, binding to localhost on port 9999
	server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()