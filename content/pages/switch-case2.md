Title: Switch Case 2: A second switch-case example, showing how to take different actions based on the characters received in the serial port.
status: hidden
URL:
save_as: pages/switch-case2.html

An if statement allows you to choose between two discrete options, TRUE or FALSE. When there are more than two options, you can use multiple if statements, or you can use the <a href="http://www.arduino.cc/en/Reference/SwitchCase">switch</a> statement. Switch allows you to choose between several discrete options.<br />
<br />
This tutorial shows you how to use switch to turn on one of several different LEDs based on a byte of data received serially. The sketch listens for serial input, and turns on a different LED for the characters a, b, c, d, or e.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino</li>
<li>5 LEDs</li>
<li>5 220 ohm resistors</li>
<li>hook-up wires</li>
<li>breadboard</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Five LEDs are attached to digital pins 2, 3, 4, 5, and 6 in series through 220 ohm resistors.<br />
<br />
To make this sketch work, your board must be connected to your computer. In the Arduino IDE open the serial monitor and send the characters a, b, c, d, or e to lit up the corresponding LED, or anything else to switch them off.<br />
<br />
click the image to enlarge</div>
<div>
<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="http://www.arduino.cc/en/uploads/Tutorial/switchCase2_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="http://www.arduino.cc/en/uploads/Tutorial/switchCase2_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
Schematic<br />
<br />
click the image to enlarge</div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="http://www.arduino.cc/en/uploads/Tutorial/SwitchCase2.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="http://www.arduino.cc/en/uploads/Tutorial/SwitchCase2.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<span style="font-size: large;">Code</span></div>
<div>
<span style="font-size: large;"><br /></span></div>
```
/*
  Switch statement  with serial input

 Demonstrates the use of a switch statement.  The switch
 statement allows you to choose from among a set of discrete values
 of a variable.  It's like a series of if statements.

 To see this sketch in action, open the Serial monitor and send any character.
 The characters a, b, c, d, and e, will turn on LEDs.  Any other character will turn
 the LEDs off.

 The circuit:
 * 5 LEDs attached to digital pins 2 through 6 through 220-ohm resistors

 created 1 Jul 2009
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SwitchCase2
 */

void setup()
{
	// initialize serial communication:
	Serial.begin(9600);
	// initialize the LED pins:
	for (int thisPin = 2; thisPin < 7; thisPin++)
	{
		pinMode(thisPin, OUTPUT);
	}
}

void loop()
{
	// read the sensor:
	if (Serial.available() > 0)
	{
		int inByte = Serial.read();
		// do something different depending on the character received.
		// The switch statement expects single number values for each case;
		// in this exmaple, though, you're using single quotes to tell
		// the controller to get the ASCII value for the character.  For
		// example 'a' = 97, 'b' = 98, and so forth:

		switch (inByte)
		{
			case 'a':
				digitalWrite(2, HIGH);
				break;
			case 'b':
				digitalWrite(3, HIGH);
				break;
			case 'c':
				digitalWrite(4, HIGH);
				break;
			case 'd':
				digitalWrite(5, HIGH);
				break;
			case 'e':
				digitalWrite(6, HIGH);
				break;
			default:
				// turn all the LEDs off:
				for (int thisPin = 2; thisPin < 7; thisPin++)
				{
					digitalWrite(thisPin, LOW);
				}
		}
	}
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
