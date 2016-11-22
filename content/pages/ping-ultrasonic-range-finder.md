Title: Ping Ultrasonic Range Finder
status: hidden

<div style="box-sizing: border-box; direction: ltr; margin-bottom: 1.5em; margin-left: auto; margin-right: auto; padding: 0px;">
Use an HC-SR04 ultrasonic sensor to give your project the ability to calculate distance. This popular ultrasonic distance sensor provides stable and accurate distance measurements from 2cm to 450cm. It has a focus of less than 15 degrees and an accuracy of about 2mm.<br />
<br />
Connect the VCC and GND pins to a 5V power supply, the trigger input (Trig) pin to a digital output and the echo (Echo) pin to a digital input to your microcontroller. Pulse the trigger (Trig) pin high for at least 10us (microseconds) and then wait for a high level on the echo (Echo) pin. The amount of time the Echo pin stays high corresponds to the distance that the ultrasonic sound has travelled. The quicker the response, the closer the object is.<br />
<br />
<h3>
<span style="font-size: large;">Hardware Required</span></h3>
</div>
<a href="http://www.amazon.com/gp/product/B00BT0NDB8/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=B00BT0NDB8&amp;linkCode=as2&amp;tag=davimakespa0e-20&amp;linkId=XFOHYOW4GUHCYPGW">Arduino </a>Board<br />
<a href="http://www.amazon.com/gp/product/B01COSN7O6/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=B01COSN7O6&amp;linkCode=as2&amp;tag=davimakespa0e-20&amp;linkId=GONDNRTZMYR2NYHC" rel="nofollow">HC-SR04 Ultrasonic Module</a>&nbsp;Ultrasonic Range Finder <br />
hook-up wires<br />
<br />
<h3>
<span style="font-size: large;">Circuit</span></h3>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
The <a href="http://www.amazon.com/gp/product/B01COSN7O6/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=B01COSN7O6&amp;linkCode=as2&amp;tag=davimakespa0e-20&amp;linkId=GONDNRTZMYR2NYHC" rel="nofollow">HC-SR04 Ultrasonic Module</a> has 4 pins, Ground, VCC, Trig and Echo. The Ground and the VCC pins of the module needs to be connected to the Ground and the 5 volts pins on the Arduino Board respectively and the trig and echo pins to any Digital I/O pin on the Arduino Board.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://4.bp.blogspot.com/-8qb6OmuivbM/Vv5zjlrtObI/AAAAAAAAs3k/cj9VMzJj70EpTHu55uxMpW5V9RU0iGKVg/s1600/Ultrasonic-Sensor-Cirucit-Schematics-04.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="243" src="https://4.bp.blogspot.com/-8qb6OmuivbM/Vv5zjlrtObI/AAAAAAAAs3k/cj9VMzJj70EpTHu55uxMpW5V9RU0iGKVg/s320/Ultrasonic-Sensor-Cirucit-Schematics-04.png" width="320" /></a></div>
<br />
<br />
<br />
<br />
click the image to enlarge<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br />
<span style="font-size: large;"> Code</span></div>
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<br /></div>
<div>
The sample below is using the <a href="http://playground.arduino.cc/Code/NewPing" rel="nofollow" target="_blank">NewPing library</a>. &nbsp;If you are using the Arduino IDE instead of codebender you will need to <a href="https://bitbucket.org/teckel12/arduino-new-ping/downloads" rel="nofollow" target="_blank">download the library here</a> and install it.<br />
<br />
In the example code below the Trig pin is connected to pin 12 and the Echo to pin 11. &nbsp;If your pins are connected to different Arduino pins then adjust the code accordingling.</div>
```
#include <NewPing.h>

#define TRIGGER_PIN  12
#define ECHO_PIN     11
#define MAX_DISTANCE 200

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

void setup()
{
	Serial.begin(115200);
}

void loop()
{
	delay(50);
	int uS = sonar.ping();
	Serial.print("Ping: ");
	Serial.print(uS / US_ROUNDTRIP_CM);
	Serial.println("cm");
}
```

<br />
<h2 style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 22px; margin: 0px; position: relative;">
<div style="text-align: center;">
<span style="font-size: large;">Want to save some time learning&nbsp;</span><span style="font-size: large;">Arduino?</span></div>
<span style="font-size: large;"><div style="text-align: center;">
Join the thousands of awesome people to sign up for our<br />
<a href="http://freecourse.hackerspacetech.com/" style="color: #888888; text-decoration: none;">FREE Arduino Video Crash Course!</a></div>
</span></h2>
