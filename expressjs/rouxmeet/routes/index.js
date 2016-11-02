var express = require('express');
var router = express.Router();
var appdata = require('../data.json');

/* GET home page. */
router.get('/', function(req, res) {
  var myArtwork = [];
  var myArtists = [];

  myArtists = appdata.rooms;
  appdata.rooms.forEach(function(item) {
    myArtwork = myArtwork.concat(item.artwork);
  });
  res.render('index', {
    title: 'Home',
    artwork: myArtwork,
    artists: myArtists,
    page: 'home'
  });
});

/* GET rooms page. */
router.get('/rooms', function(req, res) {
  var myArtwork = [];
  var myArtists = [];
  myArtists = appdata.rooms;

  appdata.rooms.forEach(function(item) {
    myArtwork = myArtwork.concat(item.artwork);
  });
  res.render('rooms', {
    title: 'Rooms',
    artwork: myArtwork,
    artists: myArtists,
    page: 'artistList'
  });
});


/* GET speakers detail page */
router.get('/rooms/:roomsid', function(req, res) {
  var myArtwork = [];
  var myArtists = [];

  appdata.rooms.forEach(function(item) {
    if (item.shortname == req.params.roomsid) {
      myArtists.push(item);
      myArtwork = myArtwork.concat(item.artwork);
    }
  });
  res.render('rooms', {
    title: 'Rooms Detail',
    artwork: myArtwork,
    artists: myArtists,
    page: 'artistDetail'
  });
});



module.exports = router;