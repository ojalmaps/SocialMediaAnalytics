import csv
import tweepy

global api


def load_auth_file():  # Given authentication file returns a Twitter API object
    with open('auth.k') as auth:
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


def search_tweets(api, query="Happy", num=100):  # Given a keyword will try to find matching tweets
    newFile = open('keyword_results.txt', 'w', encoding="utf-8")
    fileWriter = csv.writer(newFile)
    fileWriter.writerow(["Username", "followers", " friends", "Created", "Text", "Retweet-count", "Hashtag"])

    for tweet in api.search_tweets(q=query, count=100):
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


def mentions_timeline(api):  # Returns the 20 most recent tweets in timeline and sorts them based on the most retweeted
    mentions = api.user_timeline(count=100)
    array = {}  # Stores
    key_array = []  # all the keys of the array
    for tweet in mentions:
        if tweet.retweet_count not in array.keys():
            array[tweet.retweet_count] = [tweet.text]
            key_array.append(int(tweet.retweet_count))
        else:
            array[tweet.retweet_count] += [tweet.text]

    key_array.sort()
    key_array.reverse()  # descending order

    newFile = open('mention_results.txt', 'w', encoding="utf-8")
    fileWriter = csv.writer(newFile)
    fileWriter.writerow(["Retweet Count", "Tweet"])

    for i in range(len(key_array) - 1):
        index = key_array[i]
        for tweet in array[index]:
            fileWriter.writerow([index, tweet])
    newFile.close()


def favorite_count_timeline(api):  # Returns the 100 most recent tweets in timeline and sorts them based on the most retweeted
    mentions = api.user_timeline(count=100)
    array = {}  # Stores
    key_array = []  # all the keys of the array
    for tweet in mentions:
        if tweet.favorite_count not in array.keys():
            array[tweet.favorite_count] = [tweet.text]
            key_array.append(int(tweet.favorite_count))
        else:
            array[tweet.favorite_count] += [tweet.text]
    key_array.sort()  # descending order
    key_array.reverse()

    newFile = open('favorite_count.txt', 'w', encoding="utf-8")
    fileWriter = csv.writer(newFile)
    fileWriter.writerow(["Favorite Count", "Tweet"])

    for i in range(len(key_array) - 1):
        index = key_array[i]
        for tweet in array[index]:
            fileWriter.writerow([index, tweet])
    newFile.close()


def user_timeline(api):  # Returns the 20 most recent tweets in timeline
    all_tweets = api.user_timeline()
    array = {}
    for tweet in all_tweets:
        print(tweet.text)
    # Know sort the dictionar based on the retweet count
    print(array)

def get_followers (api):
    follower = api.get_follower_ids(user_id = "@Unicornz4ehva")
    print(follower)
    all_followers = api.get_followers(count = 200, user_id = "@Unicornz4ehva")
    for f in all_followers:
        print(f.screen_name, f.id)

def automate_messege(api):
    pass
    # Every time a user follows us they should get a messege. Test on user - Erin Foley.
    # Write a short text description
    # Use the Direct Message


def all_direct_messages(api):  # Returns all the messages within 30 days.
    all_messages = api.get_direct_messages()
    m = api.get_direct_message()
    print(all_messages)
    print(m)
    for mess in all_messages:
        print(mess)


def send_message(api):
    response = api.send_direct_message(recipient_id="@Unicornz4ehva", text="Here is a sample tweet ! ")
    print(response)


api = load_auth_file()
# get_followers(api)
# get_friends_list(api)
# send_message(api)
# all_direct_messages(api)
# mentions_timeline(api)
# favorite_count_timeline(api)
mentions_timeline(api)
favorite_count_timeline(api)

# Other code includes get_query and then search_tweets
