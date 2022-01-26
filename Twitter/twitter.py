import csv
import matplotlib as plt

import tweepy
import pandas as pd
from textblob import TextBlob  # for textual analysis

global api  # a global variable for the Twitter API object


def load_auth_file():  # Given authentication file returns a Twitter API object
    # Assuming the auth.k file has the Twitter API tokens
    with open('auth.k') as auth:
        auth_array = auth.readlines()  # loading all
    auth.close()

    access_token2 = auth_array[0].replace("\n", "").strip('"') # Removing the newline character
    access_token_secret2 = auth_array[1].replace("\n", "").strip('"')
    consumer_key2 = auth_array[2].replace("\n", "").strip('"')
    consumer_secret2 = auth_array[3].replace("\n", "").strip('"')

    auth = tweepy.OAuthHandler(consumer_key2, consumer_secret2)  # using inbuilt Tweepy authenticator
    auth.set_access_token(access_token2, access_token_secret2)
    API = tweepy.API(auth)
    return API


def number_pending_requests():  # Returns the number of pending friend request for a user
    numRequest = 0
    for friend_request in api.outgoing_friendships():
        currentUser = api.get_user(user_id=friend_request)
        display_user_profile(currentUser)
        numRequest += 1
    print("The number of pending friend requests" + str(numRequest))
    return


def display_user_profile(user):  # Given a user object displays prints profile information
    print("User : ", user.name, end=" ")
    print('Friends: ', + user.friends_count)


def get_friends_list(api):  # Prints the users friend list
    for friend in api.get_friends():
        print(friend.screen_name)


def get_favorite_tweets(api):  # Prints the favorite tweets and username
    all_tweets = api.get_favorites()
    for tweet in all_tweets:
        print(tweet.text + " by " + tweet.user.name)


def search_tweets(api, query="Happy", num=50):  #

    newFile = open('search_tweets.txt', 'w', encoding="utf-8")
    fileWriter = csv.writer(newFile)
    fileWriter.writerow(["Username", "followers", " friends", "Created", "Text", "Retweet-count", "Hashtag"])

    for tweet in api.search_tweets(q=query, count=100):  # iterating through the tweets from query
        created = tweet.created_at  # tweet created
        text = tweet.text  # tweet text
        retweetcount = tweet.retweet_count  # re-tweet count

        try:
            hashtag = tweet.entities[u'hashtags'][0][u'text']  # hashtags used
        except:
            hashtag = "None"
        username = tweet.author.name
        followers = tweet.author.followers_count
        friends = tweet.author.friends_count

        fileWriter.writerow([username, followers, friends, created, str(text).encode("utf-8"), retweetcount, hashtag, ])
    newFile.close()


def get_query():  # provides a brief overview on using twitter queries and returns string
    print(" In case you are searching for a specific hashtag use #word")
    print("Inorder to use mulitple filters use AND and OR keywords")
    q = input("Enter query for program")
    return q


def sentiment_analysis(api):
    file = open('results2.csv', 'w', newline='', encoding="utf-8")
    fileWriter = csv.writer(file)
    fileWriter.writerow(["username", "followers", "friends", "tweet", "retweet", "hashtag", "polarity", "subjectivity"])
    i = 0

    query = "health"
    target_num = 50
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", result_type="popular", count=100).items():
        # text = unidecode.unidecode(text)
        try:
            hashtag = tweet.entities[u'hashtags'][0][u'text']  # hashtags used
        except:
            hashtag = "None"  # when hashtag does not exist.
        username = tweet.author.name
        followers = tweet.author.followers_count
        friends = tweet.author.friends_count

        text = tweet.text
        text_blob = TextBlob(text)  # can choose to use sentiment
        polarity = text_blob.polarity  # polarity from -1 to 1
        subjectivity = text_blob.subjectivity  # subjectivity from 0 to 1
        count = tweet.retweet_count
        # from 0 to 0.5 can be objective / else subjective

        fileWriter.writerow([username, followers, friends, text, count, hashtag, polarity, subjectivity])
        # i = i + 1
        if i == target_num:
            break
    file.close()


def review_file():
    data = pd.read_csv('results.csv')
    print(data.corr())


api = load_auth_file()
# get_favorite_tweets(api)
# search_tweets(api)
sentiment_analysis(api)
review_file()
