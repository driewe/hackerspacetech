Title: Wifi connectivity - using CC3000

<div class="jumbotron">
<div class="container-fluid">
<h2 class="section-title" data-lecture-id="276240" data-lecture-url="/courses/arduino-sbs/lectures/276240" data-next-lecture-id="276241" data-next-lecture-url="/courses/arduino-sbs/lectures/276241" data-previous-lecture-id="276238" data-previous-lecture-url="/courses/arduino-sbs/lectures/276238" id="lecture_heading" style="box-sizing: border-box; color: #333333; font-family: proxima; font-size: 31px; line-height: 41px; margin-bottom: 18px; margin-top: 10px; text-align: center;">
<span style="color: red; font-family: 'Times New Roman'; font-size: small; font-weight: normal; line-height: normal;">**&nbsp;</span><a href="http://www.meetup.com/TechmillDenton/" rel="nofollow" style="font-family: 'Times New Roman'; font-size: medium; font-weight: normal; line-height: normal; text-align: center;" target="_blank">Visit Our Meetup Page To Register For Free Workshop</a><span style="color: red; font-family: 'Times New Roman'; font-size: small; font-weight: normal; line-height: normal;">&nbsp;**</span></h2>
<h2 class="section-title" data-lecture-id="276240" data-lecture-url="/courses/arduino-sbs/lectures/276240" data-next-lecture-id="276241" data-next-lecture-url="/courses/arduino-sbs/lectures/276241" data-previous-lecture-id="276238" data-previous-lecture-url="/courses/arduino-sbs/lectures/276238" id="lecture_heading" style="box-sizing: border-box; color: #333333; font-family: Proxima; font-size: 31px; line-height: 41px; margin-bottom: 18px; margin-top: 10px;">
<span style="font-weight: normal;"><a href="http://txplore.tv/courses/arduino-sbs/lectures/276240?affcode=6107_xiz8dp9c" rel="nofollow" target="_blank">Wifi connectivity, Part 1 of 4</a></span></h2>
<div>
<br />
<section style="box-sizing: border-box;"><article style="box-sizing: border-box;"><blockquote class="tr_bq">
In an earlier presentation, you learned about the Arduino Ethernet shield, and connected your Arduino to the Internet. In this presentation, we'll again connect the Arduino to the Internet, but we'll do that using Wifi, and go completely wireless!<br />
<br />
<br />
For this presentation, I chose the Adafruit CC3000 breakout board, with an on-board ceramic antenna. This product also is It comes as a shield, and with a connector for an external antenna if you need extended range. At around $35, it offers 802.11a/g connectivity, very small size, a nice library, and lots of documentation.</blockquote>
<blockquote class="tr_bq">
I will go through 3 demos in this presentation. In the first one (Part 2 of this presentation), we'll connect the CC3000 to the Arduino and run one of the library's examples to make sure that it works and that it can connect to our Wifi router. In the second one (Part 3 of this lecture), I'll show you how to create a Wifi web client, whereby the Arduino will be polling a URL, and fetching a file contains instructions for turning an LED on or off. The polling method has an advantage over the web server method because it is not affected by firewall or NAT restrictions. This means that by polling an external URL to your local network, you will be able to control your Arduino from anywhere in the Internet without having to configure your router to allow access to the Arduino from the outside world.</blockquote>
<blockquote class="tr_bq">
In the last one (Part 4 of this presentation) I will show you an adapted version of Demo 2 from the Ethernet presention, where we had a web server running on the Arduino, showing us a simple user interface through which we could turn an LED on and off.</blockquote>
<b>Parts</b><br /><ul>
<li>An Arduino Uno</li>
<li>The Adafruit CC3000 Wifi module</li>
<li>An LED</li>
<li>A 1kΩ resistor</li>
<li>Access to a Wifi access point.</li>
</ul>
<br /><b>Sketches for this presentation</b><br /><ul>
<li>Github (a link is available in External Resources)</li>
</ul>
</article></section><b>View external resources</b><br />
<ul>
<li><a href="https://github.com/futureshocked/arduino_sbs/tree/master/Wifi-CC3000">Demo sketches on Github</a></li>
<li><a href="http://processors.wiki.ti.com/index.php/CC3000">CC3000 documentation from Texas Instruments</a></li>
<li><a href="https://github.com/adafruit/Adafruit_CC3000_Library">The Arduino CC3000 library on Github</a></li>
<li><a href="http://processors.wiki.ti.com/index.php/CC3000_Serial_Port_Interface_%28SPI%29">CC3000 SPI documentation by Texas Instrument</a></li>
</ul>
</div>

</div></div>