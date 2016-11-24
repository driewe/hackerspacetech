Title: Arrays: A variation on the For Loop example that demonstrates how to use an array
status: hidden

This variation on the <a href="https://www.arduino.cc/en/Tutorial/ForLoopIteration">For Loop Iteration</a> example shows how to use an <a href="https://www.arduino.cc/en/Reference/Array">array</a>. An array is a variable with multiple parts. If you think of a variable as a cup that holds values, you might think of an array as an ice cube tray. It's like a series of linked cups, all of which can hold the same maximum value.<br />
<br />
The <a href="https://www.arduino.cc/en/Tutorial/ForLoopIteration">For Loop Iteration</a> example shows you how to light up a series of LEDs attached to pins 2 through 7 of the Arduino or Genuino board, with certain limitations (the pins have to be numbered contiguously, and the LEDs have to be turned on in sequence).<br />
<br />
This example shows you how you can turn on a sequence of pins whose numbers are neither contiguous nor necessarily sequential. To do this is, you can put the pin numbers in an array and then use for loops to iterate over the array.<br />
<br />
This example makes use of 6 LEDs connected to the pins 2 - 7 on the board using 220 ohm resistors, just like in the For Loop. However, here the order of the LEDs is determined by their order in the array, not by their physical order.<br />
<br />
This technique of putting the pins in an array is very handy. You don't have to have the pins sequential to one another, or even in the same order. You can rearrange them in any order you want.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino or Genuino Board</li>
<li>6 LEDs</li>
<li>6 220 ohm resistors</li>
<li>hook-up wires</li>
<li>breadboard</li>
<li>Circuit</li>
</ul>
Connect six LEDs, with 220 ohm resistors in series, to digital pins 2-7 on your board.<br />
<br />
click the image to enlarge</div>
<div>
<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/forLoop_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/forLoop_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
<br />
<span style="font-size: large;">Schematic:</span><br />
<br />
click the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/forLoop2_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img  src="https://www.arduino.cc/en/uploads/Tutorial/forLoop2_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<span style="font-size: large;">Code</span></div>
<div>
<span style="font-size: large;"><br /></span></div>
```
/*
  Arrays

 Demonstrates the use of  an array to hold pin numbers
 in order to iterate over the pins in a sequence.
 Lights multiple LEDs in sequence, then in reverse.

 Unlike the For Loop tutorial, where the pins have to be
 contiguous, here the pins can be in any random order.

 The circuit:
 * LEDs from pins 2 through 7 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Array
 */

int timer = 100;           // The higher the number, the slower the timing.
int ledPins[] = {
  2, 7, 4, 6, 5, 3
};       // an array of pin numbers to which LEDs are attached
int pinCount = 6;           // the number of pins (i.e. the length of the array)

void setup() {
  // the array elements are numbered from 0 to (pinCount - 1).
  // use a for loop to initialize each pin as an output:
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }
}

void loop() {
  // loop from the lowest pin to the highest:
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(ledPins[thisPin], LOW);

  }

  // loop from the highest pin to the lowest:
  for (int thisPin = pinCount - 1; thisPin >= 0; thisPin--) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(ledPins[thisPin], LOW);
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
<br />