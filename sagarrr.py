Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
... 
... # Connect to the database
... cnx = mysql.connector.connect(
...     host="localhost",
...     user="username",
...     password="password",
...     database="database"
... )
... cursor = cnx.cursor()
... 
... # Prompt the user for a username
... username = input("Enter a username: ")
... 
... # Construct and execute the SQL query
... query = f"SELECT password FROM users WHERE username = '{username}'"
... cursor.execute(query)
... 
... # Print the results
... result = cursor.fetchone()
... if result:
...     print(f"The password for user '{username}' is: {result[0]}")
... else:
...     print(f"No user with the username '{username}' was found.")
... 
... # Close the connection
