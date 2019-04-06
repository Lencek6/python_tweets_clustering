import json
import fileinput

# declaration of counter for usable and not usable tweets
count_usable = 0
count_nonusable = 0
filter_list = ['beer', 'ale', 'brew', 'stout']

# read json file line by line. Every second line is empty, filtering only en lang tweets.
for line in fileinput.input(['tweets.json']):
    if line.strip():
        tweet = json.loads(line)
        if tweet["lang"]=="en":
            # checks if any of the filter_list items is in tweets text and saves them to key_tweets.json for further use
            if(any(i in tweet["text"] for i in filter_list)):
                count_usable = count_usable + 1
                print(tweet["text"])
                #file = open("key_tweets.json", "a")
                #file.write(line)
                print("---------------------------------")
    # increments counter for not usable tweets
    else:
        count_nonusable = count_nonusable + 1

# printing number of usable and nonusable tweets. For nonusable is /2, because every second line in tweets.json is empty
print('Number of usable tweets: ', count_usable)
print('Number of nonusable tweets: ', count_nonusable/2)


