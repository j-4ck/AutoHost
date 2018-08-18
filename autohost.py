import subprocess
import sys
import os
import socket
from colorama import Fore, Style, init
init()

class s:
	g = Fore.GREEN + '[+] ' + Fore.WHITE
	g2 = Fore.GREEN
	r = Fore.RED + '[!] ' + Fore.WHITE
	y = Fore.YELLOW + '[-] ' + Fore.WHITE

class setup:
	def __init__(self, name):
		self.name = name

	def startapache(self):
		print s.y + 'Starting Apache 2 server...'
		subprocess.call('service apache2 start',shell=True)
		print s.g + 'Server started!'
	def rmhtml(self):
		try:
			os.remove('/var/www/html/index.html')
		except:
			pass
		print s.g + 'Removed index.html!'

	def getip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8",80))
		return s.getsockname()[0]

	def writepayload(self):
		print s.y + 'Writing payload output file...'
		try:
			f = open(self.name, 'r')
			f1 = open('/var/www/html/' + self.name, 'a')
		except Exception as e:
			print s.r + 'Unable to open files! ' + str(e)
			sys.exit()

		for line in f:
			f1.write(line)
		print s.g + 'File successfuly written!'
def main():
	if len(sys.argv) < 2:
		print 'Usage:\n\t' + sys.argv[0] + ' [payloadfile.example]'
		sys.exit()
	print Style.BRIGHT + s.g2 + '''
    ___         __        __  __           __ 
   /   | __  __/ /_____  / / / /___  _____/ /_
  / /| |/ / / / __/ __ \/ /_/ / __ \/ ___/ __/
 / ___ / /_/ / /_/ /_/ / __  / /_/ (__  ) /_ 
/_/  |_\__,_/\__/\____/_/ /_/\____/____/\__/ 
	'''
	se = setup(sys.argv[1])
	try:
		choice = raw_input(s.y + 'Would you like to remove /var/www/html/index.html? [y/n] ')
	except KeyboardInterrupt:
		print ''
		sys.exit()
	if choice.lower().strip() == 'y':
		se.rmhtml()
	se.startapache()
	se.writepayload()
	print s.g + 'Link created: http://' + se.getip() + '/' + sys.argv[1]

if __name__ == '__main__':
	main()
