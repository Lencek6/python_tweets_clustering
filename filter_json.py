import json
import fileinput

count_empty = 0
filter_list = ['beer', 'ale', 'brew', 'stout']

#read json file line by line. Every second line is empty, filtering only en lang tweets.
for line in fileinput.input(['tweets.json']):
    if line.strip():
        tweet = json.loads(line)
        if tweet["lang"]=="en":
            if(any(i in tweet["text"] for i in filter_list)): #checks if any of the filter_list items is in tweets text
                print(tweet["text"])
                file = open("key_tweets.json", "a")
                file.write(line)
                print("---------------------------------")

    else:
        count_empty = count_empty + 1


print(count_empty/2, len(tweet))


#52820 tweets positive

