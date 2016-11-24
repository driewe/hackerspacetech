Title: Graph: Send data to the computer and graph it in Processing.
status: hidden

This example shows you how to send a byte of data from the Arduino or Genuino to a personal computer and graph the result. This is called serial communication because the connection appears to both the board and the computer as a serial port, even though it may actually use a USB cable, a serial to USB and a USB to serial converter.<br />
<br />
You can use the serial monitor of the Arduino Software (IDE) to view the sent data, or it can be read by Processing (see code below), Flash, PD, Max/MSP, etc.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<br />
Arduino<br />
Analog Sensor (potentiometer, photocell, FSR, etc.)<br />
Software Required<br />
<a href="http://www.processing.org/">Processing</a><br />
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Connect a potentiometer or other analog sensor to analog input 0.<br />
<br />
click the image to enlarge<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/graph-circuit3.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/graph-circuit3.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;">Schematic</span><br />
<br />
click the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/AnalogReadSerial_sch.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  height="400px" src="https://www.arduino.cc/en/uploads/Tutorial/AnalogReadSerial_sch.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<br /></div>
</div>
<span style="font-size: large;">Code</span><br />
<div>
<br /></div>
</div>
```
/*
  Graph

 A simple example of communication from the Arduino board to the computer:
 the value of analog input 0 is sent out the serial port.  We call this "serial"
 communication because the connection appears to both the Arduino and the
 computer as a serial port, even though it may actually use
 a USB cable. Bytes are sent one after another (serially) from the Arduino
 to the computer.

 You can use the Arduino serial monitor to view the sent data, or it can
 be read by Processing, PD, Max/MSP, or any other program capable of reading
 data from a serial port.  The Processing code below graphs the data received
 so you can see the value of the analog input changing over time.

 The circuit:
 Any analog input sensor is attached to analog in pin 0.

 created 2006
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Graph
 */

void setup()
{
	// initialize the serial communication:
	Serial.begin(9600);
}

void loop()
{
	// send the value of analog input 0:
	Serial.println(analogRead(A0));
	// wait a bit for the analog-to-digital converter
	// to stabilize after the last reading:
	delay(2);
}

/* Processing code for this example

 // Graphing sketch


// This program takes ASCII-encoded strings
// from the serial port at 9600 baud and graphs them. It expects values in the
// range 0 to 1023, followed by a newline, or newline and carriage return

// Created 20 Apr 2005
// Updated 24 Nov 2015
// by Tom Igoe
// This example code is in the public domain.

import processing.serial.*;

Serial myPort;        // The serial port
int xPos = 1;         // horizontal position of the graph
float inByte = 0;

void setup () {
  // set the window size:
  size(400, 300);

  // List all the available serial ports
  // if using Processing 2.1 or later, use Serial.printArray()
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  Arduino, so I open Serial.list()[0].
  // Open whatever port is the one you're using.
  myPort = new Serial(this, Serial.list()[0], 9600);

  // don't generate a serialEvent() unless you get a newline character:
  myPort.bufferUntil('\n');

  // set inital background:
  background(0);
}
void draw () {
  // draw the line:
  stroke(127, 34, 255);
  line(xPos, height, xPos, height - inByte);

  // at the edge of the screen, go back to the beginning:
  if (xPos >= width) {
    xPos = 0;
    background(0);
  } else {
    // increment the horizontal position:
    xPos++;
  }
}


void serialEvent (Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');

  if (inString != null) {
    // trim off any whitespace:
    inString = trim(inString);
    // convert to an int and map to the screen height:
    inByte = float(inString);
    println(inByte);
    inByte = map(inByte, 0, 1023, 0, height);
  }
}

*/
```
<br />
<span style="font-size: large;">Processing Sketch</span><br />
<br />
Using the Processing sketch in the code sample above, you'll get a graph of the sensor's value. As you change the value of the analog sensor, you'll get a graph something like this:<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<img src="https://www.arduino.cc/en/uploads/Tutorial/graph-output.png" style="border: 0px; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" /><br />
<br />
<br />
<div style="color: #666666; font-family: 'trebuchet ms', trebuchet, verdana, sans-serif; font-size: 22px; font-weight: bold; line-height: 20px; text-align: center;">
<span style="font-size: medium;">Want to save some time learning&nbsp;</span><span style="font-size: medium;">Arduino?</span></div>
<span style="color: #666666; font-family: &quot;trebuchet ms&quot; , &quot;trebuchet&quot; , &quot;verdana&quot; , sans-serif; font-size: medium; font-weight: bold; line-height: 20px; text-align: center;"></span><br />
<div style="text-align: center;">
Join the thousands of awesome people to sign up for our<br />
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</div>
