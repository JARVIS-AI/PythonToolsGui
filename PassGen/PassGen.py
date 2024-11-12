#!/usr/bin/env python3

import random
import string

# tabe akhz vorodi
def get_yes_no_input(prompt):
	while True:
		response = input(prompt).lower()  #lowercase
		if response in ['yes', 'y', 'no', 'n']:
			return response in ['yes', 'y']
		else:
			print("ALERT: faghat (y) ya (n)")
			
# tabe ijad password
def generate_password(length, use_lower, use_upper, use_numbers, use_symbols):
	characters = ''
	
	if use_lower:
		characters += string.ascii_lowercase
	if use_upper:
		characters += string.ascii_uppercase
	if use_numbers:
		characters += string.digits
	if use_symbols:
		characters += string.punctuation
		
	if not characters:
		return "Che passwordi mikhay, tamam gozine haro rad kardi!"
	
	# ijad pass ba character haye mojaz
	password = ''.join(random.choice(characters) for _ in range(length))
	return password

# porsesh soal
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
			max_length = int(input("Hadeaksar tool ramz (bayad >= hadeaghal bashe) :"))
			if max_length >= min_length:
				break
			else:
				print(f"hadeaksar bayad >= {min_length} bashad")
		except ValueError:
			print("Ye addad motabar vared kon")
	
	
	use_lower = get_yes_no_input("Dar ramz az character kochic estefade beshe ? (yes/no): ")
	use_upper = get_yes_no_input("Dar ramz az character bozorg estefade beshe ? (yes/no): ")
	use_numbers = get_yes_no_input("Dar ramz az addad estefade beshe ? (yes/no): ")
	use_symbols = get_yes_no_input("Dar ramz az sambol estefade beshe ? (yes/no): ")
	
	if not (use_lower or use_upper or use_numbers or use_symbols):
		print("Che ramzi besazam ? Dobare RUN kon")
		return
	
	
	# ijad pass
	with open('password.txt', 'w') as file:
		for i in range(num_passwords):
			password_length = random.randint(min_length, max_length)
			password = generate_password(password_length, use_lower, use_upper, use_numbers, use_symbols)
			print(f"Ramz {i+1}: {password}")
			file.write(f"Ramz {i+1}: {password}\n")
	
	print("Password ha dar file password.txt save shodan!")
	
if __name__ == "__main__":
	main()
	