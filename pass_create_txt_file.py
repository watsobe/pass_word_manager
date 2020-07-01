import os.path

def check_existence():
	# This function checks for the existence of user account file
	# and will create the file if it doesn't exist
	if os.path.exists('accts.txt'):
		pass
	else:
		file = open('accts.txt', 'write')
		file.close()

def append_new_uinfo():
	# This function will append new pwd, UID, website to the accounts file
	file = open('accts.txt', 'append')

	print()
	print()

	# Request user account information
	user_name = input('Please enter the user name: ')
	password = input('Please enter the password: ')
	website = input('Please enter the website address: ')

	print()
	print()

	usr_id = 'User Name: ' + user_name + '\n'
	pwd = 'Password: ' + password + '\n'
	web = 'Website: ' + password + '\n'

	file.write('*********************************\n')
	file.write(usr_id)
	file.write(pwd)
	file.write(web)
	file.write('*********************************\n')
	file.write('\n')
	file.close

def read_uinfo():
	# This function reads the text file and prints ALL user information (yikes!)
	file = open('accts.txt')
	content = file.read()
	file.close()
	print(content)
