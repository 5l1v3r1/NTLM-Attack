#coding:utf-8

import sys
import hashlib
import binascii
import threading
import Queue
import time

class NTLM(threading.Thread):
	def __init__(self, system_threads=30):
		threading.Thread.__init__(self)
		self.threads = system_threads
		# Calling Thread variable.
		try:
			# We will test the arguments.
			# To handle incorrect errors.

			self.LIST = sys.argv[1]
			self.NTLM = sys.argv[2]
	
			# I create an exception for the error.
			# For the use of the program.
		except IndexError as e:
			sys.exit(e)

	def NTLModel(self, q):
		"""
		This function will handle the attack.
		
		Parameters
		----
			self : The self parameter is used to manage the supervariables
			q : It's the wordlist for bruteforce hash NTLM.
			
		Return
		----
		Be he will return the password or nothing.
		"""
		while True:
			qet = q.get()
			if(self.NTLM.islower() == False):
				self.NTLM = self.NTLM.lower()

					HASH = hashlib.new('md4', qet.encode('utf-16le')).digest()
					if(binascii.hexlify(HASH) == self.NTLM):
						sys.exit("[+] NTLM : %s:%s" %(self.NTLM, qet))

	def run(self):
		"""
		This function will handle
		the thread system to speed up the
		program and the list.
		"""
		if(self.LIST):
			q = Queue.Queue()
			with open(self.LIST, "r") as files:
				for online in files:
					q.put(online.rstrip("\n\r"))
				self.NTLModel(q)	

			for i in range(int(self.threads)):
				wrapper = threading.Thread(target=self.NTLModel, args=(i, q))
				wrapper.setDaemon(True)
				wrapper.start()
				wrapper.join(600)

			q.join()
		

if __name__ == "__main__":
	NTLM().start()
	
