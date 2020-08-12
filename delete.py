import sqlite3
import os

def delete_password():
	conn = sqlite3.connect('pwdatabase.db')
	c = conn.cursor()
	print(conn)
	print("\nYou are deleting your password by website name")
	user_input = input("Enter website: ")

	c.execute("""DELETE FROM passwords
		WHERE website = ?
		""", (user_input,))
	conn.commit()
	conn.close()
	print("Your password has now been deleted")
	input("Press Enter to Exit")
	os.system('clear')
	return