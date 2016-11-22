Title: For Loop Iteration (aka The Knight Rider)
status: hidden

Often you want to iterate over a series of pins and do something to each one. For instance, this example blinks 6 LEDsattached to the Arduino or Genuino by using a <a href="https://www.arduino.cc/en/Reference/For">for()</a> loop to cycle back and forth through digital pins 2-7. The LEDS are turned on and off, in sequence, by using both the <a href="https://www.arduino.cc/en/Reference/DigitalWrite">digitalWrite()</a> and <a href="https://www.arduino.cc/en/Reference/Delay">delay()</a> functions .<br />
<br />
We also call this example "<a href="http://en.wikipedia.org/wiki/KITT">Knight Rider</a>" in memory of a TV-series from the 80's where David Hasselhoff had an AI machine named KITT driving his Pontiac. The car had been augmented with plenty of LEDs in all possible sizes performing flashy effects. In particular, it had a display that scanned back and forth across a line, as shown in this exciting <a href="https://www.youtube.com/watch?v=PO5E5mQIy_Q">fight between KITT and KARR</a>. This example duplicates the KITT display.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino or Genuino Board</li>
<li>6 220 ohm resistors</li>
<li>6 LEDs</li>
<li>hook-up wires</li>
<li>breadboard</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
<br />
Connect six LEDS, with 220 ohm resistors in series, to digital pins 2-7 on your Arduino.<br />
<br />
click the image to enlarge</div>
<div>
<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/forLoop_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/forLoop_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;">Schematic:</span><br />
<br />
click the image to enlarge</div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/forLoop2_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/forLoop2_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<br />
<span style="font-size: large;">Code</span><br />
<br />
The code below begins by utilizing a for() loop to assign digital pins 2-7 as outputs for the 6 LEDs used.<br />
<br />
In the main loop of the code, two for() loops are used to loop incrementally, stepping through the LEDs, one by one, from pin 2 to pin seven. Once pin 7 is lit, the process reverses, stepping back down through each LED.</div>
<div>
<br /></div>
<div>
<br /></div>
```
/*
  For Loop Iteration

 Demonstrates the use of a for() loop.
 Lights multiple LEDs in sequence, then in reverse.

 The circuit:
 * LEDs from pins 2 through 7 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/ForLoop
 */

int timer = 100;           // The higher the number, the slower the timing.

void setup()
{
	// use a for loop to initialize each pin as an output:
	for (int thisPin = 2; thisPin < 8; thisPin++)
	{
		pinMode(thisPin, OUTPUT);
	}
}

void loop()
{
	// loop from the lowest pin to the highest:
	for (int thisPin = 2; thisPin < 8; thisPin++)
	{
		// turn the pin on:
		digitalWrite(thisPin, HIGH);
		delay(timer);
		// turn the pin off:
		digitalWrite(thisPin, LOW);
	}

	// loop from the highest pin to the lowest:
	for (int thisPin = 7; thisPin >= 2; thisPin--)
	{
		// turn the pin on:
		digitalWrite(thisPin, HIGH);
		delay(timer);
		// turn the pin off:
		digitalWrite(thisPin, LOW);
	}
}
```
<h2 style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 22px; margin: 0px; position: relative;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our&nbsp;</div>
<div style="text-align: center;">
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
