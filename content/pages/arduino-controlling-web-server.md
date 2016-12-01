Title: Setting up an Arduino Controlling Web server

<div class="jumbotron">
<div class="container-fluid">
<h2 class="section-title" data-lecture-id="276228" data-lecture-url="/courses/arduino-sbs/lectures/276228" data-next-lecture-id="276229" data-next-lecture-url="/courses/arduino-sbs/lectures/276229" data-previous-lecture-id="276226" data-previous-lecture-url="/courses/arduino-sbs/lectures/276226" id="lecture_heading" style="box-sizing: border-box; color: #333333; font-family: proxima; font-size: 31px; line-height: 41px; margin-bottom: 18px; margin-top: 10px; text-align: center;">
<span style="color: red; font-family: 'Times New Roman'; font-size: small; font-weight: normal; line-height: normal;">**&nbsp;</span><a href="http://www.meetup.com/TechmillDenton/" rel="nofollow" style="font-family: 'Times New Roman'; font-size: medium; font-weight: normal; line-height: normal; text-align: center;" target="_blank">Visit Our Meetup Page To Register For Free Workshop</a><span style="color: red; font-family: 'Times New Roman'; font-size: small; font-weight: normal; line-height: normal;">&nbsp;**</span></h2>
<h2 class="section-title" data-lecture-id="276228" data-lecture-url="/courses/arduino-sbs/lectures/276228" data-next-lecture-id="276229" data-next-lecture-url="/courses/arduino-sbs/lectures/276229" data-previous-lecture-id="276226" data-previous-lecture-url="/courses/arduino-sbs/lectures/276226" id="lecture_heading" style="box-sizing: border-box; color: #333333; font-family: Proxima; font-size: 31px; line-height: 41px; margin-bottom: 18px; margin-top: 10px;">
<span style="font-weight: normal;"><a href="http://txplore.tv/courses/arduino-sbs/lectures/276228?affcode=6107_xiz8dp9c" rel="nofollow" target="_blank">An Arduino controlling web server</a></span></h2>
<blockquote class="tr_bq">
In this presentation, I will show you how to setup a web server on the Arduino that allows you to control LEDs via a web browser. You could replace the LEDs for other devices, like motors, without having to introduce significant changes to the sketch we'll see here. We will do this in the next presentation.</blockquote>
<blockquote class="tr_bq">
Just like in presentation 35, we first look at the HTTP request parsing issues that we will need to deal with before implementing the controlling web server sketch. Because the web browser will be sending information with instructions to the Arduino, the Arduino's web server HTTP parser will have a lot more work to do.</blockquote>
<b>Parts</b><br />
<ul>
<li>An Arduino</li>
<li>An Arduino Ethernet shield</li>
<li>One red LED</li>
<li>One yellow LED</li>
<li>Two 10KΩ resistors</li>
<li>Four jumper wires</li>
</ul>
<b><br />View external resources</b><br />
<ul>
<li><a href="https://github.com/futureshocked/arduino_sbs/blob/master/Controlling%20web%20server/ControllingWebServer_Manipulate_LED_using_GET/ControllingWebServer_Manipulate_LED_using_GET.ino">The demo sketch on Github</a></li>
</ul>
<div>
<h2 class="section-title" data-lecture-id="276230" data-lecture-url="/courses/arduino-sbs/lectures/276230" data-next-lecture-id="276232" data-next-lecture-url="/courses/arduino-sbs/lectures/276232" data-previous-lecture-id="276229" data-previous-lecture-url="/courses/arduino-sbs/lectures/276229" id="lecture_heading" style="box-sizing: border-box; color: #333333; font-family: Proxima; font-size: 31px; line-height: 41px; margin-bottom: 18px; margin-top: 10px;">
<span style="font-weight: normal;"><a href="http://txplore.tv/courses/arduino-sbs/lectures/276230?affcode=6107_xiz8dp9c" rel="nofollow" target="_blank">Controlling a motor with a web browser</a></span></h2>
</div>
<blockquote class="tr_bq">
In this presentation, I'll show you how to send HTTP GET requests that contain values other than 1s and 0s as we did in the previous presentations. To do that I will demonstrate how you can control a DC motor through your web browser. Motor control requires sending direction and speed values to the Arduino from your web browser, and this adds realism to our controlling web server.</blockquote>
<b>Parts</b><br />
<ul>
<li>An Arduino</li>
<li>An Arduino Ethernet shield</li>
<li>One or two DC motors</li>
<li>An L298N motor control bridge</li>
<li>A battery pack with 4 x 1.5V AA bateries or a 18V-9V power supply</li>
<li>A bunch of jumper wires</li>
</ul>
<br />
<b>View external resources</b><br />
<ul>
<li><a href="https://github.com/futureshocked/arduino_sbs/blob/master/Web%20motor%20control/webMotorControl_using_GET/webMotorControl_using_GET.ino">The demo sketch on Github</a></li>
</ul>

</div></div>