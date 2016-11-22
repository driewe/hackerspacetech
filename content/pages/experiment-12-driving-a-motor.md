Title: Experiment 12: Driving a Motor
status: hidden

<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; font-size: 14px; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></h3>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Introduction</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Back in experiment 8, you got to work with a servo motor. Now, we are going to tackle spinning a motor. This requires the use of a&nbsp;<a href="https://learn.sparkfun.com/tutorials/transistors" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;">transistor</a>, which can switch a larger amount of current than the RedBoard or Arduino Uno R3 can.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
When using a transistor, you just need to make sure its maximum specs are high enough for your use case. The transistor we are using for this circuit is rated at 40V max and 200 milliamps max – perfect for our toy motor! When the motor is spinning and suddenly turned off, the magnetic field inside it collapses, generating a voltage spike. This can damage the transistor. To prevent this, we use a “flyback diode”, which diverts the voltage spike around the transistor.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Parts Needed</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You will need the following parts:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Breadboard</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RedBoard or Arduino Uno</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Motor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;330Ω Resistor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;NPN transistor</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Diode 1N4148</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">6x</span>&nbsp;Jumper Wires</li>
</ul>
<div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Suggested Reading</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Before continuing on with this experiment, we recommend you be familiar with the concepts in the following tutorial:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><a href="https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;">Motors and Selecting the Right One</a></li>
<li style="box-sizing: border-box;"><a href="https://learn.sparkfun.com/tutorials/diodes" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;">Diodes</a></li>
<li style="box-sizing: border-box;"><a href="https://learn.sparkfun.com/tutorials/transistors" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;">Transistors</a></li>
</ul>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Hardware Hookup</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Ready to start hooking everything up? Check out the Fritzing diagram below, to see how everything is connected.</div>
<table class="table table-bordered" style="background-color: white; border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 640px;"><tbody style="box-sizing: border-box;">
<tr class="warning" style="box-sizing: border-box;"><td align="center" class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Polarized Components&nbsp;<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td align="left" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Pay special attention to the component’s markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction.</td></tr>
</tbody></table>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<span style="box-sizing: border-box; font-weight: 700;">Please note:</span>&nbsp;When you’re building the circuit be careful not to mix up the transistor and the temperature sensor, they’re almost identical. Look for “P2N2222A” on the body of the transistor.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Fritzing Diagram for RedBoard</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_12_01.png" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_12_01.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
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
Example sketch 12

SPINNING A MOTOR

  Use a transistor to spin a motor at different speeds.
  We'll also show you how to input data from the serial port
  (see the serialSpeed() function below).

  Motors are the basis for thousands of things in our daily lives,
  and the Arduino can control them. Here we'll use pulse-width
  modulation (PWM) to vary the speed of a motor.

  The Arduino pins are strong enough to light small LEDs (up to
  40 milliAmps), but they're not strong enough to run motors and
  other power-hungry parts. (This motor needs 50-100mA).
  Because the motor needs more current than an Arduino pin can
  provide, we'll use a transistor to do the heavy lifting.
  A transistor is a solid-state switch. When we give it a small
  amount of current, it can switch a much larger current.
  The transistors in your kit (2N2222) can switch up to 200mA.

  You can turn a transistor on and off using the digitalWrite()
  function, but you can also use the analogWrite() function to
  vary the speed of the motor. The analogWrite() function pulses
  a pin, varying the width of the pulse from 0% to 100%. We call
  this technique "PWM", for "Pulse-Width Modulation".

  One thing to keep in mind is that when you lower the speed of
  a motor using PWM, you're also reducing the torque (strength)
  of the motor. For PWM values below 50 or so, the motor won't have
  enough torque to start spinning. It will start spinning when you
  raise the speed a bit.

Hardware connections:

  Transistor:
  
    The transistor has three pins. Looking at the flat side with the
    pins down, the order is COLLECTOR, BASE, EMITTER.
    
    Connect the black wire on the motor to the
    COLLECTOR pin on the transistor.

    Connect the BASE pin through a 330 Ohm resistor to
    digital pin 9.
    
    Connect the EMITTER pin to GND.
 
  Motor:

    You've already connected the black wire on the motor to the
    COLLECTOR pin on the transistor.
    
    Connect the other (red) wire on the motor to 5V.
  
  Flyback diode:

    When the motor is spinning and suddenly turned off, the
    magnetic field inside it collapses, generating a voltage spike.
    This can damage the transistor. To prevent this, we use a
    "flyback diode", which diverts the voltage spike "around" the
    transistor.

    Connect the side of the diode with the band (cathode) to 5V
    Connect the other side of the diode (anode) to the black wire
    on the motor.

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/

// We'll be controlling the motor from pin 9.
// This must be one of the PWM-capable pins.

const int motorPin = 9;


void setup()
{
  // Set up the motor pin to be an output:

  pinMode(motorPin, OUTPUT);

  // Set up the serial port:

  Serial.begin(9600);
}


void loop()
{
  // Here we've used comments to disable some of the examples.
  // To try different things, uncomment one of the following lines
  // and comment the other ones. See the functions below to learn
  // what they do and how they work.

  // motorOnThenOff();
  // motorOnThenOffWithSpeed();
  // motorAcceleration();
     serialSpeed();
}


// This function turns the motor on and off like the blinking LED.
// Try different values to affect the timing.

void motorOnThenOff()
{
  int onTime = 3000;  // milliseconds to turn the motor on
  int offTime = 3000; // milliseconds to turn the motor off
  
  digitalWrite(motorPin, HIGH); // turn the motor on (full speed)
  delay(onTime);                // delay for onTime milliseconds
  digitalWrite(motorPin, LOW);  // turn the motor off
  delay(offTime);               // delay for offTime milliseconds
}


// This function alternates between two speeds.
// Try different values to affect the timing and speed.

void motorOnThenOffWithSpeed()
{
  int Speed1 = 200;  // between 0 (stopped) and 255 (full speed)
  int Time1 = 3000;  // milliseconds for speed 1
  
  int Speed2 = 50;   // between 0 (stopped) and 255 (full speed)
  int Time2 = 3000;  // milliseconds to turn the motor off
  
  analogWrite(motorPin, Speed1);  // turns the motor On
  delay(Time1);                   // delay for onTime milliseconds
  analogWrite(motorPin, Speed2);  // turns the motor Off
  delay(Time2);                   // delay for offTime milliseconds
}


// This function slowly accelerates the motor to full speed,
// then back down to zero.

void motorAcceleration()
{
  int speed;
  int delayTime = 20; // milliseconds between each speed step
  
  // accelerate the motor

  for(speed = 0; speed <= 255; speed++)
  {
    analogWrite(motorPin,speed);	// set the new speed
    delay(delayTime);           	// delay between speed steps
  }
  
  // decelerate the motor

  for(speed = 255; speed >= 0; speed--)
  {
    analogWrite(motorPin,speed);	// set the new speed
    delay(delayTime);           	// delay between speed steps
  }
}


// This function will let you type a speed into the serial
// monitor window. Open the serial monitor using the magnifying-
// glass icon at the top right of the Arduino window. Then
// type your desired speed into the small text entry bar at the
// top of the window and click "Send" or press return. The motor
// will then operate at that speed. The valid range is 0 to 255.

void serialSpeed()
{
  int speed;
  
  Serial.println("Type a speed (0-255) into the box above,");
  Serial.println("then click [send] or press [return]");
  Serial.println();  // Print a blank line

  // In order to type out the above message only once,
  // we'll run the rest of this function in an infinite loop:

  while(true)  // "true" is always true, so this will loop forever.
  {
    // First we check to see if incoming data is available:
  
    while (Serial.available() > 0)
    {
      // If it is, we'll use parseInt() to pull out any numbers:
      
      speed = Serial.parseInt();
  
      // Because analogWrite() only works with numbers from
      // 0 to 255, we'll be sure the input is in that range:
  
      speed = constrain(speed, 0, 255);
      
      // We'll print out a message to let you know that the
      // number was received:
      
      Serial.print("Setting speed to ");
      Serial.println(speed);
  
      // And finally, we'll set the speed of the motor!
      
      analogWrite(motorPin, speed);
    }
  }
}
```
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Code To Note</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">while (Serial.available() &gt; 0)</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The Arduino’s serial port can be used to receive as well as send data. Because data could arrive at any time, the Arduino stores, or “buffers” data coming into the port until you’re ready to use it. The&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">Serial.available()</code>&nbsp;command returns the number of characters that the port has received, but haven’t been used by your sketch yet. Zero means no data has arrived.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">speed = Serial.parseInt();</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
If the port has data waiting for you, there are a number of ways for you to use it. Since we’re typing numbers into the port, we can use the handy&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">Serial.parseInt()</code>&nbsp;command to extract, or “parse” integer numbers from the characters it’s received. If you type “1” “0” “0” to the port, this function will return the number 100.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
What You Should See</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
The DC Motor should spin if you have assembled the circuit’s components correctly, and also verified/uploaded the correct code. If your circuit is not working check the troubleshooting section.</div>
<div class="row" style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_12_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_12_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Radio Controlled (RC) cars use&nbsp;<a href="https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc" rel="nofollow" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;" target="_blank">Direct Current</a>&nbsp;(DC) motors to turn the wheels for propulsion.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Troubleshooting</h3>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Motor Not Spinning</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
If you sourced your own transistor, double check with the data sheet that the pinout is compatible with a P2N2222AG (many are reversed).</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Still No Luck</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
If you sourced your own motor, double check that it will work with 5 volts and that it does not draw too much power.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Still Not Working</h4>
<div style="background-color: white; box-sizing: border-box; margin-bottom: 10px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
Sometimes the Arduino will disconnect from the computer. Try un-plugging and then re-plugging it into your USB port.</div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<div style="text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;"><a href="http://www.davidriewe.com/p/experiment-11-using-piezo-buzzer.html">Experiment 11: Using a Piezo Buzzer</a>&nbsp;-|-&nbsp;<a href="http://www.davidriewe.com/p/experiment-13-using-relays.html">Experiment 13: Using Relays</a></span></span></div>
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
