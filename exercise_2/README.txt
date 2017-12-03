================================================================================
Introduction
================================================================================

This streaming application captures and processes live tweets and aggregates 
the results in a postgres database.  The user can then use two serving
scripts to perform analytics on the stored data.

================================================================================
How to Run this Application
================================================================================

First, you will need to start up an instance of the following AMI:

AMI Name: UCB MIDS W205 EX2-FULL
AMI ID: ami-d4dd4ec3

Out of the box, this AMI has most, but not all of the technologies to run this
application (python, postgres, hadoop, streamparse).

Once the instance is started and you have established a connection, you will 
need to attach and mount your EBS volume at /data.

Start up postgres:

$ /data/start_postgres.sh

You will need to install psycopg (to connect python and postgres) and tweepy 
(a python module that interacts with Twitter).

Install psycopg by running:

$ pip install psycopg2

Install tweepy by running:

$ pip install tweepy

Switch user from root to w205 and clone my w205_2017_fall repository from
GitHub.

Now navigate to the extweetwordcount directory as it contains all of the files
required to run the application.  Here is the full path:

w205_2017_fall/exercise_2/extweetwordcount

Once in extweetwordcount, run:

$ python setup_db.py

setup_db.py is a python script creates the tcount database and corresponding 
tweetwordcount table in postgres where the parsed tweets will be stored.

Now, we are ready to capture tweets!

Enter:

$ sparse run

After some start-up, you will see a continuous log of parsed words from 
captured tweets onscreen.

In the background, the words and their respective counts are being inserted/
updated to the tcount database in the tweetwordcount table.  The
tweetwordcount 
table has two columns, word (primary key, string) and count (integer).  

Once you feel you have collected enough tweets, you can stop the process by
CNTRL + C (holding down the control key and c at the same time).

Now for some analysis on our captured tweets.  We have provided you with two
convenient serving scripts, finalresults.py and histogram.py, that query the
database and return specific results.

================================================================================
Running finalresults.py
================================================================================

finalresults.py finds the number of occurrences a word, "trump", for example
appears in the stream.  "trump" is the argument passed to the program,
finalresults.py.  To run this search, type the following:

$ python finalresults.py trump

The number of occurrences that trump (or any word passed as the argument)
appears in the stream will be returned.

Running finalresults.py without an argument will return all the words in the
stream and their respective total number of occurrences, sorted
alphabetically.
To execute this, type:

$ python finalresults.py

================================================================================
Running histogram.py
================================================================================

This script takes two positive integers, k1 and k2, as arguments and returns 
all of the words with a total number of occurrences greater than or equal to
k1, and less than or equal to k2.  You pass the arguments, k1 and k2, after
the program name (histogram.py).  k1 and k2 must be separated by spaces.
For example, let k1 = 3 and k2 = 8:

$ python histogram.py 3 8

================================================================================
Other things you can do with this application
================================================================================

If you desire, you can run more complex querries on the Twitter stream
collected
by writing your own queries in postgres.

To start postgres:

$ psql -U postgres

You will see the postgres prompt:

postgres=#

You can then connect to the tcount database created by our app by:

postgres=# \c tcount

Now can query the tcount database and tweetwordcount table directly.  For 
example, to find the top 20 words by number of occurrences presented in 
descending order, we can enter the following SQL query:

tcount=# SELECT word, count FROM tweetwordcount ORDER BY count DESC LIMIT 20;

ENJOY!
