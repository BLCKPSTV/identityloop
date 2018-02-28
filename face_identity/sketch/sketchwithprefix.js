/**
 * JSON Faces ID (v2.1)
 * GoToLoop & Layzfat (2018-Jan-08)
 *
 * Forum.Processing.org/two/discussion/25872/
 * request-for-json-object-object#Item_8
 *
 * ThimbleProjects.org/gotoloop/388545
 */

"use strict";

const FACES = 2, INTER = 1.5 * 1000, FPS = 1000 / INTER,
      FILL = 'white', STROKE = 0, BOLD = 0,
      BG = '#000000', FONT_SIZE = 20, BW = .98, BH = .96,

      JSON_FOLDER = 'json/', JSON_FILE = 'id_JP_.json',
      JSON_PATH = JSON_FOLDER + JSON_FILE,
      IMG_FOLDER = 'images/', IMG_EXT = '.png', IMG_PROP = 'face',

      faces = Array(FACES);

let bg, persons, idx = 0;
var monoFont;
var notoFont;
var zp = 'zip code';
var sn = 'street name';
var lp = 'license plate';
var pn = 'phone number';
var cc = 'credit card';
var ccsc = 'credit card security code';
var ccryp = 'cryptocurrency code';


function preload() {
  loadJSON(JSON_PATH, json => ({persons} = json));

  for (let i = 0; i < FACES; ++i)
    faces[i] = loadImage(IMG_FOLDER + i + IMG_EXT);

  monoFont = loadFont('assets/UbuntuMono-R.ttf');
  notoFont = loadFont('assets/NotoSansCJKtc-Thin.otf');
}

function setup() {
  createCanvas(windowWidth*BW, windowHeight*BH)//.mousePressed(nextIdx);
  frameRate(FPS)//.noLoop();

  colorMode(RGB).imageMode(CENTER);
  fill(FILL).stroke(STROKE).strokeWeight(BOLD);
  textFont(notoFont);
  textSize(FONT_SIZE).textAlign(LEFT, BASELINE);

  bg = color(BG);
  //persons.forEach((person, idx) => person[IMG_PROP] = faces[idx]);
}

function draw() {
  const face = faces[idx], person = persons[idx];
  idx = (idx + 1) % FACES;

  background(bg);
  image(face, width>>1, height>>2, 800, 960);
  text( "name:" + " " + person.name + "\n" +
        "country:" + " " + person.country + "\n" +
        "city:" + " " + person.city + "\n" +
        "zip code:" + " " + person[zp] + "\n" +
        "street name:" + " " + person[sn] + "\n" +
        "license plate:" + " " + person[lp] + "\n" +
        "phone number" + " " + person[pn] + "\n" +
        "email:" + " " + person.email + "\n" +
        "favorite username:" + " " + person.username + "\n" +
        "password:" + " " + person.password + "\n" +
        "iban:" + " " + person.iban + "\n" +
        "credit card:" + " " + person[cc] + "\n" +
        "credit card security code:" + " " + person[ccsc] + "\n" +
        "cryptocurrency:" + " " + person[ccryp] + "\n" +
        "profession:" + " " + person.profession + "\n"
        , width>>1-250, height/2+450);
  console.table(person);
}

function windowResized() {
  resizeCanvas(windowWidth*BW, windowHeight*BH);
  //redraw();
}

//function nextIdx() {
//  idx = (idx + 1) % FACES;
//  redraw();
//}
