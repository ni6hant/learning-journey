// Daniel Shiffman
// http://codingtra.in
// http://patreon.com/codingtrain
// Code for: https://youtu.be/KkyIDI6rQJI

// Purple Rain
// (138, 43, 226)
// (230, 230, 250) // background

var drops = [];
var canvas;
var noOfDrops=0;
var slider;

function setup() {
  canvas = createCanvas(window.innerWidth, window.innerHeight);
  slider = createSlider(0,1000,2500);
  noOfDrops = slider.value();
  for (var i = 0; i < noOfDrops; i++) {
    drops[i] = new Drop();
  }
}

function draw() {
  background(230, 230, 250);
  for (var i = 0; i < drops.length; i++) {
    drops[i].fall();
    drops[i].show();
  }
}
