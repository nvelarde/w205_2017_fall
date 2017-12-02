# importing required python libraries

import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# connecting to tcount database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# error handling block

user_arguments = sys.argv[1:]
number_arguments = len(user_arguments)

if number_arguments > 1:
	print "You have entered too many arguments.  Please enter the word for which you want the total number of occurrences after the program name, finalresults.py, OR enter no arguments after the program name if you want to return all the words in the stream and their total count of occurrences."
	exit()

# scenario where user provides zero arguments (i.e., no word to query the database), number_arguments = 0, therefore, code will return all words in the stream with their total number of occurrences in alphabetical order

elif number_arguments == 0:
	cur = conn.cursor()
	# SQL statement to select word, count FROM tweetwordcount table in alphabetical order (ASC default)
	cur.execute("SELECT word, count FROM tweetwordcount ORDER BY word")
	records = cur.fetchall()
	print "All words in the Twitter stream and their respective number of occurrences:"
	print "\n"
	for rec in records:
		print "word = ", rec[0]
		print "count = ", rec[1], "\n"
	conn.commit()
	conn.close()

# scenario where user correctly provides a word in the form of a command line argument to query the database - code will return the word and the number of occurrences if the word is in tweetwordcount, if not, notify the user that the word was not captured in the Twitter stream and is not in the table

else:
	uword = sys.argv[1]
	uword_occurrences = 0

	cur = conn.cursor()
	cur.execute("SELECT word, count FROM tweetwordcount")
	records = cur.fetchall()

	for rec in records:
		if rec[0] == uword:
			print "Total number of occrrences of \"%s\" is: %s" %(rec[0], rec[1])
			uword_occurrences =+ 1

	if uword_occurrences == 0:
		print "There were no occurences of \"%s\" in the captured Twitter stream" %(uword)

	conn.commit()
	conn.close()

