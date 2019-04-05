from collections import Counter
from nltk.util import everygrams
import json
import pandas as pd
import re
from nltk.tokenize import TweetTokenizer
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud

#Reading key tweets.json file to list of tweets
tweets = []
with open("key_tweets.json", 'r') as infile:
    for line in infile:
        tweets.append((json.loads(line)))

#Declaration of data object for storing tweets' info and all_text for storing all tweets text
data = {'text': [], 'hour': [], 'user': []}
all_text = ''

#Loop trough tweets list and storing them into object. Date is converted to hour for better presenatation in histogram
for t in tweets:
    all_text = all_text + t['text']
    data['text'].append(t['text'])
    tweet_date = pd.to_datetime(t['created_at'])
    data['hour'].append(tweet_date.hour)
    data['user'].append(t['id'])

#creating DataFrame from data and expanding terminal display width for nicer looks of output
pd.set_option('display.max_colwidth', 150)
df = pd.DataFrame(data)

#showind DataFrame as histogram x axis -> hours, y axis -> unique tweets at this hour
df.groupby('hour')['text'].nunique().plot(kind='bar', title='Universal Time Zone')

#Transforming text only into letters and lower case & tokenizing text
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
all_text = re.sub("[^a-zA-Z]", " ", all_text)
all_text = all_text.lower()
word_tokens = tknzr.tokenize(all_text)

#defining stop words and filter words, and applying filters
stop_words = set(stopwords.words('english'))
filter_words = ["https", "co", "rt", "c", "sv", "yo", "gwkrt", "amp"]
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = [w for w in filtered_sentence if not w in filter_words]

#getting n-grams of tokenized text, lenght--> 1 word
every_grams = Counter(everygrams(filtered_sentence, min_len=1, max_len=1))

#Prepearing text for wordcloud
polished_text = (" ").join(filtered_sentence)
polished_text = polished_text.upper()

#Creating WordCloud from polished text
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10,
                collocations = False,
                ).generate(polished_text)

#Plot the WordCloud image and HistoGram of dataFrame
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()


