Title: Physical Pixel: Turn a LED on and off by sending data to your Arduino from Processing or Max/MSP
status: hidden

This example example uses the Arduino or Genuino board to receive data from the computer. The board turns on an LED when it receives the character 'H', and turns off the LED when it receives the character 'L'.<br />
<br />
<br />
The data can be sent from the Arduino Software (IDE) serial monitor, or another program like Processing (see code below), Flash (via a serial-net proxy), PD, or Max/MSP.<br />
<div>
<br />
<span style="font-size: large;"> Hardware Required</span><br />
<br />
<ul>
<li>Arduino</li>
<li>LED (optional)&nbsp;</li>
<li>220 ohm resistor (optional)&nbsp;</li>
</ul>
<div>
<br />
<span style="font-size: large;"> Software Required&nbsp;</span></div>
<div>
<br /></div>
<div>
<ul>
<li><a href="http://www.processing.org/">Processing</a></li>
</ul>
<div>
<br />
<span style="font-size: large;"> Circuit</span><br />
<br />
Many Arduino and Genuino boards have a built-in LED connected to pin 13; if your board has no built-in LED, attach an external LED to pin 13. The long leg, or anode, goes to pin 13 through a 220 resistor. The short leg, or cathode, goes to ground.<br />
<br />
<br />
click the image to enlarge<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'typoninesans regular 18', 'lucida grande', lucida, verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/ExampleCircuit_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  height="300px" src="https://www.arduino.cc/en/uploads/Tutorial/ExampleCircuit_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;"> Schematic</span><br />
<br />
click the image to enlarge</div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'typoninesans regular 18', 'lucida grande', lucida, verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/ExampleCircuit_sch.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  height="300px" src="https://www.arduino.cc/en/uploads/Tutorial/ExampleCircuit_sch.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /></a><br />
<br /></div>
</div>
<span style="font-size: large;">Code</span><br />
<div>
<br /></div>
```
/*
  Physical Pixel

 An example of using the Arduino board to receive data from the
 computer.  In this case, the Arduino boards turns on an LED when
 it receives the character 'H', and turns off the LED when it
 receives the character 'L'.

 The data can be sent from the Arduino serial monitor, or another
 program like Processing (see code below), Flash (via a serial-net
 proxy), PD, or Max/MSP.

 The circuit:
 * LED connected from digital pin 13 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/PhysicalPixel
 */

const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup()
{
	// initialize serial communication:
	Serial.begin(9600);
	// initialize the LED pin as an output:
	pinMode(ledPin, OUTPUT);
}

void loop()
{
	// see if there's incoming serial data:
	if (Serial.available() > 0)
	{
		// read the oldest byte in the serial buffer:
		incomingByte = Serial.read();
		// if it's a capital H (ASCII 72), turn on the LED:
		if (incomingByte == 'H')
		{
			digitalWrite(ledPin, HIGH);
		}
		// if it's an L (ASCII 76) turn off the LED:
		if (incomingByte == 'L')
		{
			digitalWrite(ledPin, LOW);
		}
	}
}

/* Processing code for this example

 // mouseover serial

 // Demonstrates how to send data to the Arduino I/O board, in order to
 // turn ON a light if the mouse is over a square and turn it off
 // if the mouse is not.

 // created 2003-4
 // based on examples by Casey Reas and Hernando Barragan
 // modified 30 Aug 2011
 // by Tom Igoe
 // This example code is in the public domain.



 import processing.serial.*;

 float boxX;
 float boxY;
 int boxSize = 20;
 boolean mouseOverBox = false;

 Serial port;

 void setup() {
 size(200, 200);
 boxX = width/2.0;
 boxY = height/2.0;
 rectMode(RADIUS);

 // List all the available serial ports in the output pane.
 // You will need to choose the port that the Arduino board is
 // connected to from this list. The first port in the list is
 // port #0 and the third port in the list is port #2.
 // if using Processing 2.1 or later, use Serial.printArray()
 println(Serial.list());

 // Open the port that the Arduino board is connected to (in this case #0)
 // Make sure to open the port at the same speed Arduino is using (9600bps)
 port = new Serial(this, Serial.list()[0], 9600);

 }

 void draw()
 {
 background(0);

 // Test if the cursor is over the box
 if (mouseX > boxX-boxSize && mouseX < boxX+boxSize &&
 mouseY > boxY-boxSize && mouseY < boxY+boxSize) {
 mouseOverBox = true;
 // draw a line around the box and change its color:
 stroke(255);
 fill(153);
 // send an 'H' to indicate mouse is over square:
 port.write('H');
 }
 else {
 // return the box to it's inactive state:
 stroke(153);
 fill(153);
 // send an 'L' to turn the LED off:
 port.write('L');
 mouseOverBox = false;
 }

 // Draw the box
 rect(boxX, boxY, boxSize, boxSize);
 }
 */
```
<div style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;">Processing Code</span><br />
Copy the Processing code from the code sample above. As you mouse over the center square, the LED on pin 13 should turn on and off. The Processing applet looks like this:<span style="color: #4f4e4e; font-family: &quot;typoninesans regular&quot; , &quot;lucida grande&quot; , &quot;lucida&quot; , &quot;verdana&quot; , sans-serif;"><span style="background-color: white; border-color: initial; border-image-outset: initial; border-image-repeat: initial; border-image-slice: initial; border-image-source: initial; border-image-width: initial; border-style: initial; font-size: 18px; line-height: 31.5px;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/physicalPixel-output.png" style="border: 0px; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /></span></span></div>
Mouse over the square to turn the LED on and off.<br />
<br />
<br />
<br />
<h2 style="background-color: white; color: #666666; font-family: 'trebuchet ms', trebuchet, verdana, sans-serif; font-size: 22px; line-height: 20px; margin: 0px; position: relative; text-align: center;">
<div>
<span style="font-size: medium;">Want to save some time learning&nbsp;</span><span style="font-size: medium;">Arduino?</span></div>
<span style="font-size: medium;">Join the thousands of awesome people to sign up for our<br /><a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></span></h2>
</div>
</div>
</div>
