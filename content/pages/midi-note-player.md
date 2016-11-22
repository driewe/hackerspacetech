Title: MIDI Note Player
status: hidden

This tutorial shows how to send MIDI notes from an Arduino or Genuino board to a MIDI instrument connected through the standard 5 poles DIN cable.<br />
<br />
<a href="http://en.wikipedia.org/wiki/MIDI">MIDI</a>, the Musical Instrument Digital Interface, is a useful protocol for controlling synthesizers, sequencers, and other musical devices. MIDI devices are generally grouped in to two broad classes: controllers (i.e. devices that generate MIDI signals based on human actions) and synthesizers (including samplers, sequencers, and so forth). The latter take MIDI data in and make sound, light, or some other effect.<br />
<br />
MIDI is a serial protocol that operates at 31,250 bits per second. The board built-in serial port (all of them on the Mega as well) can send data at that rate.<br />
<br />
MIDI bytes are divided into two types: command bytes and data bytes. Command bytes are always 128 or greater, or 0x80 to 0xFF in hexadecimal. Data bytes are always less than 127, or 0x00 to 0x7F in hex. Commands include things such as note on, note off, pitch bend, and so forth. Data bytes include things like the pitch of the note to play, the velocity, or loudness of the note, amount of pitch bend and so forth. For more details, see the MIDI specification or one of the many <a href="http://hinton-instruments.co.uk/reference/midi/protocol/index.htm">MIDI Protocol Guides</a> on the Web.<br />
<br />
MIDI data is usually notated in hexadecimal because MIDI banks and instruments are grouped in groups of 16.<br />
<br />
For more see this <a href="http://www.tigoe.net/pcomp/code/communication/midi">introduction to MIDI</a> or this <a href="http://itp.nyu.edu/physcomp/Labs/MIDIOutput">example</a>.<br />
<div>
<br />
<span style="font-size: large;">Hardware Required</span><br />
<ul>
<li>Arduino</li>
<li>Female MIDI jack</li>
<li>2 220 ohm resistors</li>
<li>hook-up wires</li>
<li>MIDI enabled device (optional, for testing)</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Circuit</span><br />
<ul>
<li>All MIDI connectors are female, by definition of the MIDI spec. Here's how to wire the connector to the board:</li>
<li>MIDI jack pin 5 connected to Digital pin 1 through a 220 ohm resistor</li>
<li>MIDI jack pin 2 connected to ground</li>
<li>MIDI jack pin 4 connected to +5V through a 220 ohm resistor</li>
</ul>
<br />
<br />
click the image to enlarge<br />
<div class="circuit" style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/MIDI_bb.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/MIDI_bb.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
<br />
<br />
image developed using <a href="http://www.fritzing.org/">Fritzing</a>. For more circuit examples, see the <a href="http://fritzing.org/projects/">Fritzing project page</a><br />
Schematic<br />
<br />
click the image to enlarge<br />
<div style="background-color: white; box-sizing: border-box; color: #4f4e4e; direction: ltr; font-family: 'TyponineSans Regular 18', 'Lucida Grande', Lucida, Verdana, sans-serif; font-size: 18px; line-height: 31.5px; margin: 0px; padding: 0px;">
<a class="urllink" href="https://www.arduino.cc/en/uploads/Tutorial/MIDI_schem.png" rel="nofollow" style="box-sizing: border-box; color: #00979c; line-height: inherit; text-decoration: none;"><img alt="" src="https://www.arduino.cc/en/uploads/Tutorial/MIDI_schem.png" style="border: none; box-sizing: border-box; display: inline-block; vertical-align: middle;" title="" width="400px" /></a></div>
</div>
<br />
<span style="font-size: large;">Code</span><br />
<br />
Attention If you're using a board with ATmega32U4 like DUE or Leonardo, please replace Serial with Serial1 in the sketch below.</div>
<div>
<br /></div>
<div>
<br /></div>
```
/*
 MIDI note player

 This sketch shows how to use the serial transmit pin (pin 1) to send MIDI note data.
 If this circuit is connected to a MIDI synth, it will play
 the notes F#-0 (0x1E) to F#-5 (0x5A) in sequence.


 The circuit:
 * digital in 1 connected to MIDI jack pin 5
 * MIDI jack pin 2 connected to ground
 * MIDI jack pin 4 connected to +5V through 220-ohm resistor
 Attach a MIDI cable to the jack, then to a MIDI synth, and play music.

 created 13 Jun 2006
 modified 13 Aug 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Midi

 */

void setup()
{
	//  Set MIDI baud rate:
	Serial.begin(31250);
}

void loop()
{
	// play notes from F#-0 (0x1E) to F#-5 (0x5A):
	for (int note = 0x1E; note < 0x5A; note ++)
	{
		//Note on channel 1 (0x90), some note value (note), middle velocity (0x45):
		noteOn(0x90, note, 0x45);
		delay(100);
		//Note on channel 1 (0x90), some note value (note), silent velocity (0x00):
		noteOn(0x90, note, 0x00);
		delay(100);
	}
}

//  plays a MIDI note.  Doesn't check to see that
//  cmd is greater than 127, or that data values are  less than 127:
void noteOn(int cmd, int pitch, int velocity)
{
	Serial.write(cmd);
	Serial.write(pitch);
	Serial.write(velocity);
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
