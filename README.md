# FYP-Honeypot
This repository contains malicious files meant for educational purposes only.

## Project Objective
Build a robust and attractive IoT Honeypot Environment with the available IoT devices and IT infrastructure

## Project Specifications
Build IoT environment and configure IoT devices  
●	Setup of Raspberry Pi  
●	Setup of Sense Hat  
●	Setup of EdgeX Foundry (Ubuntu VM)  

Create data visualisation using visualisation platforms  
●	Send data from Raspberry Pi to EdgeX Foundry (using python script to communicate REST API)  
●	Export data from MQTT broker to InfluxDB  
●	Using Grafana, create a graphical dashboard using data collected in InfluxDB  

Export and upload data to AWS IoT Core  
●	Export the data from EdgeX Foundry using MQTT  

Create use cases (as red team) to attack IoT system  
●	Password Brute Force (via SSH)  
●	Trojan  
●	Malware Dropper  
●	Keylogger  
●	Botnet  
●	Denial of Service  
●	SQL Injection  

Monitor traffic on Wireshark and create rules and alerts using Snort  
●	Analyse the traffic on Wireshark and examine the packets for malicious activities  
●	Identify any Indicators of Compromise for each attack  
●	Creation of rules using the IOCs  
●	Test out the rules for alerts when attacks are detected  
