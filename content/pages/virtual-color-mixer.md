Title: Virtual Color Mixer
status: hidden

This example demonstrates how to send multiple values from the Arduino board to the computer. The readings from three potentiometers are used to set the red, green, and blue components of the&nbsp;background color of a Processing sketch.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino or Genuino Board</li>
<li>3 Analog Sensors (potentiometer, photocell, FSR, etc.)</li>
<li>3 10K ohm resistors</li>
<li>hook-up wires</li>
<li>breadboard</li>
</ul>
<div class="BOM" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;">Software Required</span><br />
<ul>
<li><a href="http://www.processing.org/">Processing</a></li>
</ul>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Connect analog sensors to analog input pins 0, 1, and 2.<br />
<br />
This circuit uses three <a href="http://www.tigoe.com/pcomp/code/controllers/input-output/analog-input/">voltage divider</a> sub-circuits to generate analog voltages from the force-sensing resistors. a voltage divider has two resistors in series, dividing the voltage proportionally to their values.<br />
<br />
Click on the image to enlarge</div>
<div class="BOM" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br /></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/virtualColorMixer_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/virtualColorMixer_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
Schematic<br />
<br />
Click on the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/VCM_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/VCM_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<span style="font-size: large;">Code</span><br />
<br />
The sensor values are sent from the Arduino to the computer as <a href="http://www.tigoe.net/pcomp/code/communication/interpreting-serial-data-bytes">ASCII-encoded decimal numbers</a>. This means that each number is sent using the ASCII characters "0" through "9". For the value "234" for example, three bytes are sent: ASCII "2" (binary value 50), ASCII "3" (binary value 51), and ASCII "4" (binary value 52).</div>
<div>
<br /></div>
```
/*
  This example reads three analog sensors (potentiometers are easiest)
 and sends their values serially. The Processing and Max/MSP programs at the bottom
 take those three values and use them to change the background color of the screen.

 The circuit:
 * potentiometers attached to analog inputs 0, 1, and 2

 http://www.arduino.cc/en/Tutorial/VirtualColorMixer

 created 2 Dec 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

  This example code is in the public domain.
 */

const int redPin = A0;      // sensor to control red color
const int greenPin = A1;    // sensor to control green color
const int bluePin = A2;     // sensor to control blue color

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	Serial.print(analogRead(redPin));
	Serial.print(",");
	Serial.print(analogRead(greenPin));
	Serial.print(",");
	Serial.println(analogRead(bluePin));
}

/* Processing code for this example

//  This example code is in the public domain.

import processing.serial.*;

float redValue = 0;        // red value
float greenValue = 0;      // green value
float blueValue = 0;       // blue value

Serial myPort;

void setup() {
  size(200, 200);

  // List all the available serial ports
  // if using Processing 2.1 or later, use Serial.printArray()
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  Arduino, so I open Serial.list()[0].
  // Open whatever port is the one you're using.
  myPort = new Serial(this, Serial.list()[0], 9600);
  // don't generate a serialEvent() unless you get a newline character:
  myPort.bufferUntil('\n');
}

void draw() {
  // set the background color with the color values:
  background(redValue, greenValue, blueValue);
}

void serialEvent(Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');

  if (inString != null) {
    // trim off any whitespace:
    inString = trim(inString);
    // split the string on the commas and convert the
    // resulting substrings into an integer array:
    float[] colors = float(split(inString, ","));
    // if the array has at least three elements, you know
    // you got the whole thing.  Put the numbers in the
    // color variables:
    if (colors.length >=3) {
      // map them to the range 0-255:
      redValue = map(colors[0], 0, 1023, 0, 255);
      greenValue = map(colors[1], 0, 1023, 0, 255);
      blueValue = map(colors[2], 0, 1023, 0, 255);
    }
  }
}
 */
 ```
<br />
<span style="font-size: large;"><br />Processing Code</span><br />
<br />
Copy the Processing sketch from the code sample above. As you change the value of the analog sensors, the background color will change:<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<img  src="https://www.arduino.cc/en/uploads/Tutorial/virtualColorMixer-output.png" style="border: 0px; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /></div>
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<br /></div>
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<h2 style="color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 22px; margin: 0px; position: relative;">
<div style="text-align: center;">
<span style="font-size: medium;">Want to save some time learning&nbsp;</span><span style="font-size: medium;">Arduino?</span></div>
<span style="font-size: medium;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our<br />
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
</div>
