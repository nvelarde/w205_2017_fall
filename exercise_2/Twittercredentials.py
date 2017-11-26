import tweepy

consumer_key = "RSNZo0fq5QEYrxJrPUdJcq7MI";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "6ijPYGpwiOtxndwePvf03h1iz8B4w3xXWmzZWAEzfUHqc3eGJh";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "934652729636433921-bKxvK8AlvxMvFVOnvFgUnzpMyDEMxqI";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "qSv3sxdpEqR9DlkK9Vn0T9qIpIx5jasYmJqEAyYvZNT9a";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



