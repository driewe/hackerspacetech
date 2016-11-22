Title: 8x16 LED matrix controlled by 2 MAX7219's
Date: 2015-11-21 20:49
Category: Blog
Tags: Arduino, LED, Projects
Author: David Riewe


![8x8 LED Matrix](/images/ledmatrix.jpg)

Expanding on my experiment with the MAX7219 controlling an 8x8 LED Matrix I added a second one. Both of the 8x8 displays and controllers were part of kits that couldn't fit neatly side by side, but the concept can still be demonstrated.

Using the circuit layout of the [MAX7219 8X8 Red Dot LED Matrix Kit](http://www.davidriewe.com/2015/11/max7219-8x8-red-dot-led-matrix-kit.html) proved cumbersome as it didn't provide enough room to get the 8x8 LED panels
close together and when you add additional devices the library expects
to see them to the left of the previous device.  No big deal for
testing. I would like to wire up a board that all three could neatly
mount on and present a nice 8x24 display.

Here is a video of the 8x16 display created by cascading two of the
MAX7219 controllers together.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ibbhZqjT-AY" frameborder="0" allowfullscreen></iframe>
