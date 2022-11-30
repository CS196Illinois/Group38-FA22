#Grace He @ 11/29/2022

import json
import random
import sys
#you need to install the requests library to use this
import requests

#musixmatch api base url
base_url = "https://api.musixmatch.com/ws/1.1/"

#api key
api_key = "&apikey=846b5791051b80bfc37d22ff90b1c41a"

# gets the genre ID number
#   mainly for use by the getURL() method, don't worry about this one much
def getGenreID(genre_name):
    genre_data = requests.get(base_url + "music.genres.get" + api_key).json()
    genre_data = genre_data['message']['body']['music_genre_list']
    for i in range(len(genre_data)):
        if genre_data[i]['music_genre']['music_genre_name'] == genre_name.capitalize():
            return genre_data[i]['music_genre']['music_genre_id']

# asks for a number of songs to generate and checks if the input is valid
def getNumberOfResults():
    resultNumber = input("How many songs would you like? ")
    if (not resultNumber.isdigit() or int(resultNumber) <= 0):
        if (resultNumber != ""):
            print("Please enter a valid number. You may also leave this field blank.")
            getNumberOfResults()
    return resultNumber
        
# returns the API call based off of inputs
def getURL():
    api_call = base_url + "track.search?f_has_lyrics=1"
    print("Any of the following fields may be left blank.")
    prompt = input("Prompt: ")
    artist = input("Artist: ")
    genre = input("Genre: ")
    mood = input("Mood: ")
    resultNumber = getNumberOfResults()
    if prompt != "":
        prompt = prompt.replace(" ", "%20")
        api_call = api_call + "&quorum_factor=0.3&q=" + prompt
    if artist != "":
        artist = artist.replace(" ", "%20")
        api_call = api_call + "&s_artist_rating=desc&s_track_rating&q_artist=" + artist
    if genre != "":
        genre_id = str(getGenreID(genre))
        api_call = api_call + "&f_music_genre_id=" + genre_id
    if mood != "":
        mood = mood.replace(" ", "%20")
        api_call = api_call + "&q_lyrics=" + mood
    if resultNumber != "" and resultNumber.isdigit():
        api_call = api_call + "&page_size=" + resultNumber
    api_call = api_call + api_key
    #print(api_call)
    return api_call

# gets all the song data and prints it out nicely
# writes song recs to a .txt file
# also creates and returns a list of song ids
def getSongs(api_call):
    sys.stdout = open('song_recs.txt','wt')
    print(" Song Recommendations \n")
    print("-------------------------------\n")
    id_list = []
    data = requests.get(api_call).json()
    data = data['message']['body']['track_list']
    for i in range(len(data)):
        track_id = str(data[i]['track']['track_id'])
        lyrics = requests.get(base_url + "track.lyrics.get?track_id=" + track_id + api_key).json()
        lyrics = lyrics['message']['body']['lyrics']['lyrics_body']
        lyrics = lyrics.split("\n...\n\n*******", 1)[0]
        if (lyrics == ""):
            lyrics = "None Found."
        song_data = requests.get(base_url + "track.get?track_id=" + track_id + api_key).json()
        name = song_data['message']['body']['track']['track_name']
        artist = song_data['message']['body']['track']['artist_name']

        print(name)
        print("By: " + artist + "\n")
        print("Lyrics Snippet: \n\n" + lyrics + "\n")
        print("-------------------------------\n")

        id_list.append(track_id)
    sys.stdout.close()
    id_list = list(filter(None, id_list))
    return id_list

# putting all of these methods together, we can get song recs!
api_call = getURL()
songs = getSongs(api_call)
