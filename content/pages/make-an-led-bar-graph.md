Title: Make An LED Bar Graph
status: hidden

The bar graph - a series of LEDs in a line, such as you see on an audio display - is a common hardware display for analog sensors. It's made up of a series of LEDs in a row, an analog input like a potentiometer, and a little code in between. You can buy multi-LED bar graph displays fairly cheaply, like <a href="http://www.digikey.com/product-detail/en/MV54164/1080-1183-ND/2675674">this one</a>. This tutorial demonstrates how to control a series ofLEDs in a row, but can be applied to any series of digital outputs.<br />
<br />
This tutorial borrows from the <a href="http://www.arduino.cc/en/Tutorial/Loop">For Loop and Arrays</a> tutorial as well as the <a href="http://www.arduino.cc/en/Tutorial/AnalogInput">Analog Input</a> tutorial.<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<img alt="A bar graph display" src="http://media.digikey.com/photos/Lite%20On%20Photos/LITE-ON%20INC-%20LTA-1000G.jpg" style="border: 0px; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="A bar graph display" width="200px" /></div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<br />
<ul>
<li>Arduino</li>
<li>LED bar graph display or 10 LEDs</li>
<li>Potentiometer</li>
<li>10 220 ohm resistors</li>
<li>hook-up wires</li>
<li>breadboard</li>
</ul>
<div>
<span style="font-size: large;">Circuit</span><br />
<br />
<br />
click the image to enlarge<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="http://www.arduino.cc/en/uploads/Tutorial/BarGraph_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="http://www.arduino.cc/en/uploads/Tutorial/BarGraph_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
<br />
<span style="font-size: large;">Schematic:</span><br />
<br />
click the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="http://www.arduino.cc/en/uploads/Tutorial/BarGraph2_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="http://www.arduino.cc/en/uploads/Tutorial/BarGraph2_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<br />
<span style="font-size: large;">Code</span><br />
<br />
The sketch works like this: first you read the input. You map the input value to the output range, in this case ten LEDs. Then you set up a <a href="http://www.arduino.cc/en/Tutorial/Loop">for loop</a> to iterate over the outputs. If the output's number in the series is lower than the mapped input range, you turn it on. If not, you turn it off.</div>
<div>
<br /></div>
```
/*
  LED bar graph

  Turns on a series of LEDs based on the value of an analog sensor.
  This is a simple way to make a bar graph display. Though this graph
  uses 10 LEDs, you can use any number by changing the LED count
  and the pins in the array.

  This method can be used to control any series of digital outputs that
  depends on an analog input.

  The circuit:
   * LEDs from pins 2 through 11 to ground

 created 4 Sep 2010
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/BarGraph
 */


// these constants won't change:
const int analogPin = A0;   // the pin that the potentiometer is attached to
const int ledCount = 10;    // the number of LEDs in the bar graph

int ledPins[] =
{
	2, 3, 4, 5, 6, 7, 8, 9, 10, 11
};   // an array of pin numbers to which LEDs are attached


void setup()
{
	// loop over the pin array and set them all to output:
	for (int thisLed = 0; thisLed < ledCount; thisLed++)
	{
		pinMode(ledPins[thisLed], OUTPUT);
	}
}

void loop()
{
	// read the potentiometer:
	int sensorReading = analogRead(analogPin);
	// map the result to a range from 0 to the number of LEDs:
	int ledLevel = map(sensorReading, 0, 1023, 0, ledCount);

	// loop over the LED array:
	for (int thisLed = 0; thisLed < ledCount; thisLed++)
	{
		// if the array element's index is less than ledLevel,
		// turn the pin for this element on:
		if (thisLed < ledLevel)
		{
			digitalWrite(ledPins[thisLed], HIGH);
		}
		// turn off all pins higher than the ledLevel:
		else
		{
			digitalWrite(ledPins[thisLed], LOW);
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
