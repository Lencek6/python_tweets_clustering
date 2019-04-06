import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def main():
    # Collecting tweets from .json file line by line
    tweets = []
    with open("key_tweets.json", 'r') as infile:
        for line in infile:
            tweets.append((json.loads(line)))

    # Checking if collected tweets includes coordinates
    tweets_W_coordinates = []
    for t in tweets:
        if t['coordinates'] != None:
            tweets_W_coordinates.append(t)

    # calling method on tweets with coordinates
    populate_tweet_df(tweets_W_coordinates)


def populate_tweet_df(tweets):
    # method that feeds pandas dataFrame with lon and lat from tweets and performs clustering
    df = pd.DataFrame()
    df['lon'] = list(map(lambda tweet: tweet['geo']['coordinates'][0], tweets))
    df['lat'] = list(map(lambda tweet: tweet['geo']['coordinates'][1], tweets))

    # clustering dataFrame on 8 clusters using Kmeans++ init for centroid
    test_cluster = KMeans(n_clusters=8)
    test_cluster.fit(df)
    color1 = np.array(['red', 'green', 'blue', "yellow", "purple", "orange", "black", "brown"])

    # plotting results
    plt.scatter(df['lat'], df['lon'], c=color1[test_cluster.labels_])
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


if __name__ == '__main__':
    main()