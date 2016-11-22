Title: Matrix keypad with 7 segment display 
status: hidden

This mini project shows you how to read a 3x4 matrix keypad and display the results on a 7 segment display via a 74HC595 serial to parallel shift register.<br />
<br />
<span style="font-size: large;">Hardware</span><br />
<br />
<ul>
<li>Arduino</li>
<li>Adafruits&nbsp;<a href="https://www.adafruit.com/products/419" rel="nofollow" target="_blank">Membrane 3x4 Matrix Keypad</a></li>
<li>7 Seg LCD Display (common cathode is what I used)</li>
<li>74HC595</li>
<li>330 resistor</li>
<li>hookup wire</li>
<li>breadboard</li>
</ul>
<div>
<span style="font-size: large;">Circuit:</span></div>
<div>
<br /></div>
<div>
Connect the keypad to the Arduino to match this image</div>
<div class="separator" style="clear: both; text-align: center;">
<a href="https://2.bp.blogspot.com/-oAeRkRoWcJ8/Vv6yVpZrilI/AAAAAAAAs4I/rBNgSZys6K83g_nvhgFPSZRCCEpw3TiPg/s1600/membranekeypad34arduino_LRG.jpg" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="491" src="https://2.bp.blogspot.com/-oAeRkRoWcJ8/Vv6yVpZrilI/AAAAAAAAs4I/rBNgSZys6K83g_nvhgFPSZRCCEpw3TiPg/s640/membranekeypad34arduino_LRG.jpg" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-size: large;">Connecting up the 74HC595</span></div>
<br />
<br />
<b>Make the following connections:</b><br />
GND (pin 8) to ground,<br />
Vcc (pin 16) to 5V<br />
OE (pin 13) to ground<br />
MR (pin 10) to 5V<br />
<br />
This set up makes all of the output pins active and addressable all the time. The one flaw of this set up is that you end up with the lights turning on to their last state or something arbitrary every time you first power up the circuit before the program starts to run. You can get around this by controlling the MR and OE pins from your Arduino board too, but this way will work and leave you with more open pins.<br />
<div>
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="https://1.bp.blogspot.com/-7ZmCGxtJKFk/Vv6zgaKQR3I/AAAAAAAAs4U/APX-pkLAYKsbylyTdJyt9HkfzY80TSfhA/s1600/ShftOutExmp1_1.gif" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="377" src="https://1.bp.blogspot.com/-7ZmCGxtJKFk/Vv6zgaKQR3I/AAAAAAAAs4U/APX-pkLAYKsbylyTdJyt9HkfzY80TSfhA/s640/ShftOutExmp1_1.gif" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<br />
<span style="font-size: large;">Arduino Connections to 74HC595</span><br />
<div>
<br /></div>
<div>
DS (pin 14) to Ardunio DigitalPin 11 (blue wire)<br />
SH_CP (pin 11) to to Ardunio DigitalPin 10 (yellow wire)<br />
ST_CP (pin 12) to Ardunio DigitalPin 9 (green wire)<br />
<br />
From now on those will be refered to as the dataPin, the clockPin and the latchPin respectively. Notice the 0.1"f capacitor on the latchPin, if you have some flicker when the latch pin pulses you can use a capacitor to even it out.<a href="https://1.bp.blogspot.com/-sO6Hv1m58Bg/Vv61KoQdZ3I/AAAAAAAAs4g/FXZf6S7Dq7YdkX_f9gSkgTNX2es-vgl7w/s1600/ShftOutExmp1_2.gif" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" height="334" src="https://1.bp.blogspot.com/-sO6Hv1m58Bg/Vv61KoQdZ3I/AAAAAAAAs4g/FXZf6S7Dq7YdkX_f9gSkgTNX2es-vgl7w/s640/ShftOutExmp1_2.gif" width="640" /></a><br />
<br />
<span style="font-size: large;">Connecting 7 Seg Dispay to 74HC595</span><br />
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
I used a common cathode seven segment display which means the middle pin on the top (pin 9) and bottom (pin 3) of the display would be connected to ground via a 220ohm current limiting resistor (pins 3 and 9). &nbsp;Starting with D0 of the 74HC595 (pin 15) I connected to the dot segment on the 7 segment display, and followed around connecting D2 - D7 to the remaining segments.</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
I use trial and error to figure out what my bit map would be. &nbsp;You can look at the symbols array in the code and compare the bits being turned on with the segments that it takes to make that number. &nbsp;For example. &nbsp;to display a character number 1 on a seven segment display we need to turn on segments 'c' and 'b'. &nbsp;The bit pattern to do that is B00010010, so we can conclude that D1 connects to the c segment and D4 to the b (notice when making a 6 that D4 is off while D1 is on, that is how I knew D1 connects to the c segment and b to the D4)</div>
<div>
<div>
<br /></div>
<div>
<div>
<br /></div>
<div>
<span style="font-size: large;">Code</span></div>
<div>
<br /></div>
```
#include "Arduino.h"
#include "Keypad.h"

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] =
{
	{'1', '2', '3'},
	{'4', '5', '6'},
	{'7', '8', '9'},
	{'*', '0', '#'}
};
byte rowPins[ROWS] = {8, 7, 6, 5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {4, 3, 2}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

//Pin connected to latch pin (ST_CP) of 74HC595
const int latchPin = 9;
//Pin connected to clock pin (SH_CP) of 74HC595
const int clockPin = 10;
////Pin connected to Data in (DS) of 74HC595
const int dataPin = 11;

const byte CHAR_COUNT = 10;

const byte symbols[CHAR_COUNT] =
{
	B01111110, // 0
	B00010010, // 1
	B10111100, // 2
	B10110110, // 3
	B11010010, // 4
	B11100110, // 5
	B11101110, // 6
	B00110010, // 7
	B11111110, // 8
	B11110110  // 9
};


void setup()
{
	//set pins to output because they are addressed in the main loop
	pinMode(latchPin, OUTPUT);
	pinMode(dataPin, OUTPUT);
	pinMode(clockPin, OUTPUT);
	Serial.begin(9600);
}

void loop()
{
	char key = keypad.getKey();

	if (key != NO_KEY)
	{
		Serial.println(key);
		Serial.println(symbols[key-48]);
		writeLeds(symbols[key - 48]);
	}

}


void writeLeds(byte pattern)
{
	// turn off the output so the pins don't light up
	// while you're shifting bits:
	digitalWrite(latchPin, LOW);

	// shift the bits out:
	shiftOut(dataPin, clockPin, MSBFIRST, pattern);

	// turn on the output so the LEDs can light up:
	digitalWrite(latchPin, HIGH);
}
```

<span style="font-size: large;">Video</span><br />
<br />
<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/lIJE86yvEU0" width="560"></iframe>
</div>
</div>
