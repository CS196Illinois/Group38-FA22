#Grace He @ 11/9/2022

import json
#you need to install the requests library to use this
import requests

#musixmatch api base url
base_url = "https://api.musixmatch.com/ws/1.1/"

#api key
api_key = "&apikey=846b5791051b80bfc37d22ff90b1c41a"

# gets the genre ID number
#   mainly for use by the getURL() method, don't worry about this one much.
def getGenreID(genre_name):
    genre_data = requests.get(base_url + "music.genres.get" + api_key).json()
    genre_data = genre_data['message']['body']['music_genre_list']
    for i in range(len(genre_data)):
        if genre_data[i]['music_genre']['music_genre_name'] == genre_name.capitalize():
            return genre_data[i]['music_genre']['music_genre_id']

# returns the API call based off of inputs
#   you can change the number of songs it gives out
#   by changing the page_size parameter on the api_call variable declaration.
#   the range is 1 to 100.
def getURL():
    api_call = base_url + "track.search?page_size=50&f_has_lyrics=1"
    print("Any of the following fields may be left blank.")
    prompt = input("Prompt: ")
    artist = input("Artist: ")
    genre = input("Genre: ")
    mood = input("Mood: ")
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
    api_call = api_call + api_key
    print(api_call)
    return api_call

# creates a list of lyrics from an api call
#   you should use this one only after getURL()
def getLyrics(api_call):
    lyrics_list = []
    data = requests.get(api_call).json()
    data = data['message']['body']['track_list']
    for i in range(len(data)):
        track_id = str(data[i]['track']['track_id'])
        lyrics_data = requests.get(base_url + "track.lyrics.get?track_id=" + track_id + api_key).json()
        lyrics_data = lyrics_data['message']['body']['lyrics']['lyrics_body']
        lyrics_data = lyrics_data.replace("\n******* This Lyrics is NOT for Commercial use *******\n", "")
        lyrics_list.append(lyrics_data)
    return lyrics_list

# writes a list of lyrics onto a .json file
def writeLyricsFile(lyrics_list):
    with open('matching_lyrics.json', 'w') as f:
        json.dump(lyrics_list, f, sort_keys=True, indent=2)

# putting all of these methods together, we can get lyrics!
api_call = getURL()
lyrics = getLyrics(api_call)
writeLyricsFile(lyrics)
print(json.dumps(lyrics, sort_keys=True, indent=2))
