import tweepy

global api

def load_auth_file():
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


def number_pending_requests():
    numRequest = 0
    for friend_request in api.outgoing_friendships():
        currentUser = api.get_user(user_id=friend_request)
        display_user_profile(currentUser)
        numRequest += 1
    return numRequest


def display_user_profile(user):
    print(user.name)
    print(user.friends_count)


def get_friends_list(api):
    for friend in api.get_friends():
        print(friend.screen_name)


api = load_auth_file()
get_friends_list(api)
number_pending_requests()