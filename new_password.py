import sqlite3


conn = sqlite3.connect('pwdatabase.db')
c = conn.cursor()

def new():
	conn = sqlite3.connect('pwdatabase.db')
	c = conn.cursor()

	website = input("Enter website: ")
	username = input("Enter username: ")
	password = input("Enter password: ")

	c.execute("""INSERT INTO passwords
		(website, username, password) VALUES
		(?, ?, ?)
		""", (website, username, password))
	conn.commit()
	c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1")
	result = c.fetchone()
	for row in result:
		print(row)
	conn.close()
	input("Press Enter to Exit")

	return