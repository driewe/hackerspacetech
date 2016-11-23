Title: Experiment 10: Reading a Soft Potentiometer
status: hidden

<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; font-size: 14px; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></h3>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Introduction</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
In this circuit, we are going to use yet another kind of variable resistor – this time, a soft potentiometer (or soft pot). This is a thin and flexible strip that can detect where pressure is being applied. By pressing down on various parts of the strip, you can vary the resistance from 100 to 10k ohms. You can use this ability to track movement on the soft pot, or simply as a button. In this circuit, we’ll get the soft pot up and running to control an RGB LED.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Parts Needed</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You will need the following parts:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Breadboard</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RedBoard or Arduino Uno</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Soft Potentiometer</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;10k resistor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">3x</span>&nbsp;330Ω resistors</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RGB LED</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">9x</span>&nbsp;Jumper Wires</li>
</ul>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Hardware Hookup</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Ready to start hooking everything up? Check out the Fritzing diagram below, to see how everything is connected.</div>
<table class="table table-bordered" style="background-color: white; border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 640px;"><tbody style="box-sizing: border-box;">
<tr class="warning" style="box-sizing: border-box;"><td align="center" class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Polarized Components&nbsp;<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td align="left" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Pay special attention to the component’s markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction.</td></tr>
</tbody></table>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Fritzing Diagram for RedBoard</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_10_02-01.png" style="background: 0px 0px; box-sizing: border-box; color: #9c2214; outline: 0px; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_10_02-01.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<em style="box-sizing: border-box;">Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.</em><br />
<div style="text-align: left;">
<em style="box-sizing: border-box;"></em></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: start;">
Open the Sketch</h3>
<div style="text-align: left;">
<br /></div>
</div>
</div>
</div>
```
/*
SparkFun Inventor's Kit
Example sketch 10

SOFT POTENTIOMETER

  Use the soft potentiometer to change the color
  of the RGB LED

  The soft potentiometer is a neat input device that detects 
  pressure along its length. When you press it down with a finger
  (it works best on a flat surface), it will change resistance
  depending on where you're pressing it. You might use it to make
  a piano or light dimmer; here we're going to use it to control
  the color of an RGB LED.
  
Hardware connections:

  Soft potentiometer:

    The soft potentiometer is the large plastic strip with three
    pins. We'll be connecting it as a voltage divider, just like
    we did with the knob-type potentiometer back in circuit #2.

    Connect the middle pin to ANALOG IN pin 0 on the Arduino.
    Connect one side to 5V.
    Connect the other side to GND.
    Also connect a 10K resistor from the middle pin to GND.

    TIP: the soft pot will only work while you're actively
    pressing on it; at other times it will "float" to random
    values. To prevent this, we've added a 10K pull-down resistor
    to the middle pin (output voltage). This will keep the output
    at zero volts when the pot is not being pressed.

  RGB LED:

    An RGB LED is actually three LEDs (red, green, and blue)
    in one package. When we run them at different brightnesses,
    they mix to form new colors.
    
    Starting at the flattened edge of the flange on the LED,
    the pins are ordered RED, COMMON, GREEN, BLUE.
    
    Connect RED to a 330 Ohm resistor.
    Connect the other end of the resistor to Arduino digital pin 9.
  
    Connect COMMON to GND.
  
    Connect GREEN through a 330 Ohm resistor.
    Connect the other end of the resistor to Arduino digital pin 10.
  
    Connect BLUE through a 330 Ohm resistor.
    Connect the other end of the resistor to Arduino digital pin 11.

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/


// Constants for LED connections (note that these must be
// PWM pins, which are marked with "PWM" or have a "~" symbol
// next to them on the board).

const int RED_LED_PIN = 9;    // Red LED Pin
const int GREEN_LED_PIN = 10; // Green LED Pin
const int BLUE_LED_PIN = 11;  // Blue LED Pin

const int SENSOR_PIN = 0;      // Analog input pin

// Global PWM brightness values for the RGB LED.
// These are global so both loop() and setRGB() can see them.

int redValue, greenValue, blueValue;


void setup()
{
  // No need for any code here
  // analogWrite() sets up the pins as outputs
}


void loop()
{
  int sensorValue;

  // Read the voltage from the softpot (0-1023)
  
  sensorValue = analogRead(0);

  // We've written a new function called setRGB() (further down
  // in the sketch) that decodes sensorValue into a position
  // on the RGB "rainbow", and sets the RGB LED to that color.
 
  setRGB(sensorValue);
}


// setRGB()
// Set a RGB LED to a position on the "rainbow" of all colors.
// RGBposition should be in the range of 0 to 1023 (such as
// from an analog input).

void setRGB(int RGBposition)
{
  int mapRGB1, mapRGB2, constrained1, constrained2;
  
  // Here we take RGBposition and turn it into three RGB values.

  // The three values are computed so that the colors mix and 
  // produce a rainbow of colors across the 0-1023 input range.
  
  // For each channel (red green blue), we're creating a "peak"
  // a third of the way along the 0-1023 range. By overlapping
  // these peaks with each other, the colors are mixed together.
  // This is most easily shown with a diagram:
  // http://sfecdn.s3.amazonaws.com/education/SIK/SchematicImages/Misc/RGB_function.jpg
  
  // Create the red peak, which is centered at 0.
  // (Because it's centered at 0, half is after 0, and half
  // is before 1023):

  mapRGB1 = map(RGBposition, 0, 341, 255, 0);
  constrained1 = constrain(mapRGB1, 0, 255);

  mapRGB2 = map(RGBposition, 682, 1023, 0, 255);
  constrained2 = constrain(mapRGB2, 0, 255);

  redValue = constrained1 + constrained2;

  // Create the green peak, which is centered at 341
  // (one-third of the way to 1023):

  // Note that we've nested the functions by putting the map()
  // function inside the constrain() function. This can make your
  // code more compact, and requires fewer variabls:
  
  greenValue = constrain(map(RGBposition, 0, 341, 0, 255), 0, 255)
             - constrain(map(RGBposition, 341, 682, 0,255), 0, 255);

  // Create the blue peak, which is centered at 682
  // (two-thirds of the way to 1023):
              
  blueValue = constrain(map(RGBposition, 341, 682, 0, 255), 0, 255)
            - constrain(map(RGBposition, 682, 1023, 0, 255), 0, 255);

  // Now we have all three brightnesses,
  // we just need to display the computed color:

  analogWrite(RED_LED_PIN, redValue);
  analogWrite(GREEN_LED_PIN, greenValue);
  analogWrite(BLUE_LED_PIN, blueValue);

  // Feel free to use this function in your own code!
}
```
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Code To Note</h3>
<pre data-language="language:cpp
,cpp
" style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(204, 204, 204); box-sizing: border-box; color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 13px; line-height: 19px; margin-bottom: 20px; max-height: 350px; overflow: auto; padding: 6px 10px; word-break: break-all; word-wrap: break-word;"><div class="copy-code" data-code-id="code-1" style="box-sizing: border-box; float: right;">
<button class="btn btn-default btn-sm" style="-webkit-user-select: none; background-color: white; background-image: none; border-radius: 3px; border: 1px solid rgb(204, 204, 204); color: #e0311d; cursor: pointer; font-family: SparkGauge, 'Arial Narrow', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; font-stretch: inherit; font-style: inherit; font-variant: inherit; font-weight: 700; letter-spacing: 0.1em; line-height: 1.5; margin: 0px; overflow: visible; padding: 5px 10px; text-transform: uppercase; vertical-align: middle; white-space: nowrap;">COPY CODE</button></div>
<code class="rainbow" style="background: transparent; border-radius: 0px; border: 0px; box-sizing: border-box; color: inherit; font-family: Consolas, 'Liberation Mono', Courier, monospace; margin: 0px; padding: 0px; white-space: pre-wrap;">redValue <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">=</span> <span class="function call" style="box-sizing: border-box;">constrain</span>(<span class="function call" style="box-sizing: border-box;">map</span>(RGBposition, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">341</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>), <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>)
 <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">+</span> <span class="function call" style="box-sizing: border-box;">constrain</span>(<span class="function call" style="box-sizing: border-box;">map</span>(RGBposition, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">682</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">1023</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>), <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>);


