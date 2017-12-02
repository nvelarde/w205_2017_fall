# importing general python libraries

from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter

# importing streamparse bolt library

from streamparse.bolt import Bolt

# importing pyscopg2 library and extensions to interact with postgres

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):

	def initialize(self, conf, ctx):
		self.counts = Counter()

		# connect to database tcount
		self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

	def process(self, tup):
		word = str(tup.values[0])

		# creating a cursor data structure to execute SQL statements in postgres
		cur = self.conn.cursor()

		# code for incrementing the word count in postgres

		# updating count in tweetwordcount table if the incoming word is already in table
		cur.execute("UPDATE tweetwordcount SET count=count+1 WHERE word=%s",(word,))

		# inserting word and count of 1 for words not present in table 
		# if cur.rowcount==0, indicating that no rows were updated by the prior UPDATE statement, then INSERT word with count 1

		if cur.rowcount == 0:
			cur.execute("INSERT INTO tweetwordcount (word, count) VALUES (%s, 1)",(word,))

		# commiting the updates to the database

		self.conn.commit()

		# Increment the local count

		self.counts[word] += 1
		self.emit([word, self.counts[word]])

		# Logging the count - to see the topology running on screen

		self.log('%s: %d' % (word, self.counts[word]))
