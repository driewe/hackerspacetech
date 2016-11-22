Title:Matrix keypad with 7 segment display (Arduino mini project)
Date: 2016-02-12 12:53
Category: Blog
Tags: Arduino, keypad, 7-Segment Display, Tutorials
Author: David Riewe


![Matrix Keypad](/images/matrixkeypad.png)

3x4 Matrix keypad connected to an arduino. Displaying results of key pressed on a 7 segment led display via 74HC595 shift register which
reduces the required pins of the 7seg display from 8 to 3.

[Learn More about about Matrix Keyboards on Arduiino Playground](http://playground.arduino.cc/Main/KeypadTutorial)

[Learn More about using the 74HC595](https://www.arduino.cc/en/Tutorial/ShiftOut)

I will be holding Arduino classes at Northbranch Library on the 2nd and
4th Saturdays . [Click Here For More Info.](http://www.meetup.com/hackerspacetech.com)

Come learn both theory and trouble shooting techniques.  If you cannot
make it I can also skype.

Here is the video followed by the code used in this mini project:

<iframe width="560" height="315" src="https://www.youtube.com/embed/lIJE86yvEU0" frameborder="0" allowfullscreen></iframe>


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

