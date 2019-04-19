import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Reading key tweets.json file to list of tweets
tweets = []
with open("key_tweets.json", 'r') as infile:
    for line in infile:
        tweets.append((json.loads(line)))

# filter words that we don't want to use
filter_words = ["https", "co", "rt", "c", "sv", "yo", "gwkrt", "amp", "gwk"]


def resubstitute(text):
    # resubstitute function, re-subs all filter_words elements in our tweets text
    this = text
    for i in filter_words:
        this = re.sub(i, "", this)
    return this


tweets_text = []

# loop trough all tweets that we read from .json file, and pre-process them
for t in tweets:
    tmp = (re.sub("[^a-zA-Z]", " ", t['text']))
    tmp = tmp.lower()
    tmp = resubstitute(tmp)
    tweets_text.append(tmp)

# term frequency–inverse document frequency on our tweets text
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(tweets_text)

# kMeans algorithm on TFIDF results
true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

# printing top 5 words per cluster
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind]),
    print

# predictions - you can put any string in predict_me var and see which cluster does it fit in
print("\n")
print("Prediction")
predict_me = "bring me the beer"

Y = vectorizer.transform([predict_me])
prediction = model.predict(Y)
print("cluster number: ", prediction)

# counting documents per cluster
clusters = model.fit_predict(X)
clusters = list(clusters)
print(clusters.count(0), clusters.count(1), clusters.count(2))

# cosine similarity between corpus vectors and document vectors we want to calculate similarity - corpus VS predict_me
cos = cosine_similarity(X, Y)
print(cos)

# get documents with above average cosine similarity: if cos similarity > 0.5
ideal = np.where(cos > 0.5)

# tumple to list
list = list(ideal)

# print each document that has similarity > 0.5, walk trough indexes and print them, indexes are in 1st array element!
print("----------------------")
for f in list[0]:
    print(tweets_text[int(f)], cos[int(f)])