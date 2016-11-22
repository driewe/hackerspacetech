Title: While Statement Conditional: How to use a while loop to calibrate a sensor while a button is being read.
status: hidden
URL:
save_as: pages/while-statement-conditional.html

Sometimes you want everything in the program to stop while a given condition is true. You can do this using a <a href="http://www.arduino.cc/en/Reference/While">while loop</a>. This example shows how to use a while loop to <a href="http://www.arduino.cc/en/Tutorial/Calibration">calibrate</a> the value of an analog sensor.<br />
<br />
In the main loop, the sketch below reads the value of a photoresistor on analog pin 0 and uses it to fade an LED on pin 9. But while a button attached to digital pin 2 is pressed, the program runs a method called calibrate() that looks for the highest and lowest values of the analog sensor. When you release the button, the sketch continues with the main loop.<br />
<br />
This technique lets you update the maximum and minimum values for the photoresistor when the lighting conditions change.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino</li>
<li>pushbutton or switch</li>
<li>photoresistor or another analog sensor</li>
<li>2 10k ohm resistors</li>
<li>breadboard</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Connect your analog sensor (e.g. potentiometer, light sensor) on analog input 2 with a 10K ohm resistor to ground. Connect your button to digital pin, again with a 10K ohm resistor to ground. Connect your LED to digital pin 9, with a 220 ohm resistor in series.<br />
<br />
click the image to enlarge<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="http://www.arduino.cc/en/uploads/Tutorial/while_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="http://www.arduino.cc/en/uploads/Tutorial/while_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="600px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;">Schematic</span><br />
<br />
click the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="http://www.arduino.cc/en/uploads/Tutorial/whileloop_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="http://www.arduino.cc/en/uploads/Tutorial/whileloop_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<span style="font-size: large;">Code</span></div>
<div>
<span style="font-size: large;"><br /></span></div>
```
/*
  Conditionals - while statement

 This example demonstrates the use of  while() statements.

 While the pushbutton is pressed, the sketch runs the calibration routine.
 The  sensor readings during the while loop define the minimum and maximum
 of expected values from the photo resistor.

 This is a variation on the calibrate example.

 The circuit:
 * photo resistor connected from +5V to analog in pin 0
 * 10K resistor connected from ground to analog in pin 0
 * LED connected from digital pin 9 to ground through 220 ohm resistor
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground

 created 17 Jan 2009
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/WhileLoop

 */


// These constants won't change:
const int sensorPin = A2;       // pin that the sensor is attached to
const int ledPin = 9;           // pin that the LED is attached to
const int indicatorLedPin = 13; // pin that the built-in LED is attached to
const int buttonPin = 2;        // pin that the button is attached to


// These variables will change:
int sensorMin = 1023;  // minimum sensor value
int sensorMax = 0;     // maximum sensor value
int sensorValue = 0;         // the sensor value


void setup()
{
	// set the LED pins as outputs and the switch pin as input:
	pinMode(indicatorLedPin, OUTPUT);
	pinMode(ledPin, OUTPUT);
	pinMode(buttonPin, INPUT);
}

void loop()
{
	// while the button is pressed, take calibration readings:
	while (digitalRead(buttonPin) == HIGH)
	{
		calibrate();
	}
	// signal the end of the calibration period
	digitalWrite(indicatorLedPin, LOW);

	// read the sensor:
	sensorValue = analogRead(sensorPin);

	// apply the calibration to the sensor reading
	sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

	// in case the sensor value is outside the range seen during calibration
	sensorValue = constrain(sensorValue, 0, 255);

	// fade the LED using the calibrated value:
	analogWrite(ledPin, sensorValue);
}

void calibrate()
{
	// turn on the indicator LED to indicate that calibration is happening:
	digitalWrite(indicatorLedPin, HIGH);
	// read the sensor:
	sensorValue = analogRead(sensorPin);

	// record the maximum sensor value
	if (sensorValue > sensorMax)
	{
		sensorMax = sensorValue;
	}

	// record the minimum sensor value
	if (sensorValue < sensorMin)
	{
		sensorMin = sensorValue;
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
