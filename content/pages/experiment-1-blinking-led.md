Title: Experiment 1: Blinking an LED
status: hidden

*Adapted from [Sparkfun Inventor Kit Experiential Guide](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570)*

###Introduction

LEDs are small, powerful lights that are used in many different applications. To start off, we will work on blinking an LED, the Hello World of microcontrollers. That’s right - it’s as simple as turning a light on and off. It might not seem like much, but establishing this important baseline will give you a solid foundation as we work toward more complex experiments.

###Parts Needed

####You will need the following parts:

* Breadboard
* Redboard or Arduino Uno R3
* 1x LED
* 1x 330Ω Resistor
* 2x Jumper Wires

###Hardware hookup

Ready to start hooking everything up? Check out the Fritzing diagram and hookup table below, to see how everything is connected.

*Please note: Pay close attention to the LED. The negative side of the LED is the short leg, marked with a flat edge.*

Components like resistors need to have their legs bent into 90° angles in order to correctly fit the breadboard sockets. You can also cut the legs shorter to make them easier to work with on the breadboard.

###Fritzing Diagram for RedBoard

<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_01_02_1.png"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_01_02_1.png"></a>


```
/*
SparkFun Inventor's Kit
Example sketch 01

BLINKING A LED

  Turn an LED on for one second, off for one second,
  and repeat forever.

Hardware connections:

  Most Arduinos already have an LED and resistor connected to
  pin 13, so you may not need any additional circuitry.

  But if you'd like to connect a second LED to pin 13, or use
  a different pin, follow these steps:

    Connect the positive side of your LED (longer leg) to Arduino
    digital pin 13 (or another digital pin, don't forget to change
    the code to match).
  
    Connect the negative side of your LED (shorter leg) to a 
    330 Ohm resistor (orange-orange-brown). Connect the other side
    of the resistor to ground.

    pin 13 _____ + LED - _____ 330 Ohm _____ GND
	
    (We always use resistors between the Arduino and and LEDs
    to keep the LEDs from burning out due to too much current.)

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/


// Welcome to Arduino!

// If you're brand-new to this, there will be some new things to
// learn, but we'll jump right in and explain things as we go.

// The Arduino is a tiny computer that runs programs called
// "sketches". These are text files written using instructions
// the computer understances. You're reading a sketch right now.

// Sketches have computer code in them, but also (hopefully)
// "comments" that explain what the code does. Comments and code
// will have different colors in the editor so you can tell them
// apart.

// This is a comment - anything on a line after "//" is ignored
// by the computer.

/* This is also a comment - this one can be multi-line, but it
must start and end with these characters */

// A "function" is a named block of code, that performs a specific,
// well, function. Many useful functions are already built-in to
// the Arduino; others you'll name and write yourself for your
// own purposes.

// All Arduino sketches MUST have two specific functions, named
// "setup()" and "loop()". The Arduino runs these functions
// automatically when it starts up or if you press the reset
// button. You'll typically fill these function "shells" with your
// own code. Let's get started!


// The setup() function runs once when the sketch starts.
// You'll use it for things you need to do first, or only once:


void setup()
{
  // The Arduino has 13 digital input/output pins. These pins
  // can be configured as either inputs or outputs. We set this
  // up with a built-in function called pinMode().

  // The pinMode() function takes two values, which you type in
  // the parenthesis after the function name. The first value is
  // a pin number, the second value is the word INPUT or OUTPUT.
  
  // Here we'll set up pin 13 (the one connected to a LED) to be
  // an output. We're doing this because we need to send voltage
  // "out" of the Arduino to the LED.

  pinMode(13, OUTPUT);

  // By the way, the Arduino offers many useful built-in functions
  // like this one. You can find information on all of them at the
  // Arduino website: http://arduino.cc/en/Reference
}


// After setup() finishes, the loop() function runs over and over
// again, forever (or until you turn off or reset the Arduino).
// This is usually where the bulk of your program lives:


void loop()
{
  // The 13 digital pins on your Arduino are great at inputting
  // and outputting on/off, or "digital" signals. These signals
  // will always be either 5 Volts (which we call "HIGH"), or
  // 0 Volts (which we call "LOW").

  // Because we have an LED connected to pin 13, if we make that
  // output HIGH, the LED will get voltage and light up. If we make
  // that output LOW, the LED will have no voltage and turn off.

  // digitalWrite() is the built-in function we use to make an
  // output pin HIGH or LOW. It takes two values; a pin number,
  // followed by the word HIGH or LOW:

  digitalWrite(13, HIGH);   // Turn on the LED

  // delay() is a function that pauses for a given amount of time.
  // It takes one value, the amount of time to wait, measured in
  // milliseconds. There are 1000 milliseconds in a second, so if
  // you delay(1000), it will pause for exactly one second:
  
  delay(1000);              // Wait for one second
  
  digitalWrite(13, LOW);    // Turn off the LED
  
  delay(1000);              // Wait for one second

  // All together, the above code turns the LED on, waits one
  // second, turns it off, and waits another second.

  // When the computer gets to the end of the loop() function,
  // it starts loop() over again. So this program will continue
  // blinking the LED on and off!

  // Try changing the 1000 in the above delay() functions to
  // different numbers and see how it affects the timing. Smaller
  // values will make the loop run faster. (Why?)
}
```

###Code to Note</h3>
```pinMode(13, OUTPUT);```
Before you can use one of the Arduino’s pins, you need to tell the RedBoard or Arduino Uno R3 whether it is an INPUT or OUTPUT. We use a built-in “function” called ```pinMode()``` to do this.

```digitalWrite(13, HIGH)```

When you’re using a pin as an OUTPUT, you can command it to be HIGH (output 5 volts), or LOW (output 0 volts).

###What You Should See
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You should see your LED blink on and off. If it isn’t, make sure you have assembled the circuit correctly and verified and uploaded the code to your board, or see the troubleshooting section.</div>
<div class="row" style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_01_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_01_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="box-sizing: border-box; margin-bottom: 10px;">
Almost all modern flat screen televisions and monitors have LED indicator lights to show they are on or off.</div>
<div style="box-sizing: border-box; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/circuit_01_rwa_02.png" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/circuit_01_rwa_02.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<div class="row" style="background-color: white; box-sizing: border-box; margin-left: -15px; margin-right: -15px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Questions:</h3>
<div>
<ol>
<li><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;">Which instruction controls the duration for which the LED it lit?</span></span></li>
<li><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;">Symbolically, what is the difference between a diode and an LED?</span></span></li>
<li><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;">What is the function of the 330 ohm resistor in the circuit?</span></span></li>
</ol>
<div>
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;"><br /></span></span></div>
</div>
</div>


<center>
[Experiment 2: Reading a Potentiometer](/pages/experiment-2-reading-a-potentiometer.html)

*Adapted from [Sparkfun Inventor Kit Experiential Guide](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570)*
</center>




