Title: Experiment 5: Push Buttons
status: hidden

<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="font-size: xx-small;"><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></span></h3>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Introduction</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Up until now, we’ve focused mostly on outputs. Now we’re going to go to the other end of spectrum and play around with inputs. In experiment 2, we used an analog input to read the potentiometer. In this circuit, we’ll be reading in one of the most common and simple inputs – a push button – by using a digital input. The way a push button works with your RedBoard or Arduino Uno R3 is that when the button is pushed, the voltage goes LOW. You RedBoard or Arduino Uno R3 reads this and reacts accordingly.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
In this circuit, you will also use a&nbsp;<a href="https://learn.sparkfun.com/tutorials/pull-up-resistors" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;" target="_blank">pull-up resistor</a>, which keeps the voltage HIGH when you’re not pressing the button.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Parts Needed</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You will need the following parts:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Breadboard</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RedBoard or Arduino Uno</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;LED</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;330Ω Resistor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">7x</span>&nbsp;Jumper Wires</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">2x</span>&nbsp;Push Buttons</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">2x</span>&nbsp;10k Resistors</li>
</ul>
<div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Suggested Reading</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Before continuing on with this tutorial, we recommend you be somewhat familiar with the concepts in these tutorials:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><a href="https://learn.sparkfun.com/tutorials/switch-basics" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;" target="_blank">Switch Basics</a></li>
<li style="box-sizing: border-box;"><a href="https://learn.sparkfun.com/tutorials/analog-vs-digital" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;" target="_blank">Analog vs. Digital</a></li>
</ul>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Hardware Hookup</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Ready to start hooking everything up? Check out the Fritzing diagram and hookup table below, to see how everything is connected.</div>
<table class="table table-bordered" style="background-color: white; border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 640px;"><tbody style="box-sizing: border-box;">
<tr class="warning" style="box-sizing: border-box;"><td align="center" class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Polarized Components&nbsp;<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td align="left" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Pay special attention to the component’s markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction.</td></tr>
</tbody></table>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Fritzing Diagram for RedBoard</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_05_01.png" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_05_01.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<em style="box-sizing: border-box;">Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.</em></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: left;">
<em style="box-sizing: border-box;"></em></div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Run the Sketch</h3>
</div>
</div>
<div>
<br /></div>
```
/*
SparkFun Inventor's Kit
Example sketch 05

PUSH BUTTONS

  Use pushbuttons for digital input

  Previously we've used the analog pins for input, now we'll use
  the digital pins for input as well. Because digital pins only
  know about HIGH and LOW signals, they're perfect for interfacing
  to pushbuttons and switches that also only have "on" and "off"
  states.
  
  We'll connect one side of the pushbutton to GND, and the other
  side to a digital pin. When we press down on the pushbutton,
  the pin will be connected to GND, and therefore will be read
  as "LOW" by the Arduino.
  
  But wait - what happens when you're not pushing the button?
  In this state, the pin is disconnected from everything, which 
  we call "floating". What will the pin read as then, HIGH or LOW?
  It's hard to say, because there's no solid connection to either
  5 Volts or GND. The pin could read as either one.
  
  To deal with this issue, we'll connect a small (10K, or 10,000 Ohm)
  resistance between the pin and 5 Volts. This "pullup" resistor
  will ensure that when you're NOT pushing the button, the pin will
  still have a weak connection to 5 Volts, and therefore read as
  HIGH.
  
  (Advanced: when you get used to pullup resistors and know when
  they're required, you can activate internal pullup resistors
  on the ATmega processor in the Arduino. See
  http://arduino.cc/en/Tutorial/DigitalPins for information.)

Hardware connections:

  Pushbuttons:
  
    Pushbuttons have two contacts that are connected if you're
    pushing the button, and disconnected if you're not.
    
    The pushbuttons we're using have four pins, but two pairs
    of these are connected together. The easiest way to hook up
    the pushbutton is to connect two wires to any opposite corners.

    Connect any pin on pushbutton 1 to ground (GND).
    Connect the opposite diagonal pin of the pushbutton to
    digital pin 2.

    Connect any pin on pushbutton 2 to ground (GND).
    Connect the opposite diagonal pin of the pushbutton to
    digital pin 3.

    Also connect 10K resistors (brown/black/red) between
    digital pins 2 and 3 and GND. These are called "pullup"
    resistors. They ensure that the input pin will be either
    5V (unpushed) or GND (pushed), and not somewhere in between.
    (Remember that unlike analog inputs, digital inputs are only
    HIGH or LOW.)

  LED:
  
    Most Arduinos, including the Uno, already have an LED
    and resistor connected to pin 13, so you don't need any
    additional circuitry.

    But if you'd like to connect a second LED to pin 13,

    Connect the positive side of your LED to Arduino digital pin 13
    Connect the negative side of your LED to a 330 Ohm resistor
    Connect the other side of the resistor to ground

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/


// First we'll set up constants for the pin numbers.
// This will make it easier to follow the code below.

const int button1Pin = 2;  // pushbutton 1 pin
const int button2Pin = 3;  // pushbutton 2 pin
const int ledPin =  13;    // LED pin


void setup()
{
  // Set up the pushbutton pins to be an input:
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);

  // Set up the LED pin to be an output:
  pinMode(ledPin, OUTPUT);      
}


void loop()
{
  int button1State, button2State;  // variables to hold the pushbutton states

  // Since a pushbutton has only two states (pushed or not pushed),
  // we've run them into digital inputs. To read an input, we'll
  // use the digitalRead() function. This function takes one
  // parameter, the pin number, and returns either HIGH (5V)
  // or LOW (GND).

  // Here we'll read the current pushbutton states into
  // two variables:

  button1State = digitalRead(button1Pin);
  button2State = digitalRead(button2Pin);

  // Remember that if the button is being pressed, it will be
  // connected to GND. If the button is not being pressed,
  // the pullup resistor will connect it to 5 Volts.

  // So the state will be LOW when it is being pressed,
  // and HIGH when it is not being pressed.
  
  // Now we'll use those states to control the LED.
  // Here's what we want to do:
  
  // "If either button is being pressed, light up the LED"
  // "But, if BOTH buttons are being pressed, DON'T light up the LED"
  
  // Let's translate that into computer code. The Arduino gives you
  // special logic functions to deal with true/false logic:
  
  // A == B means "EQUIVALENT". This is true if both sides are the same.
  // A && B means "AND". This is true if both sides are true.
  // A || B means "OR". This is true if either side is true.
  // !A means "NOT". This makes anything after it the opposite (true or false).
  
  // We can use these operators to translate the above sentences
  // into logic statements (Remember that LOW means the button is
  // being pressed)
  
  // "If either button is being pressed, light up the LED"
  // becomes:
  // if ((button1State == LOW) || (button2State == LOW)) // light the LED
  
  // "If BOTH buttons are being pressed, DON'T light up the LED"
  // becomes:
  // if ((button1State == LOW) && (button2State == LOW)) // don't light the LED

  // Now let's use the above functions to combine them into one statement:
  
  if (((button1State == LOW) || (button2State == LOW))  // if we're pushing button 1 OR button 2
      && !                                               // AND we're NOT
      ((button1State == LOW) && (button2State == LOW))) // pushing button 1 AND button 2
                                                        // then...
  {
    digitalWrite(ledPin, HIGH);  // turn the LED on
  }
  else
  {
    digitalWrite(ledPin, LOW);  // turn the LED off
  }
     	
  // As you can see, logic operators can be combined to make
  // complex decisions!

  // Don't forget that we use = when we're assigning a value,
  // and use == when we're testing a value for equivalence.
}
```
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Code To Note</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">pinMode(button2Pin, INPUT);</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The digital pins can be used as inputs as well as outputs. Before you do either, you need to tell the Arduino which direction you’re going.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">button1State = digitalRead(button1Pin);</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
To read a digital input, you use the&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">digitalRead()</code>&nbsp;function. It will return HIGH if there’s 5V present at the pin, or LOW if there’s 0V present at the pin.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">if (button1State == LOW)</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Because we’ve connected the button to GND, it will read LOW when it’s being pressed. Here we’re using the “equivalence” operator (“==”) to see if the button is being pressed.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
What You Should See</h3>
<div style="background-color: white; box-sizing: border-box; margin-bottom: 10px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
You should see the LED turn on if you press either button, and off if you press both buttons. (See the code to find out why!) If it isn’t working, make sure you have assembled the circuit correctly and verified and uploaded the code to your board or see the troubleshooting section.</div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<div class="row" style="box-sizing: border-box; color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_05_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_05_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="box-sizing: border-box; color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The buttons we used here are similar to the buttons in most video game controllers.</div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Troubleshooting</h3>
<h4 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Light Not Turning On</h4>
<div style="box-sizing: border-box; color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The pushbutton is square, and because of this it is easy to put it in the wrong way. Give it a 90 degree twist and see if it starts working.</div>
<h4 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Underwhelmed</h4>
<div style="box-sizing: border-box; margin-bottom: 10px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
No worries, these circuits are all super stripped down to make playing with the components easy, but once you throw them together the sky is the limit.</div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Questions</h3>
<div>
<ol>
<li><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;">What is the purpose of pull up resistors?</span></span></li>
<li><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;">Describe the difference between the "=" operator and "==".</span></span></li>
</ol>
</div>
</div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<div style="text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;"><a href="http://www.davidriewe.com/p/experiment-4-driving-multiple-leds.html">Experiment 4: Driving Multiple LEDs</a>&nbsp;-|-&nbsp;<a href="http://www.davidriewe.com/p/experiment-6-reading-photoresistor.html">Experiment 6: Reading a Photoresistor</a></span></span></div>
</div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="font-size: xx-small;"><span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></span></h3>
<div>
<br /></div>
<div>
<h2 style="color: #666666; font-family: 'trebuchet ms', trebuchet, verdana, sans-serif; font-size: 22px; line-height: 20px; margin: 0px; position: relative; text-align: center;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our<br />
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
</div>
</div>
