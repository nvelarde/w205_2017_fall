# this python program creates database (tcount) and table (tweetwordcount) where we will insert tweets (word and count)

# importing libraries to interact with postgres

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# establishing connection to postgres

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

# CREATE(ing) tcount DATABASE in postgres -- DROP if already exists and CREATE a new one

try:
	# CREATE DATABASE cannot run inside a transaction
	conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = conn.cursor()
	cur.execute("DROP DATABASE IF EXISTS tcount")
	cur.execute("CREATE DATABASE tcount")
	cur.close()
	conn.close()
	print "tcount DATABASE successfully created"
	print "\n"
except:
	print "ERROR - unable to create tcount DATABASE"

# connecting to tcount database to CREATE tweetwordcount TABLE

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# CREATE(ing) tweetwordcount TABLE in tcount DATABASE

try:
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS tweetwordcount")
	cur.execute('''CREATE TABLE tweetwordcount
	   (word TEXT PRIMARY KEY NOT NULL,
	   count INT NOT NULL);''')
	conn.commit()
	cur.close()
	conn.close()
	print "tweetwordcount TABLE successfully created"
except:
	print "ERROR - unable to create tweetwordcount TABLE"
