import flask
from urllib2 import urlopen
from json import load
import socket
import fcntl
import struct

def netOs():
	networkOs = []
	for line in open("Network_OS.txt", "r").readlines():
		line = line + "<br>"
		networkOs.append(line)
	
	return networkOs

def publicIP():
	my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
	return my_ip

def privateIP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	privip = socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915, 
		struct.pack('256s', 'eth0'[:15])
	)[20:24])
	return privip

def fping():
	fpingUp = []
	for line1 in open("fpingUp.txt", "r").readlines():
		line1 = line1 + "<br>"
		fpingUp.append(line1)
	return fpingUp