greenValue <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">=</span> <span class="function call" style="box-sizing: border-box;">constrain</span>(<span class="function call" style="box-sizing: border-box;">map</span>(RGBposition, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">341</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>), <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>)
 <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">-</span> <span class="function call" style="box-sizing: border-box;">constrain</span>(<span class="function call" style="box-sizing: border-box;">map</span>(RGBposition, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">341</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">682</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>,<span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>), <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>);


blueValue <span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">=</span> <span class="function call" style="box-sizing: border-box;">constrain</span>(<span class="function call" style="box-sizing: border-box;">map</span>(RGBposition, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">341</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">682</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>), <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>)
<span class="keyword operator" style="box-sizing: border-box; font-weight: bold;">-</span> <span class="function call" style="box-sizing: border-box;">constrain</span>(<span class="function call" style="box-sizing: border-box;">map</span>(RGBposition, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">682</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">1023</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>), <span class="constant numeric" style="box-sizing: border-box; color: #009999;">0</span>, <span class="constant numeric" style="box-sizing: border-box; color: #009999;">255</span>);
</code></pre>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
These big, scary functions take a single Value (RGBposition) and calculate the three RGB values necessary to create a rainbow of color. The functions create three “peaks” for the red, green, and blue values, which overlap to mix and create new colors. See the code for more information! Even if you’re not 100% clear how it works, you can copy and paste this (or any) function into your own code and use it yourself.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
What You Should See</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You should see the RGB LED change colors in accordance with how you interact with the soft potentiometer. If it isn’t working, make sure you have assembled the circuit correctly and verified and uploaded the code to your board, or see the troubleshooting section.</div>
<div class="row" style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_10_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_10_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The knobs found on many objects, like a radio for instance, are using similar concepts to the one you just completed for this circuit.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Troubleshooting</h3>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
LED Remains Dark or Shows Incorrect Color</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
With the four pins of the LED so close together, it’s sometimes easy to misplace one. Try double checking each pin is where it should be.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Bizarre Results</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The most likely cause of this is if you’re pressing the potentiometer in more than one position. This is normal and can actually be used to create some neat results.</div>
<div style="background-color: white; box-sizing: border-box; margin-bottom: 10px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<div style="text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;"><a href="/pages/experiment-9-using-a-flex-sensor.html">Experiment 9: Using a Flex Sensor</a>&nbsp;-|-&nbsp;<a href="/pages/experiment-11-using-a-piezo-buzzer.html">Experiment 11: Using a Piezo Buzzer</a></span></span></div>
</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; font-size: 14px; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></h3>
<div>
<br /></div>
<div>
<h2 style="background-color: white; color: #666666; font-family: 'trebuchet ms', trebuchet, verdana, sans-serif; font-size: 22px; line-height: 20px; margin: 0px; position: relative; text-align: center;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our<br />
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
</div>
