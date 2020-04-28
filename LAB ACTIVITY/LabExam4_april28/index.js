// Part A (40 points) - custom sorting in JavaScript

function beatOrder(a, b) {
    let a_bpm = a.bpm;
    let b_bpm = b.bpm;

    if (a_bpm < b_bpm) {
        return -1;
    } else if (a_bpm > b_bpm) {
        return 1;
    } else {
        return 0;
    }
}

function sortByBeats(listofsongs) {
    listofsongs.sort(beatOrder);
}

  // let playlist = [{ name:"bad guy", artist : "Billie Eilish", bpm : 135, length : 194},
  //                 { name:"Beautiful People", artist : "Ed Sheeran", bpm : 93, length : 198},
  //                 { name:"Truth Hertz", artist : "Lizzo", bpm : 158, length : 173},
  //                 { name:"Old Town Road", artist : "Lil Nas X", bpm : 136, length : 157}];

  // sortByBeats(playlist);

  // console.log(playlist);