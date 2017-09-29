
# coding: utf-8

# In[1]:

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import time
import sys
import socket


# In[2]:

atoken = '913446045853429761-zMeEJRO6Cr0fJelyd1ul1o7t8GZkG1Y'
asecret = 'oVZkO4Ui7WAbtub4prfCmGCVrdAdUErCweNVS74eVu32a'
ckey = 'jHvYx5OgcJCqX7HXmNfsZuHIS'
csecret = 'hiCjYySNZURaMxZI04qI7ey8ARvFidNAFlv8hjaEkKfSekQJ52'


# In[3]:

class TweetsListener(StreamListener):
 
    def __init__(self, csocket):
        self.client_socket = csocket
 
    def on_data(self, data):
        try:
            print(data.split('\n'))
            self.client_socket.send(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


# In[4]:

def sendData(c_socket):
 
   
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, TweetsListener(c_socket))
 
    #filter Twitter Streams to capture data by the keywords: 'python'
    stream.filter(track=['trump'])


# In[ ]:

if __name__ == "__main__":
    s = socket.socket()     # Create a socket object
    host = "172.31.60.179"      # Get local machine name
    port = 1233             # Reserve a port for your service.
    s.bind((host, port))    # Bind to the port
 
    print("Listening on port: %s" % str(port))
 
    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()        # Establish connection with client.
 
    print( "Received request from: " + str( addr ) )


# In[ ]:

sendData(c)


# In[ ]:




# In[ ]:



