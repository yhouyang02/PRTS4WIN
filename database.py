# Access MySQL through pymysql
import pymysql

'''
[PRIVATE] NOT to be used in external classes. 
Return Type: SQL Connection
Returns the connection to PRTS's admin account
'''
def get_connection():
	return pymysql.connect(
		#REMINDER: to modify 'host' and 'port' if updated
		host = 'prts.tooo.top',
		port = '36850', 
		user = 'admin', 
		password = 'PRTS2020!', 
		database = 'test', 
		charset = 'utf8'
	)


'''
[PUBLIC] Free to use in all classes. 
Return Type: list[]
Returns a list containing a row of data from DB


Example(in external files): 
import database as db
sql_query = "SELECT * FROM tb_operator"
db.query_data(sql_query)
'''
def query_data(sql):
	conn = get_connection()
	try:
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursors.execute(sql)
		return cursor.fetchall()
	finally:
		#closing connection
		conn.close()


'''
[PUBLIC] Free to use in all classes. 
Return Type: void
To INSERT data in DB
'''
def insert_data(sql):
	conn = get_connection()
	try:
		cursor = conn.cursor()
		cursor.execute(sql)

		# committing changes
		conn.commit()
	finally:
		# closing connection
		conn.close()


'''
[PUBLIC] Free to use in all classes. 
Return Type: void
To UPDATE data in SB

Example:
import database as db
sql_update = "UPDATE tb_operator SET class='术师' where id='伊芙利特'"
update_data(sql_update)
'''
def update_data(sql):
	conn = get_connection()
	try:
		cursor = conn.cursor()
		cursor.execute(sql)

		# committing changes
		conn.commit()
	finally:
		# closing connection
		conn.close()