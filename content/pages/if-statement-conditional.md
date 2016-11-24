Title: If Statement Conditional: Use an ‘if statement’ to change the output conditions based on changing the input conditions.
status: hidden
URL:
save_as: pages/if-statement-conditional.html

The <a href="https://www.arduino.cc/en/Reference/If">if()</a> statement is the most basic of all programming control structures. It allows you to make something happen or not, depending on whether a given condition is true or not. It looks like this:<br />
<div>
<br /></div>
<div>
<pre style="background-color: #ecf1f1; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Monospace Regular 4', 'TyponineSans Monospace Light 5'; font-size: 15px; font-stretch: normal; line-height: 20px; margin-bottom: 1.5em; overflow-x: auto; padding: 5px 10px;">if (someCondition) {
   // do stuff if the condition is true
}</pre>
There is a common variation called if-else that looks like this:</div>
<div>
<br /></div>
<div>
<pre style="box-sizing: border-box; direction: ltr; font-stretch: normal; margin-bottom: 1.5em; overflow-x: auto; padding: 5px 10px;"><span style="background-color: #ecf1f1; color: #4f4e4e; font-family: &quot;typoninesans monospace regular 4&quot; , &quot;typoninesans monospace light 5&quot;; font-size: 15px; line-height: 20px;">if (someCondition) {
   // do stuff if the condition is true
} else {
   // do stuff if the condition is false
}</span>
</pre>
</div>
<div>
There's also the else-if, where you can check a second condition if the first is false:<br />
<pre style="box-sizing: border-box; direction: ltr; font-stretch: normal; margin-bottom: 1.5em; overflow-x: auto; padding: 5px 10px;"><span style="background-color: #ecf1f1; color: #4f4e4e; font-family: &quot;typoninesans monospace regular 4&quot; , &quot;typoninesans monospace light 5&quot;; font-size: 15px; line-height: 20px;">if (someCondition) {
   // do stuff if the condition is true
} else if (anotherCondition) {
   // do stuff only if the first condition is false
   // and the second condition is true
}
</span>
</pre>
You'll use if statements all the time. The example below turns on an LED on pin 13 (the built-in LED on many Arduino boards) if the value read on an analog input goes above a certain threshold.<br />
<br />
<span style="font-size: large;">Hardware Required</span><br />
<br />
<ul>
<li>Arduino or Genuino Board</li>
<li>Potentiometer or variable resistor</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
click the image to enlarge</div>
<div>
<br /></div>
<div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/if_noLED.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/if_noLED.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
Schematic<br />
<br />
click the image to enlarge</div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/ifStatement_sch_noLED.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/ifStatement_sch_noLED.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<br />
<span style="font-size: large;">Code</span><br />
<br />
In the code below, a variable called analogValue is used to store the data collected from a potentiometer connected to the board on analogPin 0. This data is then compared to a threshold value. If the analog value is found to be above the set threshold the built-in LED connected to digital pin 13 is turned on. If analogValue is found to be &lt; (less than) threshold, the LED remains off.</div>
<div>
<br /></div>
```
/*
  Conditionals - If statement

 This example demonstrates the use of if() statements.
 It reads the state of a potentiometer (an analog input) and turns on an LED
 only if the potentiometer goes above a certain threshold level. It prints the analog value
 regardless of the level.

 The circuit:
 * potentiometer connected to analog pin 0.
 Center pin of the potentiometer goes to the analog pin.
 side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 13 to ground

 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.

 created 17 Jan 2009
 modified 9 Apr 2012
 by Tom Igoe

This example code is in the public domain.

http://www.arduino.cc/en/Tutorial/IfStatement

 */

// These constants won't change:
const int analogPin = A0;    // pin that the sensor is attached to
const int ledPin = 13;       // pin that the LED is attached to
const int threshold = 400;   // an arbitrary threshold level that's in the range of the analog input

void setup()
{
	// initialize the LED pin as an output:
	pinMode(ledPin, OUTPUT);
	// initialize serial communications:
	Serial.begin(9600);
}

void loop()
{
	// read the value of the potentiometer:
	int analogValue = analogRead(analogPin);

	// if the analog value is high enough, turn on the LED:
	if (analogValue > threshold)
	{
		digitalWrite(ledPin, HIGH);
	}
	else
	{
		digitalWrite(ledPin, LOW);
	}

	// print the analog value:
	Serial.println(analogValue);
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
