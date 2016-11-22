Title: Serial to Parallel Shifting-Out with a 74HC595
Date: 2015-11-8
Category: Blog
Tags: Arduino, 75HC595, tutorials
Author: David Riewe

![74HC595 Driving 8 Leds](/images/74hc595.jpg)

Using the 74HC595 to control 8 leds (outputs) without giving up 8 ports on the arduino uno. Three outputs from the arduino are used to shift the data out in serial to the 74HC595 were it is then parceled out to each of its individual pins. You can link multiple registers together to extend your output even more, without giving up any more pins on the arduino.

> Note: The shift register is not what gives the appearance of the led going back and foth...ie shifting. All the shifting happens prior to the output states changing. The led appears to be shifting because it is in a loop writing the numbers 1, 2, 4, 8, 16, 32, 64, 128, 64, 32, 16, 8, 4, and 2.

If you are interested in seeing how fast data is shifted out by a 16MHz Arduino check out the post [Syncing Oscilloscope To Interrupt Activity](/syncing-oscilloscope-to-interrupt-activity.html) where we will use an oscilloscope to observe the shiftout command in action.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/-JyDOHiEaF0" frameborder="0" allowfullscreen></iframe>
</center>

 Pin out for the 74HC595 along with a short tutorial by Simon Monk can be [found here](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds/overview).

```
 /*
Using the 74HC595 to control 8 leds (outputs) without giving up 8 ports on the arduino uno. 
Three outputs from the arduino are used to shift the data out in serial to the 74HC595 were it 
is then parceled out to each of its individual pins. 

*/

int latchPin = 5;   // to pin 12
int clockPin = 6;	// to pin 11
int dataPin = 4;	// to pin 14

byte leds = 0;
int pattern[] = {1, 2, 4, 8, 16, 32, 64, 128, 64, 32, 16, 8, 4, 2};

void setup() 
{
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);  
  pinMode(clockPin, OUTPUT);
}

void loop() 
{
	
  	for (int i = 0; i < 14; i++)
  	{
    	leds = pattern[i];
    	updateShiftRegister();
    	delay(1000);
  	}
}

void updateShiftRegister()
{
   	digitalWrite(latchPin, LOW);
   	shiftOut(dataPin, clockPin, LSBFIRST, leds);
   	digitalWrite(latchPin, HIGH);
}
``` 