import csv
import tweepy
global api


def load_auth_file():  # Given authentication file returns a Twitter API object
    with open('auth.txt') as auth:
        auth_array = auth.readlines()
    auth.close()
    access_token2 = auth_array[0].replace("\n", "").strip('"')
    access_token_secret2 = auth_array[1].replace("\n", "").strip('"')
    consumer_key2 = auth_array[2].replace("\n", "").strip('"')
    consumer_secret2 = auth_array[3].replace("\n", "").strip('"')
    auth = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
    auth.set_access_token(access_token2, access_token_secret2)
    API = tweepy.API(auth)
    return API


def number_pending_requests():  # Returns the number of pending friend request for a user
    numRequest = 0
    for friend_request in api.outgoing_friendships():
        currentUser = api.get_user(user_id=friend_request)
        display_user_profile(currentUser)
        numRequest += 1
    return numRequest


def display_user_profile(user): # Given a user object displays prints profile information
    print("User : ", user.name, end = " ")
    print('Friends: ', + user.friends_count)


def get_friends_list(api): # Prints the users friend list
    for friend in api.get_friends():
        print(friend.screen_name)


def get_favorite_tweets(api): # Prints the favorite tweets and username
    all_tweets = api.get_favorites()
    for tweet in all_tweets:
        print(tweet.text + " by " + tweet.user.name)


def search_tweets(api, query = "#2021",num = 100 ):  # usinght e
    newFile = open('ans.txt', 'w', encoding="utf-8")
    fileWriter = csv.writer(newFile)
    fileWriter.writerow(["Username", "followers", " friends" ,"Created", "Text", "Retweet-count", "Hashtag"])

    for tweet in api.search_tweets(q=query, count= num):
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


def get_query(): # provides a brief overview on using twitter queries and returns string
    print(" In case you are searching for a specific hashtag use #word")
    print("Inorder to use mulitple filters use AND and OR keywords")
    q = input("Enter query for program")
    return q


api = load_auth_file()
get_favorite_tweets(api)
search_tweets(api)
