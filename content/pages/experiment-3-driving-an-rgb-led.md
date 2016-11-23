Title: Experiment 3: Driving an RGB LED
status: hidden

<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="font-size: xx-small;"><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></span></h3>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Introduction</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You know what’s even more fun than a blinking LED? Changing colors with one LED. RGB, or red-green-blue, LEDs have three different color-emitting diodes that can be combined to create all sorts of colors. In this circuit, you’ll learn how to use an RGB LED to create unique color combinations. Depending on how bright each diode is, nearly any color is possible!</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Parts Needed</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You will need the following parts:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Breadboard</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RedBoard or Arduino Uno</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;LED - RGB Common Cathode</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">3x</span>&nbsp;330Ω Resistors</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">5x</span>&nbsp;Jumper Wires</li>
</ul>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Hardware Hookup</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Ready to start hooking everything up? Check out the Fritzing diagram and hookup table below, to see how everything is connected.</div>
<table class="table table-bordered" style="background-color: white; border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 650px;"><tbody style="box-sizing: border-box;">
<tr class="warning" style="box-sizing: border-box;"><td align="center" class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Polarized Components<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td align="left" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Pay special attention to the component’s markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction. Polarized components are highlighted with a yellow warning triangle, in the table below.</td></tr>
</tbody></table>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Fritzing Diagram for RedBoard</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_02_01.png" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_02_01.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<em style="box-sizing: border-box;">Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.</em><br />
<em style="box-sizing: border-box;"><br /></em>
<br />
<h4 style="box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px; text-align: start;">
Hookup Table</h4>
<table class="table table-bordered" style="border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 650px;"><tbody style="box-sizing: border-box;">
<tr style="box-sizing: border-box;"><th class="text-center" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; text-align: center; vertical-align: top;">Component</th><th class="text-center" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; text-align: center; vertical-align: top;">RedBoard or Arduino Uno R3</th><th class="text-center" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; text-align: center; vertical-align: top;">Breadboard</th><th class="text-center" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; text-align: center; vertical-align: top;">Breadboard</th><th class="text-center" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; text-align: center; vertical-align: top;">Breadboard</th><th class="text-center" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; text-align: center; vertical-align: top;">Breadboard</th></tr>
<tr align="center" class="warning" style="box-sizing: border-box;"><td class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">RGB LED&nbsp;<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">j2 (RED)</td><td style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">j3 (GND)</td><td style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">j4 (GREEN)</td><td style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">j5 (BLUE)</td></tr>
<tr align="center" style="box-sizing: border-box;"><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">330 Resistor</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">d2</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">f2</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">330 Resistor</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">d4</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">f4</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">330 Resistor</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">d5</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">f5</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td bgcolor="#DDDDDD" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Jumper Wire</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">GND</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">( - )</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td class="danger" style="background-color: #f2dede; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Jumper Wire</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">PIN 9</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">a2</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td bgcolor="#DDDDDD" style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Jumper Wire</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">f3</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">( - )</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td class="success" style="background-color: #dff0d8; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Jumper Wire</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">PIN 10</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">a4</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
<tr align="center" style="box-sizing: border-box;"><td class="info" style="background-color: #d9edf7; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Jumper Wire</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">PIN 11</td><td class="active" style="background-color: whitesmoke; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">a5</td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td><td style="border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;"></td></tr>
</tbody></table>
<div style="text-align: left;">
<em style="box-sizing: border-box;"></em></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: left;">
Run the Sketch</h3>
<div>
<br /></div>
</div>
</div>
</div>
```
/*
SparkFun Inventor's Kit
Example sketch 03

RGB LED

  Make an RGB LED display a rainbow of colors!
  
Hardware connections:

  An RGB LED is actually three LEDs (red, green, and blue) in
  one package. When you run them at different brightnesses,
  the red, green and blue mix to form new colors.
  
  Starting at the flattened edge of the flange on the LED,
  the pins are ordered RED, COMMON, GREEN, BLUE.
  
  Connect RED to a 330 Ohm resistor. Connect the other end
  of the resistor to Arduino digital pin 9.

  Connect COMMON pin to GND.

  Connect GREEN to a 330 Ohm resistor. Connect the other end
  of the resistor to Arduino digital pin 10.

  Connect BLUE to a 330 Ohm resistor. Connect the other end
  of the resistor to Arduino digital pin 11.

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/


// First we'll define the pins by name to make the sketch
// easier to follow.

// Here's a new trick: putting the word "const" in front of a
// variable indicates that this is a "constant" value that will
// never change. (You don't have to do this, but if you do, the
// Arduino will give you a friendly warning if you accidentally
// try to change the value, so it's considered good form.)

const int RED_PIN = 9;
const int GREEN_PIN = 10;
const int BLUE_PIN = 11;

// This variable controls how fast we loop through the colors.
// (Try changing this to make the fading faster or slower.)

int DISPLAY_TIME = 100;  // In milliseconds


void setup()
{
  // Here we'll configure the Arduino pins we're using to
  // drive the LED to be outputs:

  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
}


void loop()
{
  // In this sketch, we'll start writing our own functions.
  // This makes the sketch easier to follow by dividing up
  // the sketch into sections, and not having everything in
  // setup() or loop().

  // We'll show you two ways to run the RGB LED.

  // The first way is to turn the individual LEDs (red, blue,
  // and green) on and off in various combinations. This gives you
  // a total of eight colors (if you count "black" as a color).
	
  // We've written a function called mainColors() that steps
  // through all eight of these colors. We're only "calling" the
  // function here (telling it to run). The actual function code
  // is further down in the sketch.

  mainColors();
  
  // The above function turns the individual LEDs full-on and
  // full-off. If you want to generate more than eight colors,
  // you can do so by varying the brightness of the individual
  // LEDs between full-on and full-off.
  
  // The analogWrite() function lets us do this. This function
  // lets you dim a LED from full-off to full-on over 255 steps.
  
  // We've written a function called showSpectrum() that smoothly
  // steps through all the colors. Again we're just calling it
  // here; the actual code is further down in this sketch.

  showSpectrum();
}


// Here's the mainColors() function we've written.

// This function displays the eight "main" colors that the RGB LED
// can produce. If you'd like to use one of these colors in your 
// own sketch, you cancopy and paste that section into your code.

void mainColors()
{
  // Off (all LEDs off):

  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);

  delay(1000);

  // Red (turn just the red LED on):

  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);

  delay(1000);

  // Green (turn just the green LED on):

  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, LOW);

  delay(1000);

  // Blue (turn just the blue LED on):

  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, HIGH);

  delay(1000);

  // Yellow (turn red and green on):

  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, LOW);

  delay(1000);

  // Cyan (turn green and blue on):

  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, HIGH);

  delay(1000);

  // Purple (turn red and blue on):

  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, HIGH);

  delay(1000);

  // White (turn all the LEDs on):

  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, HIGH);

  delay(1000);
}


// Below are two more functions we've written,
// showSpectrum() and showRGB().

// showRGB() displays a single color on the RGB LED.
// You call showRGB() with the number of a color you want
// to display.

// showSpectrum() steps through all the colors of the RGB LED,
// displaying a rainbow. showSpectrum() actually calls showRGB()
// over and over to do this.

// We'll often break tasks down into individual functions like
// this, which makes your sketches easier to follow, and once
// you have a handy function, you can reuse it in your other
// programs.


// showSpectrum()

// This function steps through all the colors of the RGB LED.
// It does this by stepping a variable from 0 to 768 (the total
// number of colors), and repeatedly calling showRGB() to display
// the individual colors.

// In this function, we're using a "for() loop" to step a variable
// from one value to another, and perform a set of instructions
// for each step. For() loops are a very handy way to get numbers
// to count up or down.

// Every for() loop has three statements separated by semicolons:

//   1. Something to do before starting

//   2. A test to perform; as long as it's true,
//      it will keep looping

//   3. Something to do after each loop (usually
//      increase a variable)

// For the for() loop below, these are the three statements:

//   1. x = 0;     Before starting, make x = 0.

//   2. x < 768;   While x is less than 768, run the
//                 following code.

//   3. x++        Putting "++" after a variable means
//                 "add one to it". (You can also use "x = x + 1")

// Every time you go through the loop, the statements following
// the loop (those within the brackets) will run.

// And when the test in statement 2 is finally false, the sketch
// will continue.


void showSpectrum()
{
  int x;  // define an integer variable called "x"
  
  // Now we'll use a for() loop to make x count from 0 to 767
  // (Note that there's no semicolon after this line!
  // That's because the for() loop will repeat the next
  // "statement", which in this case is everything within
  // the following brackets {} )

  for (x = 0; x < 768; x++)

  // Each time we loop (with a new value of x), do the following:

  {
    showRGB(x);  // Call RGBspectrum() with our new x
    delay(10);   // Delay for 10 ms (1/100th of a second)
  }
}


// showRGB()

// This function translates a number between 0 and 767 into a
// specific color on the RGB LED. If you have this number count
// through the whole range (0 to 767), the LED will smoothly
// change color through the entire spectrum.

// The "base" numbers are:
// 0   = pure red
// 255 = pure green
// 511 = pure blue
// 767 = pure red (again)

// Numbers between the above colors will create blends. For
// example, 640 is midway between 512 (pure blue) and 767
// (pure red). It will give you a 50/50 mix of blue and red,
// resulting in purple.

// If you count up from 0 to 767 and pass that number to this
// function, the LED will smoothly fade between all the colors.
// (Because it starts and ends on pure red, you can start over
// at 0 without any break in the spectrum).


void showRGB(int color)
{
    int redIntensity;
    int greenIntensity;
    int blueIntensity;

  // Here we'll use an "if / else" statement to determine which
  // of the three (R,G,B) zones x falls into. Each of these zones
  // spans 255 because analogWrite() wants a number from 0 to 255.

  // In each of these zones, we'll calculate the brightness
  // for each of the red, green, and blue LEDs within the RGB LED.

    if (color <= 255)          // zone 1
    {
        redIntensity = 255 - color;    // red goes from on to off
        greenIntensity = color;        // green goes from off to on
        blueIntensity = 0;             // blue is always off
    }
    else if (color <= 511)     // zone 2
    {
        redIntensity = 0;                     // red is always off
        greenIntensity = 255 - (color - 256); // green on to off
        blueIntensity = (color - 256);        // blue off to on
    }
    else // color >= 512       // zone 3
    {
        redIntensity = (color - 512);         // red off to on
        greenIntensity = 0;                   // green is always off
        blueIntensity = 255 - (color - 512);  // blue on to off
    }

  // Now that the brightness values have been set, command the LED
  // to those values

    analogWrite(RED_PIN, redIntensity);
    analogWrite(BLUE_PIN, blueIntensity);
    analogWrite(GREEN_PIN, greenIntensity);
}
```
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Code To Note</h3>
<pre data-language="language:cpp
,cpp
" style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(204, 204, 204); box-sizing: border-box; color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 13px; line-height: 19px; margin-bottom: 20px; max-height: 350px; overflow: auto; padding: 6px 10px; word-break: break-all; word-wrap: break-word;"><div class="copy-code" data-code-id="code-1" style="box-sizing: border-box; float: right;">
<button class="btn btn-default btn-sm" style="-webkit-user-select: none; background-color: white; background-image: none; border-radius: 3px; border: 1px solid rgb(204, 204, 204); color: #e0311d; cursor: pointer; font-family: SparkGauge, 'Arial Narrow', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; font-stretch: inherit; font-style: inherit; font-variant: inherit; font-weight: 700; letter-spacing: 0.1em; line-height: 1.5; margin: 0px; overflow: visible; padding: 5px 10px; text-transform: uppercase; vertical-align: middle; white-space: nowrap;">COPY CODE</button></div>
<code class="rainbow" style="background: transparent; border-radius: 0px; border: 0px; box-sizing: border-box; color: inherit; font-family: Consolas, 'Liberation Mono', Courier, monospace; margin: 0px; padding: 0px; white-space: pre-wrap;"><span class="keyword" style="box-sizing: border-box; font-weight: bold;">for</span> (x <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">=</span> <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>; x <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">&lt;</span> <span class="constant numeric" style="box-sizing: border-box; color: #009999;">768</span>; x<span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">+</span><span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">+</span>)
{}
</code></pre>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
A&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">for()</code>&nbsp;loop is used to repeat an action a set number of times across a range, and repeatedly runs code within the brackets {}. Here the variable “x” starts a 0, ends at 767, and increases by one each time (“x++”).</div>
<pre data-language="language:cpp
,cpp
" style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(204, 204, 204); box-sizing: border-box; color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 13px; line-height: 19px; margin-bottom: 20px; max-height: 350px; overflow: auto; padding: 6px 10px; word-break: break-all; word-wrap: break-word;"><div class="copy-code" data-code-id="code-2" style="box-sizing: border-box; float: right;">
<button class="btn btn-default btn-sm" style="-webkit-user-select: none; background-color: white; background-image: none; border-radius: 3px; border: 1px solid rgb(204, 204, 204); color: #e0311d; cursor: pointer; font-family: SparkGauge, 'Arial Narrow', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; font-stretch: inherit; font-style: inherit; font-variant: inherit; font-weight: 700; letter-spacing: 0.1em; line-height: 1.5; margin: 0px; overflow: visible; padding: 5px 10px; text-transform: uppercase; vertical-align: middle; white-space: nowrap;">COPY CODE</button></div>
<code class="rainbow" style="background: transparent; border-radius: 0px; border: 0px; box-sizing: border-box; color: inherit; font-family: Consolas, 'Liberation Mono', Courier, monospace; margin: 0px; padding: 0px; white-space: pre-wrap;"><span class="keyword" style="box-sizing: border-box; font-weight: bold;">if</span> (x <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">&lt;</span><span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">=</span> <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>)
{}
<span class="keyword" style="box-sizing: border-box; font-weight: bold;">else</span>
{}
</code></pre>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
“If / else” statements are used to make choices in your programs. The statement within the parenthesis () is evaluated; if it’s true, the code within the first brackets {} will run. If it’s not true, the code within the second brackets {} will run.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
What You Should See</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You should see your LED turn on, but this time in new, crazy colors! If it isn’t, make sure you have assembled the circuit correctly and verified and uploaded the code to your board or see the troubleshooting section.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<br /></div>
<div class="row" style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_03_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_03_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Many electronics such as video game consoles use RGB LEDs to have the versatility to show different colors in the same area. Often times the different colors represent different states of working condition.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Troubleshooting</h3>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
LED Remains Dark or Shows Incorrect Color</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
With the four pins of the LED so close together, it’s sometimes easy to misplace one. Double check each pin is where it should be.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Seeing Red</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The red diode within the RGB LED may be a bit brighter than the other two. To make your colors more balanced, use a higher ohm resistor. Or adjust in code.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">analogWrite(RED_PIN, redIntensity);</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
to</div>
<div style="box-sizing: border-box; margin: 0px 0px 10px;">
<div style="background-color: white; color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20px; text-transform: none; white-space: normal; word-spacing: 0px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20px; text-transform: none; white-space: normal; word-spacing: 0px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">analogWrite(RED_PIN, redIntensity/3);</code></div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20px; text-transform: none; white-space: normal; word-spacing: 0px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;"><br /></code></div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20px; text-transform: none; white-space: normal; word-spacing: 0px;">
<span style="color: #555555; font-family: &quot;montserrat&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; font-size: 20px; line-height: 1.1;">Questions</span></div>
<ol>
<li>What does the mainColors function do?</li>
<li>What does the showRGB function do?</li>
<li>What does the show Spectrum function do?</li>
<li>How is it we can have 768 possible colors with this sketch?</li>
<li>Describe how the analogWrite() function works.</li>
</ol>
</div>
<div style="background-color: white; color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20px; text-transform: none; white-space: normal; word-spacing: 0px;">
<code style="background-attachment: initial; background-clip: initial; background-color: #f8f8f8; background-image: initial; background-origin: initial; background-position: initial; background-repeat: initial; background-size: initial; border-image-outset: initial; border-image-repeat: initial; border-image-slice: initial; border-image-source: initial; border-image-width: initial; border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-size: 12px; line-height: 20px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;"><span style="color: #333333; font-family: &quot;consolas&quot; , &quot;liberation mono&quot; , &quot;courier&quot; , monospace;"><br /></span></code></div>
<div style="text-align: center;">
<a href="http://www.davidriewe.com/p/experiment-2-reading-potentiometer.html"><span style="font-family: &quot;helvetica neue&quot; , &quot;arial&quot; , &quot;helvetica&quot; , sans-serif; font-size: x-small;"></span></a><span style="font-family: &quot;helvetica neue&quot; , &quot;arial&quot; , &quot;helvetica&quot; , sans-serif; font-size: x-small;"><a href="/pages/experiment-2-reading-a-potentiometer.html">Experiment 2: Reading a Potentiometer</a> -|- <a href="/pages/experiment-4-driving-multiple-leds.html">Experiment 4: Driving Multiple LEDs</a></span></div>
</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20px; margin: 0px 0px 10px; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px;">
<div style="text-align: center;">
<span style="font-size: xx-small;"><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></span><br />
<br />
<h2 style="color: #666666; font-family: 'trebuchet ms', trebuchet, verdana, sans-serif; font-size: 22px; margin: 0px; position: relative;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our<br /><a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
</div>
</div>
