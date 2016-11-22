Title: Playing Music With Remote Control
Date: 2015-11-03
Category: Blog
Tags: Arduino, Infrared, Projects
Author: David Riewe

This was the first experiment I did with Ken Shirrif's Infrared Remote Control Library for the Arduino. 

The circuit uses a TSOP382 IR photo sensor to receive the codes from the Clarion remote controller I had lying around.  Once the code is received the program then decides which tone to play.  In this example I have 8 tones set up, middle c through middle b.  For added fun and visual effects I turn on a led for each of the notes as they are played.

Here is a short video of a few notes being played on the Arduino.  Below the video is the code along with some instructions on how to modify the library so it will work with the tone() function.
<iframe width="560" height="315" src="https://www.youtube.com/embed/8W6UCkx7llQ" frameborder="0" allowfullscreen></iframe>

If you try to use this you will need to install the Arduino library written by Ken Shirrif.  You will also need to modify the library so that it uses TIMER1 instead of TIMER2 because TIMER2 is used by the tone() function. 

First, go to Libraries\Documents\Arduino\libraries\IRremote , the files for the library would be there.
In IRremoteInt.h, at line 194 you need to uncomment the IR_USE_TIME1 line and comment out the IR_USE_TIMER2

Now if your using codebender you will need to upload the modified version of Ken Shirrif's library to your personal libraries so that when compiling it will user your modified version rather than the default version that is allready registered with codebender.


[Source Code.](https://github.com/driewe/IRMusic/blob/master/sourcecode/IR_Music.ino)

```
/*
 * IRMusic: 
 * Uses Ken Shirriff's library to receive commands from a clarion IR remote then
 * play notes based on the command pressed.  
 * In order to compile upload modified version of Ken Shirrifs IRremote library
 * where IRremoteint.h is modified to use TIMER1 instead of TIMER2
 * This will leave TIMER2 free for the tone function that is used by this sketch.
 *
 * Note that TIMER1 uses pin9.  The library likes to use this for transmit.
 * Even though this sketch is not using any of the transmit functions I
 * do not attempt to use pin 9.
 * 
 */

#include <IRremote.h>

int RECV_PIN = 2;
int currentled = 0;

// Led Pin Numbers.  Used for visual effects
int leds[]={3, 4, 5, 6, 7, 10, 11, 12};

// notes to play
const int midc = 262;
const int midd = 294;
const int mide = 330;
const int midf = 349;
const int midg = 392;
const int mida = 440;
const int midb = 494;

// the following definitions are for my specific clarion controller
// 
const long func = 0x6106C03F;
const long uparrow = 0x6106D827;
const long zone = 0x6106D02F;
const long reverse = 0x61066897;
const long play = 0x610610EF;
const long forward = 0x6106E817;
const long down = 0x6106B847;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()
{
  Serial.begin(9600);
  // set led pins to output
  for(int i=0;i<7;i++) pinMode(leds[i], OUTPUT);
  irrecv.enableIRIn(); // Start the receiver
}

// Note about checking for currentled below.
// Only when the note changes do we want to turn off the current led then
// turn on the led matching the new note.  To prevent flicker of leds
// I solved by keeping a variable "currentled" that I would check each time
// if the currentled didn't go with the results.value then I would turn off
// the currentled then set currentled to the new value and turn that on and play the tone.
// 
void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if (results.value == func) 
    {
      if (currentled != 0) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 0;
      }
      digitalWrite(leds[currentled], HIGH);
      tone(8, midc);
    } 
    else if (results.value == uparrow)
    {
      if (currentled != 1) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 1;
      }     
      digitalWrite(leds[currentled], HIGH);      
      tone(8, midd);
    }
    else if (results.value == zone)
    {
      if (currentled != 2) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 2;
      }      
      digitalWrite(leds[currentled], HIGH);      
      tone(8, mide);
    }
    else if (results.value == reverse)
    {
      if (currentled != 3) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 3;
      }      
      digitalWrite(leds[currentled], HIGH);      
      tone(8, midf);
    }
    else if (results.value == play)
    {
      if (currentled != 4) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 4;
      }      
      digitalWrite(leds[currentled], HIGH);      
      tone(8, midg);
    }
    else if (results.value == forward)
    {
      if (currentled != 5) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 5;
      }      
      digitalWrite(leds[currentled], HIGH);      
      tone(8, mida);
    }
    else if (results.value == down)
    {
      if (currentled != 6) 
      {
        digitalWrite(leds[currentled], LOW);
        currentled = 6;
      }      
      digitalWrite(leds[currentled], HIGH);      
      tone(8, midb);
    }
  } 
  else 
  {
    noTone(8);
    digitalWrite(leds[currentled], LOW);
  }
  irrecv.resume();
  delay(200);
}
```

Most likely you will not have the same controller that I have.  Therefore, use the receiving ir example from the library to discover the unique codes for your controller then replace them in the source code.

[Sparkfun IR Tutorial](https://learn.sparkfun.com/tutorials/ir-communication)
