# imports
from twython import TwythonStreamer

# dev infos
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

# streamer class
class Streamer(TwythonStreamer):
    def on_success(self, data):
    	# location of user
    	location = data['user']['location'].lower()
    	
    	# id of tweet
    	idstr = data['id_str'].encode('utf-8')
    	
    	# publication date
        time = data['created_at'].encode('utf-8')

        # concat
        line = "%s,%s\n" %(idstr,time)

        # build database for london and paris
        if 'london' in location :
        	open("db_london","a").write(line)
        if 'paris' in location :
        	open("db_paris","a").write(line)

    def on_error(self, status_code, data):
        print status_code

# initialize api
api = Streamer(consumer_key, consumer_secret, access_token_key, access_token_secret)

# track keywords
tracks = "#Runtastic session course pied, #Runtastic finished run, #Runkeeper just completed run, #MapMyRun I ran, #MapMyRun j'ai couru, #nikeplus I just ran, #nikeplus je viens de courir"

# launch stream
api.statuses.filter(track=tracks)