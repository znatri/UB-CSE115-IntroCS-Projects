"use strict";

// Function which makes the AJAX GET request to get
// song data from the server
function getSongs(){
    ajaxGetRequest("songs", displaySongs);
}

// Function called when the server responds to our GET
// request. It updates the webpage with out latest music
// info.
function displaySongs(response){
    let songs = JSON.parse(response);
    let div_html = ""
    for (let song_id in songs) {
      let song = songs[song_id];
      div_html = div_html + generate_song_html(song);
    }
    let songDiv = document.getElementById("songs");
    songDiv.innerHTML = div_html;
}

// Function called when we want to add a song to our list
function newSong() {
  let id_elem = document.getElementById("song_id_input");
  let song_id = get_value_and_clear(id_elem);
    
  let title_elem = document.getElementById("song_title_input");
  let title = get_value_and_clear(title_elem);
    
  let artist_elem = document.getElementById("song_artist_input")
  let artist = get_value_and_clear(artist_elem);
    
  let song = {"song_id": song_id, "title": title, "artist": artist};
  let songJSON = JSON.stringify(song);
  ajaxPostRequest("add_song", songJSON, displaySongs)
}

function rate(song_id, rating){
  let songRating = {"song_id": song_id, "rating": rating};
  let ratingJSON = JSON.stringify(songRating);
  ajaxPostRequest("rate_song", ratingJSON, displaySongs)
}
