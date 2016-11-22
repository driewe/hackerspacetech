Title: Infra Red Remote Controller Shield
Date: 2015-11-28
Category: Blog
Tags: Arduino, InfraRed, Shield
Author: David Riewe

![IR Shielld](/images/irshield.jpg)

Made use of The Forge makerspace at North Branch library to construct my first Arduino Shield. This shield adds 7 Status LEDs, an Infra Red LED, an Infra Red Receiver and a piezo buzzer.

Signal processing is handled by a great [Arduino library](https://github.com/shirriff/Arduino-IRremote) written by Ken Shirriff and allows you to easily send and receive IR data. In order to use the tone function I had to change which Timer the Infra Red Remote Library uses so it would not conflict. Other than that, the Infra Red Remote Library works very well. In the video below I test the shield using a sketch that plays a different tone for various buttons pressed on an old clarion remote control I found lying around.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2N15Wiu5OVM" frameborder="0" allowfullscreen></iframe>

###Applications
###Ken Shirrif used this library for several applications:

-  Controlling a [pedestrian sign](http://arcfn.com/2010/01/dont-walk-controlling-pedestrian-sign.html) with a remote.
-  Extend the library to [arbitrary remotes](http://arcfn.com/2010/01/using-arbitrary-remotes-with-arduino.html).
-  [Controlling my stereo](http://arcfn.com/2009/11/controlling-your-stereo-over-web-with.html) over the web.
-  To implement a ["Universal remote"](http://arcfn.com/2009/09/arduino-universal-remote-record-and.html) to record and playback IR codes.
-  Demonstrates turning something on and off via remote in
   his [infrared bubble maker](http://arcfn.com/2009/11/ir-bubbles-controlling-relay-with.html) project.
-  [Using the library to detect IR beam breaks](http://www.arcfn.com/2010/03/detecting-ir-beam-break-with-arduino-ir.html)

###Other projects that use this library

-  [electrosthetics](http://electrosthetics.blogspot.com/2009/11/arduino-universal-remote-and-more.html) used the library to control a home theater receiver.
-  [Arduino: Redefining the TV Remote](http://luckylarry.co.uk/2010/06/arduino-redefining-the-tv-remote/) - using the library and an ultrasonic sensor to control a TV by
   waving your hand
-  I used it to [control a Parallax Adruino based rover remotely](/infra-red-controlled-robot.html)