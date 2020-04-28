# Part B (20 points) - custom sorting in Python

def beatOrder(song):
  bpm = song.get("bpm")
  return bpm

def sortByBeats(listofsongs):
  listofsongs.sort(key=beatOrder)

# playlist = [{ "name" : "bad guy", "artist" : "Billie Eilish", "bpm" : 135, "length" : 194},
#             { "name" : "Beautiful People", "artist" : "Ed Sheeran", "bpm" : 93, "length" : 198},
#             { "name" : "Truth Hertz", "artist" : "Lizzo", "bpm" : 158, "length" : 173},
#             { "name" : "Old Town Road", "artist" : "Lil Nas X", "bpm" : 136, "length" : 157}]
# sortByBeats(playlist)
# print(playlist)


# Part C (20 points) - Using a Database

import sqlite3

def longPlay(cur, minLen):
  seq = cur.execute('SELECT * FROM pandora WHERE length > ?', (minLen,))
  accumulator = []
  for entry in seq:
    accumulator.append(entry)
  accumulator.sort(key=sortByArtist)
  return accumulator

def sortByArtist(val):
  artist = val[1]
  return artist
