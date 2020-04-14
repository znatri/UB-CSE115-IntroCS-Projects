// Each song has song_id, title, artist, and ratings as keys
function generate_song_html(song) {
  let retVal = "<a href=\"https://www.youtube.com/watch?v=" + song.song_id + "\" target=\"_blank\">"
  retVal = retVal + song.title + " - " + song.artist + "</a><br>";
  retVal = retVal + song.ratings + "<br>";
  retVal = retVal + "Rate: ";
  retVal = retVal + generate_rating_buttons(song.song_id);
  retVal = retVal + "<hr>";
  return retVal
}

function generate_rating_buttons(song_id) {
  let retVal = "";
  let array = [1, 2, 3, 4, 5];
  for(let i of array) {
    retVal = retVal + generate_button_html(song_id, i);
  }
  return retVal;
}

function generate_button_html(song_id, num) {
  let retVal = "<button onClick=\"rate(\'" + song_id + "\', " + num + ")\">";
  retVal = retVal +num+"</button>";
  return retVal;
}

function get_value_and_clear(input_obj) {
  let retVal = input_obj.value;
  input_obj.value = "";
  return retVal;
}