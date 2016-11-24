Title: Dimmer - Control LED brightness using mouse on PC
status: hidden

This example shows how to send data from a personal computer to an Arduinoboard to control the brightness of an LED. The data is sent in individual bytes, each of which ranges in value from 0 to 255. The sketch reads these bytes and uses them to set the brightness of the LED.<br />
<br />
You can send bytes to the board from any software that can access the computer serial port. Examples for <a href="http://www.processing.org/">Processing</a> are shown below.<br />
<span style="font-size: large;"><br /></span>
<span style="font-size: large;">Hardware Required</span><br />
<div>
<span style="font-size: medium;"></span><br />
<ul>
<li><span style="font-size: medium;">Arduino&nbsp;</span></li>
<li><span style="font-size: medium;">LED</span></li>
<li><span style="font-size: medium;">220 ohm resistor</span></li>
</ul>
<br />
<div>
<br />
<span style="font-size: large;">Software Required</span><br />
<div>
<br />
<ul>
<li><a href="http://www.processing.org/">Processing</a></li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Connect the 220 ohm current limiting resistor to digital pin 9, with an LED in series. The long, positive leg (the anode) of the LED should be connected to the output from the resistor, with the shorter, negative leg (the cathode) connected to ground.</div>
<div>
<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
click the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/dimmer-circuit3.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/dimmer-circuit3.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="300px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
<br />
<span style="font-size: large;">Schematic</span><br />
<br />
<br />
click the image to enlarge</div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/simplefade_pin9_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/simplefade_pin9_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="250px" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<br /></div>
</div>
<span style="font-size: large;">Code</span><br />
<span style="font-size: large;"><br /></span></div>
</div>
</div>
<div>
<span style="font-size: medium;">Note that the processing code is included within the sketch below, commented out. &nbsp;You will need to copy and paste the code into processing.&nbsp;</span></div>
```
/*
  Dimmer

 Demonstrates the sending data from the computer to the Arduino board,
 in this case to control the brightness of an LED.  The data is sent
 in individual bytes, each of which ranges from 0 to 255.  Arduino
 reads these bytes and uses them to set the brightness of the LED.

 The circuit:
 LED attached from digital pin 9 to ground.
 Serial connection to Processing, Max/MSP, or another serial application

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Dimmer

 */

const int ledPin = 9;      // the pin that the LED is attached to

void setup()
{
	// initialize the serial communication:
	Serial.begin(9600);
	// initialize the ledPin as an output:
	pinMode(ledPin, OUTPUT);
}

void loop()
{
	byte brightness;

	// check if data has been sent from the computer:
	if (Serial.available())
	{
		// read the most recent byte (which will be from 0 to 255):
		brightness = Serial.read();
		// set the brightness of the LED:
		analogWrite(ledPin, brightness);
	}
}
```

```

/* Processing code for this example
 // Dimmer - sends bytes over a serial port
 // by David A. Mellis
 //This example code is in the public domain.

 import processing.serial.*;
 Serial port;

 void setup() {
 size(256, 150);

 println("Available serial ports:");
 // if using Processing 2.1 or later, use Serial.printArray()
 println(Serial.list());

 // Uses the first port in this list (number 0).  Change this to
 // select the port corresponding to your Arduino board.  The last
 // parameter (e.g. 9600) is the speed of the communication.  It
 // has to correspond to the value passed to Serial.begin() in your
 // Arduino sketch.
 port = new Serial(this, Serial.list()[0], 9600);

 // If you know the name of the port used by the Arduino board, you
 // can specify it directly like this.
 //port = new Serial(this, "COM1", 9600);
 }

 void draw() {
 // draw a gradient from black to white
 for (int i = 0; i < 256; i++) {
 stroke(i);
 line(i, 0, i, 150);
 }

 // write the current X-position of the mouse to the serial port as
 // a single byte
 port.write(mouseX);
 }
 */
 ```
<br />
<h2 style="background-color: white; color: #666666; font-family: 'trebuchet ms', trebuchet, verdana, sans-serif; font-size: 22px; line-height: 20px; margin: 0px; position: relative; text-align: center;">
<div>
<span style="font-size: medium;">Want to save some time learning&nbsp;</span><span style="font-size: medium;">Arduino?</span></div>
<span style="font-size: medium;">Join the thousands of awesome people to sign up for our<br /><a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></span></h2>
