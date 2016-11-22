Title: Experiment 9: Using a Flex Sensor
status: hidden

<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; font-size: 14px; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></h3>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Introduction</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
In this circuit, we will use a flex sensor to measure, well, flex! A flex sensor uses carbon on a strip of plastic to act like a variable resistor, but instead of changing the resistance by turning a knob, you change it by flexing (bending) the component. We use a “voltage divider” again to detect this change in resistance.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The sensor bends in one direction and the more it bends, the higher the resistance gets; it has a range from about 10K ohm to 35K ohm. In this circuit we will use the amount of bend of the flex sensor to control the position of a servo.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Parts Needed</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You will need the following parts:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Breadboard</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RedBoard or Arduino Uno</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Flex Sensor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Servo</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;10k resistor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">11x</span>&nbsp;Jumper Wires</li>
</ul>
<div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Suggested Reading</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Before continuing on with this experiment, we recommend you be familiar with the concepts in the following tutorial:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><a href="https://learn.sparkfun.com/tutorials/voltage-dividers" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;" target="_blank">Voltage Dividers</a></li>
</ul>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Hardware Hookup</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Ready to start hooking everything up? Check out the Fritzing diagram below, to see how everything is connected.</div>
<table class="table table-bordered" style="background-color: white; border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 640px;"><tbody style="box-sizing: border-box;">
<tr class="warning" style="box-sizing: border-box;"><td align="center" class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Polarized Components&nbsp;<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td align="left" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Pay special attention to the component’s markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction.</td></tr>
</tbody></table>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Connect 3x jumper wires to the female 3 pin header on the servo. This will make it easier to breadboard the servo.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Fritzing Diagram for RedBoard</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_09_02-01.png" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_09_02-01.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<em style="box-sizing: border-box;">Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.</em><br />
<div style="text-align: left;">
<em style="box-sizing: border-box;"></em></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: start;">
Run the Sketch</h3>
<div style="text-align: left;">
<br /></div>
</div>
</div>
</div>
```
/*
SparkFun Inventor's Kit
Example sketch 09

FLEX SENSOR

  Use the "flex sensor" to change the position of a servo
  
  In the previous sketch, we learned how to command a servo to
  mode to different positions. In this sketch, we'll introduce
  a new sensor, and use it to control the servo.
  
  A flex sensor is a plastic strip with a conductive coating.
  When the strip is straight, the coating will be a certain
  resistance. When the strip is bent, the particles in the coating
  get further apart, increasing the resistance. You can use this
  sensor to sense finger movement in gloves, door hinges, stuffed
  animals, etc. See http://www.sparkfun.com/tutorials/270 for
  more information.
  
Hardware connections:

  Flex sensor:

    The flex sensor is the plastic strip with black stripes.
    It senses bending away from the striped side.
    
    The flex sensor has two pins, and since it's a resistor,
    the pins are interchangable.
    
    Connect one of the pins to ANALOG IN pin 0 on the Arduino.
    Connect the same pin, through a 10K Ohm resistor (brown
    black orange) to GND.
    Connect the other pin to 5V.

  Servo:
  
    The servo has a cable attached to it with three wires.
    Because the cable ends in a socket, you can use jumper wires
    to connect between the Arduino and the servo. Just plug the
    jumper wires directly into the socket.
    
    Connect the RED wire (power) to 5 Volts (5V)
    Connect the WHITE wire (signal) to digital pin 9
    Connect the BLACK wire (ground) to ground (GND)
  
    Note that servos can use a lot of power, which can cause your
    Arduino to reset or behave erratically. If you're using large
    servos or many of them, it's best to provide them with their
    own separate 5V supply. See this Arduino Forum thread for info:
    http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1239464763

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/


// Include the servo library to add servo-control functions:

#include <Servo.h> 

// Create a servo "object", called servo1. Each servo object
// controls one servo (you can have a maximum of 12):

Servo servo1;

// Define the analog input pin to measure flex sensor position:

const int flexpin = 0; 


void setup() 
{ 
  // Use the serial monitor window to help debug our sketch:
   
  Serial.begin(9600);
  
  // Enable control of a servo on pin 9:

  servo1.attach(9);
} 


void loop() 
{ 
  int flexposition;    // Input value from the analog pin.
  int servoposition;   // Output value to the servo.

  // Read the position of the flex sensor (0 to 1023):
  
  flexposition = analogRead(flexpin);

  // Because the voltage divider circuit only returns a portion
  // of the 0-1023 range of analogRead(), we'll map() that range
  // to the servo's range of 0 to 180 degrees. The flex sensors
  // we use are usually in the 600-900 range:
  
  servoposition = map(flexposition, 600, 900, 0, 180);
  servoposition = constrain(servoposition, 0, 180);

  // Now we'll command the servo to move to that position:

  servo1.write(servoposition);

  // Because every flex sensor has a slightly different resistance,
  // the 600-900 range may not exactly cover the flex sensor's
  // output. To help tune our program, we'll use the serial port to
  // print out our values to the serial monitor window:
  
  Serial.print("sensor: ");
  Serial.print(flexposition);
  Serial.print("  servo: ");
  Serial.println(servoposition);
  
  // Note that all of the above lines are "print" except for the
  // last line which is "println". This puts everything on the
  // same line, then sends a final carriage return to move to
  // the next line.

  // After you upload the sketch, turn on the serial monitor
  // (the magnifying-glass icon to the right of the icon bar).
  // You'll be able to see the sensor values. Bend the flex sensor
  // and note its minimum and maximum values. If you replace the
  // 600 and 900 in the map() function above, you'll exactly match
  // the flex sensor's range with the servo's range.
  
  delay(20);  // wait 20ms between servo updates
} 
```
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Code To Note</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">servoposition = map(flexposition, 600, 900, 0, 180);</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
map(value, fromLow, fromHigh, toLow, toHigh)</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Because the flex sensor / resistor combination won’t give us a full 0 to 5 volt range, we’re using the&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">map()</code>&nbsp;function as a handy way to reduce that range. Here we’ve told it to only expect values from 600 to 900, rather than 0 to 1023.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">servoposition = constrain(servoposition, 0, 180);</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
constrain(x, a, b)</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Because&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">map()</code>&nbsp;could still return numbers outside the “to” range, we’ll also use a function called&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">constrain()</code>&nbsp;that will “clip” numbers into a range. If the number is outside the range, it will make it the largest or smallest number. If it is within the range, it will stay the same.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
What You Should See</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You should see the servo motor move in accordance with how much you are flexing the flex sensor. If it isn’t working, make sure you have assembled the circuit correctly and verified and uploaded the code to your board or see the troubleshooting section.</div>
<div class="row" style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_09_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_09_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Controller accessories for video game consoles like Nintendo’s “Power Glove” use flex-sensing technology. It was the first video game controller attempting to mimic hand movement on a screen in real time.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Troublshooting</h3>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Servo Not Twisting</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Even with colored wires it is still shockingly easy to plug a servo in backwards. This might be the case.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Servo Not Moving as Expected</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The sensor is only designed to work in one direction. Try flexing it the other way (where the striped side faces out on a convex curve).</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Servo Doesn’t Move very Far</h4>
<div style="background-color: white; box-sizing: border-box; margin-bottom: 10px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
You need to modify the range of values in the call to the&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">map()</code>&nbsp;function.</div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<div style="text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;"><a href="http://www.davidriewe.com/p/experiment-8-driving-servo-motor.html">**Experiment 8: Driving a Servo Motor**</a>&nbsp;-|-&nbsp;<a href="http://www.davidriewe.com/p/experiment-10-reading-soft-potentiometer.html">Experiment 10: Reading a Soft Potentiometer</a></span></span></div>
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
