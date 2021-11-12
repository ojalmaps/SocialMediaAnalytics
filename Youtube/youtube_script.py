import csv
import googleapiclient.discovery

# Storing information about the credentials
developer_key = "AIzaSyDDD_itQ56sG3i03JD_-XPPi_Cmw-1_2so"
api_service_name = "Youtube"
api_version = "v3"


def youtube_search(query):  # Given a query

    file = open('result.csv', 'w') # creating a new csv file
    fileW = csv.writer(file)
    fileW.writerow(["Title"])

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
    search_response = youtube.search().list(q=query,part ="id", maxResults=15).execute() # calls search query
    stats = youtube.videos().list( part = "id,contentDetails",myRating ="like").execute()    # calls video query

    print(stats)
    all_response = search_response.get("items", [])  # save the items into a list

    for response in all_response:
        if response["id"]["kind"] == "youtube#video":  # only selecting videos
            print(response)


youtube_search("speech")
