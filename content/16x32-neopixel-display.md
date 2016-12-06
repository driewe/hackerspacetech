Title: Building A 16x32 NeoPixel Display
Date: 2016-10-30
Category: Blog
Tags: NeoPixel, Projects
Author: David Riewe

<style>
h6 {
    text-align: center;
}
</style>


<p><h5>Earlier this year while attending a <a href="http://www.fabnow-conference.com" target="_blank">FabNow Conferance</a> in Ft. Worth I came across a few exibits with <a href="/neopixel-16-ring-fun.html">Neo Pixel Rings.  I was fascinated with the color levels and the fact they could be controlled with a single wire!  While experimenting with the <a href="/neopixel-16-ring-fun.html">Neo Pixel Rings</a> I learned about Adafruits <a href="http://amzn.to/2fVoeuE" target="_blank">NeoPixel 64 LED 8x8 Matrix</a>, the FadeCandy controller then was mesmerized by some of the demonstrations at <a href="http://www.misc.name/fadecandy" target="_blank">Micah Elizabeth Scotts website</a> and the <a href="https://learn.adafruit.com/led-art-with-fadecandy" target="_blank">LED Art with Fadecandy</a> tutorial on Adafruits website.</h5></p>

<p><h5>I was hooked.  I knew I wanted to build some sort of display using the <a href="http://amzn.to/2fVoeuE" target="_blank">8x8 neopixel panels</a> and control them using the FadeCandy!  Using the <a href="https://learn.adafruit.com/led-art-with-fadecandy" target="_blank">LED Art with Fadecandy</a> tutorial on Adafruits website as I guide I thought I would start off with four of the <a href="http://amzn.to/2fVoeuE" target="_blank">8x8 neopixel panels</a> but then decided to go with eight so I either build two separate 2x2 panel displays (16x16) or one larger 16x32 display.</h5></p>

<h4>Parts List</h4>
<ul>
<li><a href="http://amzn.to/2fVoeuE" target="_blank">Adafruit NeoPixel NeoMatrix 8x8 - 64 RGB LED Pixel Matrix</a></li>
<li><a href="http://amzn.to/2gCDlaF" target="_blank">FadeCandy - Dithering USB-Controlled Driver for NeoPixels</a></li>
<li><a href="http://amzn.to/2fP9idY" target="_blank">5V 10A switching power supply</a></li>
<li>Each of the 8x8 Panels can draw up to 3.5 amps if all LEDs are turned on full white.  Two 10amp supplies were purchased so that I would have ample power to supply four of the  8x8 matrixes.</li>
<li>I also picked up some stranded wire from Tanner electronics.  16 gauge was used to provide main power to each of the panels and 22 gauge was used for the data signals from the Fadecandy to the 8x8 panels.</li>
</ul>

<p><h5>With parts in hand I started out by wiring up four of the 8x8 panels.  The wires on the top, running to the left, are 16 gauge stranded wire and will be combined into a barrel connector that will connect with a 5volt 10 amp supply.  The wires on the bottom bring the signal and ground from the fadecandy controller.  The twisting of the wires was dones simply to keep things neat.  I used masking tape along with toothpicks to provide some structural support until I would be ready to mount the panels.</h5></p>

<h4>Here is a closer look at the Fadecandy controller.</h4>

<div class="container-fluid">
<row>
    <div class="col-sm-4">
        <a href="/images/fadecandy/1x4-panel-rear.resized.jpg" title="Click To Enlarge"><img src="/images/fadecandy/1x4-panel-rear.resized.jpg" class="img-rounded img-responsive img-thumbnail"></a>
        <h6>1x4 Rear View</h6>
    </div>

    <div class="col-sm-4">
        <a href="/images/fadecandy/fccontroller.resized.jpg" title="Click To Enlarge"><img src="/images/fadecandy/fccontroller.resized.jpg" class="img-rounded img-responsive img-thumbnail"></a>
    </div>
    <div class="col-sm-4">
        <a href="/images/fadecandy/fccontroller2.resized.jpg" title="Click To Enlarge"><img src="/images/fadecandy/fccontroller2.resized.jpg" class="img-rounded img-responsive img-thumbnail"></a>
    </div>
