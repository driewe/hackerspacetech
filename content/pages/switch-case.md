Title: Switch Case: How to choose between a discrete number of values.
status: hidden

An if statement allows you to choose between two discrete options, TRUE or FALSE. When there are more than two options, you can use multiple if statements, or you can use the <a href="https://www.arduino.cc/en/Reference/SwitchCase">switch</a> statement. Switch allows you to choose between several discrete options. This tutorial shows you how to use it to switch between four desired states of a photo resistor: really dark, dim, medium, and bright.<br />
<br />
This program first reads the photoresistor. Then it uses the map() function to map its output to one of four values: 0, 1, 2, or 3. Finally, it uses the switch() statement to print one of four messages back to the computer depending on which of the four values is returned.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino or Genuino Board</li>
<li>photoresistor, or another analog sensor</li>
<li>10k ohm resistors</li>
<li>hook-up wires</li>
<li>breadboard</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
The photoresistor is connected to analog in pin 0 using a <a href="http://www.tigoe.com/pcomp/code/controllers/input-output/analog-input/">voltage divider</a> circuit. A 10K ohm resistor makes up the other side of the voltage divider, running from Analog in 0 to ground. The analogRead() function returns a range of about 0 to 600 from this circuit in a reasonably lit indoor space.<br />
<br />
click the image to enlarge</div>
<div>
<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/switchCase_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/switchCase_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
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
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/switchCase_N_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/switchCase2_N_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
```
/*
  Switch statement

 Demonstrates the use of a switch statement.  The switch
 statement allows you to choose from among a set of discrete values
 of a variable.  It's like a series of if statements.

 To see this sketch in action, but the board and sensor in a well-lit
 room, open the serial monitor, and and move your hand gradually
 down over the sensor.

 The circuit:
 * photoresistor from analog in 0 to +5V
 * 10K resistor from analog in 0 to ground

 created 1 Jul 2009
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SwitchCase
 */

// these constants won't change. They are the
// lowest and highest readings you get from your sensor:
const int sensorMin = 0;      // sensor minimum, discovered through experiment
const int sensorMax = 600;    // sensor maximum, discovered through experiment

void setup()
{
	// initialize serial communication:
	Serial.begin(9600);
}

void loop()
{
	// read the sensor:
	int sensorReading = analogRead(A0);
	// map the sensor range to a range of four options:
	int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

	// do something different depending on the
	// range value:
	switch (range)
	{
		case 0:    // your hand is on the sensor
			Serial.println("dark");
			break;
		case 1:    // your hand is close to the sensor
			Serial.println("dim");
			break;
		case 2:    // your hand is a few inches from the sensor
			Serial.println("medium");
			break;
		case 3:    // your hand is nowhere near the sensor
			Serial.println("bright");
			break;
	}
	delay(1);        // delay in between reads for stability
}
```
<br />
<h2 style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 22px; margin: 0px; position: relative;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our&nbsp;</div>
<div style="text-align: center;">
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
