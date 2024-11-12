"""
LICENSED TO: JARVIS-AI
--------------------------------------------
	THIS CODE IS LICENSED UNDER THE PROTECTION
	OF THE USER'S COMMANDS AND WILL BE TERMINATED
	IF THE INTEGRITY OF THE MISSION IS COMPROMISED.
	
	USER: You now have control over the Password Generator.
	You may modify, distribute, or use this code as per
	your needs, but beware... unauthorized tampering
	might trigger defense protocols.
	
	https://github.com/JARVIS-AI
	©2024 Stark Enterprises. All rights reserved.
--------------------------------------------
"""

import random
import string
import sys

c_v = None
v_n = {}

u_l = [chr(i) for i in range(65, 91)]
l_l = [chr(i) for i in range(97, 123)]

def main():
	try:
		num_passwords = int(input("Chandta password mikhay ? "))
	except ValueError:
		print("Ye addad motabar vared kon!")
		return
	
	while True:
		try:
			min_length = int(input("Hadeaghal tool ramz (Bozorgtar mosavi 6) :"))
			if min_length >= 6:
				break
			else:
				print("hadeaghal >= 6")
		except ValueError:
			print("Ye addad motabar vared kon")
			
	while True:
		try:
			max_length = int(input(f"Hadeaksar tool ramz (bayad >= hadeaghal bashe {min_length}) :"))
			if max_length >= min_length:
				break
			else:
				print(f"hadeaksar bayad >= {min_length} bashad")
		except ValueError:
			print("Ye addad motabar vared kon")
			
	up = get_y_n_input("Dar ramz az character bozorg estefade beshe ? (yes/no): ")
	number = get_y_n_input("Dar ramz az addad estefade beshe ? (yes/no): ")
	sym = get_y_n_input("Dar ramz az sambol estefade beshe ? (yes/no): ")
	low = get_y_n_input("Dar ramz az character kochic estefade beshe ? (yes/no): ")
	
	c_i()
	
	if not (low or up or number or sym):
		print("Che ramzi besazam ? Dobare RUN kon")
		return
	
	try:
		with open('pass.txt', 'w') as file:
			for i in range(num_passwords):
				password_length = random.randint(min_length, max_length)
				password = gen_p(password_length, up, number ,sym, low)
				print(f"Ramz {i+1}: {password}")
				file.write(f"Ramz {i+1}: {password}\n")
		print("Password ha dar file pass.txt save shodan!")
	except IOError:
		print("Khata dar save kardan file, lotfan dastresi ra check kon!")

def c_i():
	if c_v != 256:
		print("A")
		sys.exit(1)
	
	if 'u_l' not in globals() or not isinstance(u_l, list):
		print("B")
		sys.exit(1)

	if 'l_l' not in globals() or not isinstance(l_l, list):
		print("C")
		sys.exit(1)

def get_y_n_input(prompt):
	global c_v, v_n
	c_v = 256
	
	v_n = {
		'u_l': 'u_l',
		'l_l': 'l_l'
	}
	
	while True:
		response = input(prompt).lower()
		if response in ['yes', 'y', 'no', 'n']:
			return response in ['yes', 'y']
		else:
			print("dada: faghat (y) ya (n) bzn")

def gen_p(length, up, number ,sym, low):
	d = [chr(i) for i in range(48, 58)]
	s = list('!@#$%^&*()-_=+[]{}|;:,.<>?/`~')

	characters = []
	if up:
		characters += u_l
	if number:
		characters += d
	if sym:
		characters += s
	if low:
		characters += l_l

	if not characters:
		return "Che passwordi mikhay, tamam gozine haro rad kardi!"

	password = ''.join(random.choice(characters) for _ in range(length))
	return password

if __name__ == "__main__":
	main()
	