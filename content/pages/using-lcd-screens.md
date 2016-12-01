Title: Using LCD Screens

<div class="jumbotron">
<div class="container-fluid">

<div class="tr_bq">
<span style="color: red;">**&nbsp;</span><a href="http://www.meetup.com/TechmillDenton/" rel="nofollow" style="text-align: center;" target="_blank">Visit Our Meetup Page To Register For Free Workshop</a><span style="color: red;">&nbsp;**</span><br />
<br />
<span style="font-size: x-large;"><a href="http://txplore.tv/courses/arduino-sbs/lectures/276195?affcode=6107_xiz8dp9c" rel="nofollow" target="_blank">LCD character screen</a></span></div>
<blockquote class="tr_bq">
This 2-part presentation will show you how to connect and use and LCD character screen. In part 1, I'll show you how to wire up the screen and display a message on it. And in part 2, we'll connect a sensor and display its readings to the screen.</blockquote>
<b>Parts</b><br />
<blockquote class="tr_bq">
An LCD screen. See External Resources for an example from eBay. No need for a shield unless you really want to. Also, best NOT to buy an 2x8 screen since those come with their pins arranged in two rows which makes it a big pain to connect to your Arduino. When pins are arranged in two rows, you can't use a breadboard as is, you will need to make an adaptor. Avoid!</blockquote>
<ul>
<li>The DHT22 or DHT11 sensor.</li>
<li>A potentiometer.</li>
</ul>
<b>View external resources</b><br />
<br />
<ul>
<li><a href="https://github.com/futureshocked/arduino_sbs/blob/master/LCD%20Character/LCD_Demo_1/LCD_Demo_1.ino">LCD Demo Sketch 1</a></li>
<li><a href="https://github.com/futureshocked/arduino_sbs/blob/master/LCD%20Character/LCD_Demo_2/LCD_Demo_2.ino">LCD Demo Sketch 2</a></li>
<li><a href="http://arduino.cc/en/Tutorial/LiquidCrystal">LCD library documentation</a></li>
<li><a href="https://txplore-downloads.s3.amazonaws.com/LiquidCrystal.zip">LCD Library ZIP file, the same library I use in the Demo</a></li>
</ul>
<br />
<span style="font-size: x-large;"><a href="http://txplore.tv/courses/arduino-sbs/lectures/276197?affcode=6107_xiz8dp9c" rel="nofollow" target="_blank">Single data wire LCD and I2C</a></span><br />
<blockquote>
In the LCD Presentation, you learned how to display text in a LCD screen. Although this was a simple way to show useful information to the user, the sheer number of wires required to make the LCD screen work makes this solution far from elegant.</blockquote>
<blockquote>
In this presentaion, I will show you a much improved solution to the same problem, one that involves a single data wire (plus power).</blockquote>
<blockquote>
To achieve this reduction in total number of wires we have to switch the type of interface we use to connect the screen to the Arduino. Natively, the screen uses a parallel interface, where each of the 8 bits that make up a character encoding uses up a wire. You may remember that in Presentation 24, use used a 4-bit parallel mode instead of the full 8-bits in order to save 4 wires. Still, even 4 wires are too many for transferring data. We also needed wires for power, and for the screen backlit.</blockquote>
<blockquote>
To improve the design, we'll use an adaptor that allows us to connect the parallel LCD screen to the Arduino using the I2C serial bus.</blockquote>
<blockquote>
The adapter I'll use in the demos is the 1602LCD Display I2C board.</blockquote>
<blockquote>
In this part 1, I'll show you how to connect the LCD adaptor to the screen and to the Arduino, and make sure it works.</blockquote>
<blockquote>
In Part 2, I'll show you how to connect a second I2C device to the circuit from Demo 1 (in Part 1 of this presentation). The second device is a real-time clock.</blockquote>
<br />
<b>Parts</b><br />
<br />
<ul>
<li>An Arduino Uno</li>
<li>A 16x2 LCD screen (see External Resources for an example).</li>
<li>A 1602LCD Display I2C board (see External Resources for an example).</li>
<li>A few jumper wires, including one 4-pin jumper (Dupont) cable for the adapter (see External Resources for an example).</li>
</ul>
<div>
<b>View external resources</b><br />
<ul>
<li><a href="https://txplore-downloads.s3.amazonaws.com/LiquidCrystal.zip">Download the LCD library</a></li>
<li><a href="https://github.com/futureshocked/arduino_sbs/blob/master/LCD%20Single%20Wire/LCD_Single_wire_Demo_1/LCD_Single_wire_Demo_1.ino">LCD single wire Demo 1</a></li>
<li><a href="https://github.com/futureshocked/arduino_sbs/blob/master/LCD%20Single%20Wire/LCD_Single_wire_Demo_2/LCD_Single_wire_Demo_2.ino">LCD single wire Demo 2</a></li>
<li><a href="http://www.ebay.com.au/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xarduino+16x2+lcd&amp;_nkw=arduino+16x2+lcd&amp;_sacat=0&amp;_from=R40">An LCD character screen, 16x2</a></li>
<li><a href="http://www.ebay.com.au/sch/i.html?_trksid=p2047675.m570.l1313.TR0.TRC0.H0.X1602LCD+Display+IIC%2FI2C%2FTWI%2FSP%E2%80%8B%E2%80%8BI&amp;_nkw=1602LCD+Display+IIC%2FI2C%2FTWI%2FSP%E2%80%8B%E2%80%8BI&amp;_sacat=0&amp;_from=R40">A 1602LCD Display I2C board</a></li>
<li><a href="http://www.ebay.com.au/sch/i.html?_trksid=p3984.m570.l1313.TR0.TRC0.H0.XCable+Jumper+4P-4x1P+F-F%28Female%29+2.54mm+30cm&amp;_nkw=Cable+Jumper+4P-4x1P+F-F%28Female%29+2.54mm+30cm&amp;_sacat=0&amp;_from=R40">A 4-pin jumper (Dupont) cable for the adaptor.</a></li>
<li><a href="http://arduino.cc/en/reference/wire">I2C reference documentation</a></li>
<li><a href="https://bitbucket.org/fmalpartida/new-liquidcrystal/src">I2C library</a></li>
</ul>
</div>
</div></div>
