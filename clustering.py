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

    # calling method on results
    populate_tweet_df(tweets)


def populate_tweet_df(tweets):
    # method that feeds pandas dataFrame with followers count and friends count from tweets and performs clustering
    df = pd.DataFrame()
    df['followers_count'] = list(map(lambda tweet: tweet['user']['followers_count'], tweets))
    df['friends_count'] = list(map(lambda tweet: tweet['user']['friends_count'], tweets))

    # clustering using KMeans algorithm, using random init for centroid
    test_cluster = KMeans(n_clusters=3, init = 'random')
    test_cluster.fit(df)
    color1 = np.array(['red', 'green', 'blue'])

    # plotting results
    plt.scatter(df['followers_count'], df['friends_count'], c=color1[test_cluster.labels_])
    plt.xlabel('Followers count')
    plt.ylabel('Friends count')

    # plotting centroids
    centers = np.array(test_cluster.cluster_centers_)
    plt.scatter(centers[:, 0], centers[:, 1], marker="*", color='black', s=100)
    print(centers)
    plt.show()


if __name__ == '__main__':
    main()