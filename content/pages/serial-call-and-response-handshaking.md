Title: Serial Call and Response (handshaking)
status: hidden

This example demonstrates multi-byte communication from the Arduino or Genuino board to the computer using a call-and-response (handshaking) method.<br />
<br />
This sketch sends an ASCII A (byte of value 65) on startup and repeats that until it gets a serial response from the computer. Then it sends three sensor values as single bytes, and waits for another response from the computer.<br />
<br />
You can use the Arduino Software (IDE) serial monitor to view the sent data, or it can be read by Processing (see code below), Flash, PD, Max/MSP (see example below), etc.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino</li>
<li>2 analog sensors (potentiometer, photocell, FSR, etc.)</li>
<li>pushbutton</li>
<li>3 10K ohm resistors</li>
<li>hook-up wires</li>
<li>breadboard</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Software Required</span></div>
<div>
<ul>
<li><a href="http://www.processing.org/">Processing</a></li>
</ul>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Connect analog sensors to analog input pin 0 and 1 with 10K ohm resistors used as voltage dividers. Connect a pushbutton or switch to digital I/O pin 2 with a 10K ohm resistor as a reference to ground.<br />
<br />
click on the image to enlarge</div>
<div>
<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/SerialCallResponse-circuit3.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/SerialCallResponse-circuit3.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;">Schematic</span><br />
<br />
click the image to enlarge</div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/SerialCallResponse_sch.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/SerialCallResponse_sch.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<span style="font-size: large;">Code</span></div>
```
/*
  Serial Call and Response
 Language: Wiring/Arduino

 This program sends an ASCII A (byte of value 65) on startup
 and repeats that until it gets some data in.
 Then it waits for a byte in the serial port, and
 sends three sensor values whenever it gets a byte in.

 Thanks to Greg Shakar and Scott Fitzgerald for the improvements

   The circuit:
 * potentiometers attached to analog inputs 0 and 1
 * pushbutton attached to digital I/O 2

 Created 26 Sept. 2005
 by Tom Igoe
 modified 24 April 2012
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SerialCallResponse

 */

int firstSensor = 0;    // first analog sensor
int secondSensor = 0;   // second analog sensor
int thirdSensor = 0;    // digital sensor
int inByte = 0;         // incoming serial byte

void setup()
{
	// start serial port at 9600 bps:
	Serial.begin(9600);
	while (!Serial)
	{
		; // wait for serial port to connect. Needed for native USB port only
	}

	pinMode(2, INPUT);   // digital sensor is on digital pin 2
	establishContact();  // send a byte to establish contact until receiver responds
}

void loop()
{
	// if we get a valid byte, read analog ins:
	if (Serial.available() > 0)
	{
		// get incoming byte:
		inByte = Serial.read();
		// read first analog input, divide by 4 to make the range 0-255:
		firstSensor = analogRead(A0) / 4;
		// delay 10ms to let the ADC recover:
		delay(10);
		// read second analog input, divide by 4 to make the range 0-255:
		secondSensor = analogRead(1) / 4;
		// read  switch, map it to 0 or 255L
		thirdSensor = map(digitalRead(2), 0, 1, 0, 255);
		// send sensor values:
		Serial.write(firstSensor);
		Serial.write(secondSensor);
		Serial.write(thirdSensor);
	}
}

void establishContact()
{
	while (Serial.available() <= 0)
	{
		Serial.print('A');   // send a capital A
		delay(300);
	}
}

/*
Processing sketch to run with this example:

// This example code is in the public domain.

import processing.serial.*;

int bgcolor;                 // Background color
int fgcolor;                 // Fill color
Serial myPort;                       // The serial port
int[] serialInArray = new int[3];    // Where we'll put what we receive
int serialCount = 0;                 // A count of how many bytes we receive
int xpos, ypos;                  // Starting position of the ball
boolean firstContact = false;        // Whether we've heard from the microcontroller

void setup() {
  size(256, 256);  // Stage size
  noStroke();      // No border on the next thing drawn

  // Set the starting position of the ball (middle of the stage)
  xpos = width/2;
  ypos = height/2;

  // Print a list of the serial ports for debugging purposes
  // if using Processing 2.1 or later, use Serial.printArray()
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  FTDI adaptor, so I open Serial.list()[0].
  // On Windows machines, this generally opens COM1.
  // Open whatever port is the one you're using.
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 9600);
}

void draw() {
  background(bgcolor);
  fill(fgcolor);
  // Draw the shape
  ellipse(xpos, ypos, 20, 20);
}

void serialEvent(Serial myPort) {
  // read a byte from the serial port:
  int inByte = myPort.read();
  // if this is the first byte received, and it's an A,
  // clear the serial buffer and note that you've
  // had first contact from the microcontroller.
  // Otherwise, add the incoming byte to the array:
  if (firstContact == false) {
    if (inByte == 'A') {
      myPort.clear();          // clear the serial port buffer
      firstContact = true;     // you've had first contact from the microcontroller
      myPort.write('A');       // ask for more
    }
  }
  else {
    // Add the latest byte from the serial port to array:
    serialInArray[serialCount] = inByte;
    serialCount++;

    // If we have 3 bytes:
    if (serialCount > 2 ) {
      xpos = serialInArray[0];
      ypos = serialInArray[1];
      fgcolor = serialInArray[2];

      // print the values (for debugging purposes only):
      println(xpos + "\t" + ypos + "\t" + fgcolor);

      // Send a capital A to request new sensor readings:
      myPort.write('A');
      // Reset serialCount:
      serialCount = 0;
    }
  }
}
*/
```
<br />
<span style="font-size: large;">Processing Code</span><br />
<br />
Copy the Processing sketch from the code sample above. As you change the value of the analog sensor, you'll get a ball moving onscreen something like this. The ball will appear only when you push the button:<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/serialCallResponse-output.png" style="border: 0px; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /></div>
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<br /></div>
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<h2 style="color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 22px; margin: 0px; position: relative;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our&nbsp;</div>
<div style="text-align: center;">
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
</div>
