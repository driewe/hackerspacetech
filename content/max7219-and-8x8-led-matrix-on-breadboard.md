Title: MAX7219 and 8x8 LED Matrix on breadboard
Date: 2015-11-20 15:54
Category: Blog
Tags: Arduino, 7219, Matrix, breadboard, tutorials
Author: David Riewe

![IMAGE ALT TEXT HERE](http://4.bp.blogspot.com/-KKnWSdjT4GI/Vk8_9tMGYLI/AAAAAAAArCw/miuvVO_DER0/s320/20151120_093852.jpg)

I popped the MAX7219 and 8x8 LED Matrix from the kit and made it a little more social (watch video to see what I mean).  Using the MAX7219 requires only 3 pins from the arduino, a couple capacitors and resistor.  All the multiplexing is handled by the chip.  When writing to the device you shift out two bytes, one is the operand the second is the actual segment data. The library hides that from you so you can simply turn on and off individual leds, rows or columns.

See my prior post,[MAX7219 8X8 Red Dot LED Matrix Kit ](/max7219-8x8-red-dot-led-matrix-kit.html),
  for more details




<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/IbC_7qqGBfY" width="560"></iframe></div>