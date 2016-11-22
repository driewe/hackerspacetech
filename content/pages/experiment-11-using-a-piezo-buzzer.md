Title: Experiment 11: Using a Piezo Buzzer
status: hidden

<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif; font-size: 14px; line-height: 20px;">Adapted from&nbsp;</span><a href="https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32?_ga=1.62774956.1058471170.1443294570" rel="nofollow" style="color: #7d181e; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px; text-decoration: none;" target="_blank">Sparkfun Inventor Kit Experiential Guide</a></h3>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Introduction</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
In this circuit, we’ll again bridge the gap between the digital world and the analog world. We’ll be using a piezo buzzer that makes a small “click” when you apply voltage to it (try it!). By itself that isn’t terribly exciting, but if you turn the voltage on and off hundreds of times a second, the piezo buzzer will produce a tone. And if you string a bunch of tones together, you’ve got music! This circuit and sketch will play a classic tune. We’ll never let you down!</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Parts Needed</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You will need the following parts:</div>
<ul style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; margin-top: 0px;">
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Breadboard</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;RedBoard or Arduino Uno</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">1x</span>&nbsp;Piezo Buzzer</li>
<li style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: 700;">3x</span>&nbsp;Jumper Wires</li>
</ul>
<div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Hardware Hookup</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Ready to start hooking everything up? Check out the Fritzing diagram below, to see how everything is connected.</div>
<table class="table table-bordered" style="background-color: white; border-collapse: collapse; border-spacing: 0px; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 20px; max-width: 100%; width: 640px;"><tbody style="box-sizing: border-box;">
<tr class="warning" style="box-sizing: border-box;"><td align="center" class="form-control-feedback" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Polarized Components&nbsp;<span class="glyphicon glyphicon-warning-sign" style="box-sizing: border-box; display: inline-block; font-family: &quot;glyphicons halflings&quot;; line-height: 1; position: relative; top: 1px;"></span></td><td align="left" style="background-color: #fcf8e3; border: 1px solid rgb(221, 221, 221); box-sizing: border-box; line-height: 1.42857; padding: 8px; vertical-align: top;">Pay special attention to the component’s markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction.</td></tr>
</tbody></table>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Fritzing Diagram for RedBoard</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<a href="https://cdn.sparkfun.com/assets/learn_tutorials/3/1/0/RedBoard_circuit_11_01.png" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; text-decoration: none;"><img alt="alt text" src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/RedBoard_circuit_11_01.png" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px; text-align: center;">
<em style="box-sizing: border-box;">Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.</em><br />
<div style="text-align: left;">
<em style="box-sizing: border-box;"></em></div>
<h3 style="box-sizing: border-box; color: #555555; font-family: montserrat, 'helvetica neue', helvetica, arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px; text-align: left;">
Run the Sketch</h3>
</div>
</div>
</div>
```
/*
SparkFun Inventor's Kit
Example sketch 11

BUZZER

  Use the buzzer to play a song!

  The buzzer in your Inventor's Kit is an electromechanical
  component you can use to make noise. Inside the buzzer is a
  coil of wire and a small magnet. When current flows through 
  the coil, it becomes magnetized and pulls towards the magnet,
  creating a tiny "click". When you do this thousands of times
  per second, you create tones.
  
  The Arduino has a built-in command called tone() which clicks
  the buzzer at a certain frequency. This sketch knows the
  frequencies of the common notes, allowing you to create songs.
  We're never going to let you down!

Hardware connections:

  The buzzer has two pins. One is positive and one is negative.
  The postitive pin is marked by a "+" symbol on both the top
  and bottom of the buzzer.
  
  Connect the positive pin to Arduino digital pin 9.
  (Note that this must be a PWM pin.)
  Connect the negative pin to GND.
  
  Tip: if the buzzer doesn't fit into the breadboard easily,
  try rotating it slightly to fit into diagonal holes.

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
(This sketch was originally developed by D. Cuartielles for K3)
This code is completely free for any use.
Visit http://learn.sparkfun.com/products/2 for SIK information.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/

/*
This sketch uses the buzzer to play songs.
The Arduino's tone() command will play notes of a given frequency.
We'll provide a function that takes in note characters (a-g),
and returns the corresponding frequency from this table:

  note 	frequency
  c     262 Hz
  d     294 Hz
  e     330 Hz
  f     349 Hz
  g     392 Hz
  a     440 Hz
  b     494 Hz
  C     523 Hz

For more information, see http://arduino.cc/en/Tutorial/Tone
*/
  
const int buzzerPin = 9;

// We'll set up an array with the notes we want to play
// change these values to make different songs!

// Length must equal the total number of notes and spaces 

const int songLength = 18;

// Notes is an array of text characters corresponding to the notes
// in your song. A space represents a rest (no tone)

char notes[] = "cdfda ag cdfdg gf "; // a space represents a rest

// Beats is an array of values for each note and rest.
// A "1" represents a quarter-note, 2 a half-note, etc.
// Don't forget that the rests (spaces) need a length as well.

int beats[] = {1,1,1,1,1,1,4,4,2,1,1,1,1,1,1,4,4,2};

// The tempo is how fast to play the song.
// To make the song play faster, decrease this value.

int tempo = 150;


void setup() 
{
  pinMode(buzzerPin, OUTPUT);
}


void loop() 
{
  int i, duration;
  
  for (i = 0; i < songLength; i++) // step through the song arrays
  {
    duration = beats[i] * tempo;  // length of note/rest in ms
    
    if (notes[i] == ' ')          // is this a rest? 
    {
      delay(duration);            // then pause for a moment
    }
    else                          // otherwise, play the note
    {
      tone(buzzerPin, frequency(notes[i]), duration);
      delay(duration);            // wait for tone to finish
    }
    delay(tempo/10);              // brief pause between notes
  }
  
  // We only want to play the song once, so we'll pause forever:
  while(true){}
  // If you'd like your song to play over and over,
  // remove the above statement
}


int frequency(char note) 
{
  // This function takes a note character (a-g), and returns the
  // corresponding frequency in Hz for the tone() function.
  
  int i;
  const int numNotes = 8;  // number of notes we're storing
  
  // The following arrays hold the note characters and their
  // corresponding frequencies. The last "C" note is uppercase
  // to separate it from the first lowercase "c". If you want to
  // add more notes, you'll need to use unique characters.

  // For the "char" (character) type, we put single characters
  // in single quotes.

  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int frequencies[] = {262, 294, 330, 349, 392, 440, 494, 523};
  
  // Now we'll search through the letters in the array, and if
  // we find it, we'll return the frequency for that note.
  
  for (i = 0; i < numNotes; i++)  // Step through the notes
  {
    if (names[i] == note)         // Is this the one?
    {
      return(frequencies[i]);     // Yes! Return the frequency
    }
  }
  return(0);  // We looked through everything and didn't find it,
              // but we still need to return a value, so return 0.
}
```
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Code To Note</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">char notes[] = "cdfda ag cdfdg gf ";</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">char names[] = {'c','d','e','f','g','a','b','C'};</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Up until now we’ve been working solely with numerical data, but the Arduino can also work with text. Characters (single, printable, letters, numbers and other symbols) have their own type, called “char”. When you have an array of characters, it can be defined between double-quotes (also called a “string”), OR as a list of single-quoted characters.</div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">tone(pin, frequency, duration);</code></div>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
One of Arduino’s many useful built-in commands is the&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">tone()</code>&nbsp;function. This function drives an output pin at a certain frequency, making it perfect for driving buzzers and speakers. If you give it a duration (in milliseconds), it will play the tone then stop. If you don’t give it a duration, it will keep playing the tone forever (but you can stop it with another function,&nbsp;<code style="background: rgb(248, 248, 248); border-radius: 3px; border: 1px solid rgb(234, 234, 234); box-sizing: border-box; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; margin: 0px 2px; padding: 0px 5px; white-space: nowrap;">noTone()</code>&nbsp;).</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
What You Should See</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
You should see - well, nothing! But you should be able to hear a song. If it isn’t working, make sure you have assembled the circuit correctly and verified and uploaded the code to your board or see the troubleshooting section.</div>
<div class="row" style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-left: -15px; margin-right: -15px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_11_01.jpg" style="background: 0px 0px; box-sizing: border-box; color: #e0311d; margin-left: 1em; margin-right: 1em; text-decoration: none;"><img src="https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/0/SIK_RedBoard_exp_11_01.jpg" style="border: 0px; box-sizing: border-box; height: auto; max-width: 100%; vertical-align: middle;" /></a></div>
<div class="col-xs-6 col-md-6" style="box-sizing: border-box; float: left; min-height: 1px; padding-left: 15px; padding-right: 15px; position: relative; width: 390px;">
</div>
</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Real World Application</h3>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Many modern megaphones have settings that use a loud amplified buzzer. They are usually very loud and quite good at getting people’s attention.</div>
<h3 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 20px;">
Troubleshooting</h3>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
No Sound</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Given the size and shape of the piezo buzzer it is easy to miss the right holes on the breadboard. Try double checking its placement.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Can’t Think While the Melody is Playing</h4>
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; margin-bottom: 10px;">
Just pull up the piezo buzzer whilst you think, upload your program then plug it back in.</div>
<h4 style="background-color: white; box-sizing: border-box; color: #555555; font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1; margin-bottom: 10px; margin-top: 10px;">
Feeling Let Down and Deserted</h4>
<div style="background-color: white; box-sizing: border-box; margin-bottom: 10px;">
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
The code is written so you can easily add your own songs.</div>
<div style="color: #333333; font-family: 'helvetica neue', helvetica, arial, sans-serif; font-size: 14px; line-height: 20px;">
<br /></div>
<div style="text-align: center;">
<span style="color: #333333; font-family: &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif;"><span style="font-size: 14px; line-height: 20px;"><a href="http://www.davidriewe.com/p/experiment-10-reading-soft-potentiometer.html">Experiment 10: Reading a Soft Potentiometer</a>&nbsp;-|-&nbsp;<a href="http://www.davidriewe.com/p/experiment-12-driving-motor.html">Experiment 12: Driving a Motor</a></span></span></div>
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
