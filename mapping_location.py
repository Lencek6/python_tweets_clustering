import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import os
os.environ["PROJ_LIB"] = "C:\\Users\\RokL\\Miniconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap





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

    lon = df['lon'].tolist()
    lat = df['lat'].tolist()

    #print(df)
    #clustering KMeans
    test_cluster = KMeans(n_clusters=8)
    test_cluster.fit(df)
    color1 = np.array(['red', 'green', 'blue', "yellow", "purple", "orange", "black", "brown"])

    # A basic map
    m = Basemap(llcrnrlon=-160, llcrnrlat=-75, urcrnrlon=160, urcrnrlat=80)
    m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
    m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
    m.drawcoastlines(linewidth=0.1, color="white")

    # Add a marker per city of the data frame!
    m.plot(df['lat'], df['lon'], linestyle='none', marker="o", markersize=5, alpha=0.6, c="orange",
           markeredgecolor="black", markeredgewidth=1)
    plt.show()

if __name__== '__main__':
    main()