</row>
</div>

<h4>Construction Of Panel</h4>

<h5>With both 1x4 panels wired up it is time to get ready for mounting to a permanent base.  I chose a sheet of plexiglass I had lying around that was 1/8" thickness.
Prior to starting the build I had laid all eight panels out on a xerox machine and produced a outline of where all the holes in the pc boards were located.  Using this as a guide I drilled holes int he plexi-glass for mounting the 8x8 matrix panels. </h5>
<div class="container-fluid">
<row>
    <div class="col-sm-4">
        <a href="/images/fadecandy/premount.resized.jpg" title="Click To Enlarge"><img src="/images/fadecandy/premount.resized.jpg" class="img-rounded img-responsive img-thumbnail"></a>
    </div>
    <div class="col-sm-4">
        <a href="/images/fadecandy/rearview.resized.jpg" title="Click To Enlarge"><img src="/images/fadecandy/rearview.resized.jpg" class="img-rounded img-responsive img-thumbnail"></a>
        <h6>Rear view of mounted panels</h6>
    </div>
    <div class="col-sm-4">
        <a href="/images/fadecandy/frontview.resized.jpg" title="Click To Enlarge"><img src="/images/fadecandy/frontview.resized.jpg" class="img-rounded img-responsive img-thumbnail"></a>
        <h6>Front view of mounted panels</h6>
    </div>
</row>
</div>


<h4>Here is a short video of the 16x32 panel without any diffuser</h4>
<iframe width="560" height="315" src="https://www.youtube.com/embed/PqErA3lq35Q" frameborder="0" allowfullscreen></iframe>

<h4>Here is a short video of the un-diffused 16x32 responding to some music</h4>
<iframe width="560" height="315" src="https://www.youtube.com/embed/d7M31PMLR6c" frameborder="0" allowfullscreen></iframe>

<p><h5>At this point I was still un-decided where to go next.  One option was to use the extra space on the plexiglass to mount suction cups that would allow mounting the display to the glass wall of the North Branch Library makerspace.  Realizing I needed some sort of diffuser I started looking into different shadow boxes at local arts and crafts store.  I one which would allow the 2x4 panels to fit nicely inside.  I used my drimmel to carefully cut away the extra plexi-glass, allowing the display to fit inside of the shadow box.</h5></p>

<a href="/images/fadecandy/shadowboxrear.rotated.jpg" title="Click To Enlarge"><img src="/images/fadecandy/shadowboxrear.rotated.jpg" class="img-rounded img-responsive img-thumbnail"></a>

<p><h5>For a difusser I went to Lowes and found an overhead flourescent light diffuser panel that was chipped (the chip allowed me to negotiate a better price).  I used a right angle to mark the outline of the section I would need to cut out with a marker then used a fine tip soldering iron to go over the lines slowly until I had burned and etch over half way through.  I ended up needed three of these to get the level of diffusion that I was satisfied with.</h5></p>

<h4>Here is the 16x32 with diffusers in place running a rings algorythm</h4>
<iframe width="560" height="315" src="https://www.youtube.com/embed/qufMyeZC1rk" frameborder="0" allowfullscreen></iframe>

<h4>Here we have some cool trails</h4>
<iframe width="560" height="315" src="https://www.youtube.com/embed/1phsNupJlso" frameborder="0" allowfullscreen></iframe>

<p><h5>In a follow up post I will go into more detail on how we control the display via the Fadecandy controller using any programming language that can write to a web socket.</h5></p>

<p><h5>For now I would encourage you to take a look at the <a href="https://github.com/scanlime/fadecandy" target="_blank">Fadecandy Repo on Github</a></h5></p>

