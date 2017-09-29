
# coding: utf-8

# In[5]:


from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import time
import sys
import socket


# In[6]:


#Variables that contains the user credentials to access Twitter API 
#atoken = '619074563-ktrVz48c9sXzfSIpQUzejNeQexaqM08AIHMNwSgY'
#asecret = 'Eir4SQRBnitqbLneYt9lZr0fS6JoSXpZaMtpVlEPYDZFn'
#ckey = '6uG3fQzgXht2s8yvEOT0ZOxPE'
#csecret = 'EMz6zARpqPuVy2Fnd9Q4RswtY7lbLEC2Sx4ANi1aJEUDrg62uN'


# In[7]:


atoken = '913446045853429761-zMeEJRO6Cr0fJelyd1ul1o7t8GZkG1Y'
asecret = 'oVZkO4Ui7WAbtub4prfCmGCVrdAdUErCweNVS74eVu32a'
ckey = 'jHvYx5OgcJCqX7HXmNfsZuHIS'
csecret = 'hiCjYySNZURaMxZI04qI7ey8ARvFidNAFlv8hjaEkKfSekQJ52'


# In[ ]:


class StdOutListener(StreamListener):
 
    def on_data(self, data):
        tweet = json.loads(data)
        print(json.dumps(tweet['text']).encode("utf-8"))
        time.sleep(0.5)
        return data
 
    def on_error(self, status):
        print (status)
 
 
if __name__ == '__main__':
 
    #handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, l)
 
    #filter Twitter Streams to capture data by the keywords: 'python'
    stream.filter(track=['trump'])


# In[ ]:


class tweetsListener(StreamListener):
    def _init_(self,csocket):
        self.client_socket = csocket
    def on_data(self,data):
        try:
            msg = json.loads(data)
            print(msg['created_at'])
            print(msg['user']['name'])
            print(msg['user']['location'])
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on data:%s" %str(e))
        return True
    def on_error(self,status):
        print(status)
        return True


# In[ ]:


def sendData(c_socket):
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitter_stream = Stream(auth,tweetsListener(c_socket))
    twitter_stream.filter(track=['trump'])


# In[ ]:


s = socket.socket()


# In[ ]:


host = "10.140.167.214"
port = 5555


# In[ ]:


s.bind((host,port))
print("listening on the port %s" % str(port))


# In[ ]:


s.listen(5)


# In[ ]:


c, addr = s.accept()


# In[ ]:


print("Received Request from :" +str( addr ))


# In[ ]:


sendData(c)


# In[ ]:


#sentiment polarity extraction by TextBlob
def sentimentTextBlob(tweet):
  processedtestTweet = processTweet(tweet)
  #sentiment extraction by TextBlob
  sentimental = TextBlob(processedtestTweet)
  sentiment = sentimental.sentiment.polarity
  if sentiment<0.0:
      sentiment='negative'
  elif sentiment>0.1:
        sentiment='positive'
  else:
    sentiment='neutral'
  return sentiment


# In[ ]:


def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end


# In[ ]:




