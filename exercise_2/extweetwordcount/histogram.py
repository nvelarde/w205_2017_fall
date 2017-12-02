# importing required python libraries

import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# connecting to tcount database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# user entered arguments error handling

user_arguments = sys.argv[1:]
number_arguments = len(user_arguments)

if number_arguments != 2:
	print "This program requires exactly 2 arguments.  Both arguments must be positive integers.  Please re-run and provide the two integers as arguments -- separated by spaces -- after histogram.py which will respectively represent the lower and upper bound of the number of occurrences for words captured in the Twitter stream."
	exit()

# setting the lower and upper boundaries -- in the event the user entered in the upper bound first 
# and the lower bound second 
# for the historgram and ensuring those numerical bounds are integers 
# catching the ValueError that would result if argument was a float

try:
	k1 = min(int(sys.argv[1]),int(sys.argv[2]))
	k2 = max(int(sys.argv[1]),int(sys.argv[2]))

except ValueError:
	print "ERROR - Both program arguments must be positive integers, please re-run program and try again."

# SQL querry that returns all the words in tweetwordcount with a total number of occurrences greater than or equal to k1, and less than or equal to k2

# handles scenario where user enters a negative number for an argument

if (k1 <= 0) or (k2 <= 0):
	print "ERROR - Both program arguments must be positive integers, please re-run program and try again."
	exit()

# interacting with tcount to deliver desired information

cur = conn.cursor()

# BETWEEN operator in SQL is inclusive so query will return words with counts greater than or equal to k1 and less than or equal to k2

cur.execute("SELECT word, count from tweetwordcount WHERE count BETWEEN %s AND %s ORDER BY count DESC, word", (k1, k2))
records = cur.fetchall()
for rec in records:
	print "%s: %s" %(rec[0], rec[1])

conn.commit()
