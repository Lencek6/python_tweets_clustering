import json
import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ["PROJ_LIB"] = "C:\\Users\\RokL\\Miniconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap


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
    # method that feeds pandas dataFrame with lon and lat from tweets and map them on card
    df = pd.DataFrame()
    df['lon'] = list(map(lambda tweet: tweet['geo']['coordinates'][0], tweets))
    df['lat'] = list(map(lambda tweet: tweet['geo']['coordinates'][1], tweets))

    # A basic map definition
    m = Basemap(llcrnrlon=-160, llcrnrlat=-75, urcrnrlon=160, urcrnrlat=80)
    m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
    m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
    m.drawcoastlines(linewidth=0.1, color="white")

    # Add a marker per city of the data frame and plot coordinates
    m.plot(df['lat'], df['lon'], linestyle='none', marker="o", markersize=5, alpha=0.6, c="orange",
           markeredgecolor="black", markeredgewidth=1)
    plt.show()


if __name__ == '__main__':
    main()