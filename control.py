#!/usr/bin/python
import sys
import os

ml = "/dev/launcher0"
commands = {'u': 0x01,
			'd': 0x02,
			'l': 0x04,
			'r': 0x08,
			'f': 0x10 }

def move(fd, movement):
	for i in movement:
		if i in commands:
			command |= commands[str(i)]

	os.write(fd,command)

def main():
	fd = os.open(ml, O_WRONLY)
	command = 0x00
	if len(sys.argv) >1:
		for arg in sys.argv[1]:
			movement = eval(arg)
			move(fd, movement)
	else:
		try:
			while 1:
				movement = input().strip()
				move(fd, movement)
		except EOFError:
			os.close(ml)
			pass

main()
