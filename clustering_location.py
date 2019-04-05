import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

pd.set_option('display.max_colwidth', 300)

def main():
    tweets = []
    with open("key_tweets.json", 'r') as infile:
        for line in infile:
            tweets.append((json.loads(line)))

    tweets_W_coordinates = []
    for t in tweets:
        if t['coordinates'] != None:
            tweets_W_coordinates.append(t)

    populate_tweet_df(tweets_W_coordinates)


def populate_tweet_df(tweets):

    df = pd.DataFrame()
    #df['text'] = list(map(lambda tweet: tweet['text'], tweets))
    df['lon'] = list(map(lambda tweet: tweet['geo']['coordinates'][0], tweets))
    df['lat'] = list(map(lambda tweet: tweet['geo']['coordinates'][1], tweets))
    #df['friends_count'] = list(map(lambda tweet: tweet['user']['friends_count'], tweets))


    #print(df)
    #clustering KMeans
    test_cluster = KMeans(n_clusters=8)
    test_cluster.fit(df)
    color1 = np.array(['red', 'green', 'blue', "yellow", "purple", "orange", "black", "brown"])

    #plotting results
    plt.scatter(df['lat'], df['lon'], c=color1[test_cluster.labels_])
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


if __name__== '__main__':
    main()