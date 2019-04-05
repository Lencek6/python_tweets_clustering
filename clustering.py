import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def main():
    tweets = []
    with open("key_tweets.json", 'r') as infile:
        for line in infile:
            tweets.append((json.loads(line)))
    populate_tweet_df(tweets)


def populate_tweet_df(tweets):
    df = pd.DataFrame()
    #df['text'] = list(map(lambda tweet: tweet['text'], tweets))
    df['followers_count'] = list(map(lambda tweet: tweet['user']['followers_count'], tweets))
    df['friends_count'] = list(map(lambda tweet: tweet['user']['friends_count'], tweets))

    #clustering KMeans
    test_cluster = KMeans(n_clusters=3)
    test_cluster.fit(df)
    color1 = np.array(['red', 'green', 'blue'])

    #plotting results
    plt.scatter(df['followers_count'], df['friends_count'], c=color1[test_cluster.labels_])
    plt.xlabel('Followers count')
    plt.ylabel('Friends count')
    plt.show()


if __name__== '__main__':
    main()