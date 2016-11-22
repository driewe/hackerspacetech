Title: Syncing Oscilloscope To Interrupt Activity
Date: 2016-02-22 15:19
Category: Blog
Tags: Arduino, Oscilloscope, Interrupts, Tutorials
Author: David Riewe

![Oscilloscope](/images/synching.jpg)

Debugging interrupt service routines can be very tricky.  It's not like
you can print out variabes to the serial port as you might when
debugging code outside the interrupt.  One way you can can get some idea
of what your code is doing in the ISR is to pulse one of the GPIO pins
while in the ISR.  On the 16Mhz Arduino Uno this takes about 4
microseconds of overhead.  Another reason you might want to generate a
pusle like this is to synchronize your oscilloscope with another event.


In the case of this experiment I wanted to see the clocking out of data
to a [74HC595](https://www.amazon.com/gp/product/B00HPPOXM4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00HPPOXM4&linkCode=as2&tag=teammilleniumonl&linkId=d88428782c982080350c532cf768c759) shift register. 


This all started when I wanted to modify a sample sketch from the
Sparkfun inventor kit to allow me to dynamically select and change the
pattern being displayed on the 8 leds.  The experiment was set up so
that the student was expected to un comment only the function to be used
then re-upload the sketch to the arduino/redboard.


We had an extra [Adafruit RGB LCD Matrix](https://www.amazon.com/gp/product/B00C461CAA/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00C461CAA&linkCode=as2&tag=teammilleniumonl&linkId=38ce86ad2e2c290d498cbbf8e691dffb) that had an I2C interface and 5
menu buttons.  This worked very nicely because it only requires 2 pins
from the redboard.  However, no matter what method you use to interact
with the redboard in this example, you have the following problem:  The
sketch as written uses delays between updating the led patterns.  In
fact, the majority of what the sketch does is wait in delays.  If you
try and add code that checks for key presses in the main loop of the
program then you will have times that you need to hold the button or
press the key for over half a second in order for the sketch to see it.
  ([See sketch that uses polling here](https://github.com/driewe/CodeBender/blob/master/SFE_Circuit_14.ino).

####There are are a few ways this can be solved

1 - Have the keyboard / buttons generate an external interrupt to the redboard which cases a keyboard read and stores the key pressed in a buffer to be processed soon as the current led pattern function call is finished. (this would require additional hardware to route the physical interrupt signal). 
2 - Set up a timer interrupt that polls the key for a keypressed, if one if
found, set a flag and store the keypress for the sketch to process soon
as the current led pattern function has finished.

> Note that both 1 and 2 will involve some delay in the response time but will reduce the need of having the user hold the key or button until the redboard has a chance to check it. 

3 - A third way to do this is set up a interrupt that occurs ever
millisecond, in the interrupt service routine you will check if the
required time has elapsed and if so update the leds with the next
pattern.  The main program of your loop will be devoted to interacting
with the user.  Every millisecond the program will take 15 microseconds
to decide if it needs to update the led patter on the [74HC595](https://www.amazon.com/gp/product/B00HPPOXM4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00HPPOXM4&linkCode=as2&tag=teammilleniumonl&linkId=d88428782c982080350c532cf768c759).  99% of
the time it has nothing to do and returns.  When it does need to update
the display it will take about 135 microseconds to shift the pattern
out.

This does require rewriting the code.  No longer will you have functions
you call for each pattern, but will keep a global variable telling the
interrupt service routine which pattern is active and will decide how to
do that within the interrupt service routine.  The advantage to doing
this is the updating the display is happening in the background and
allowing the main program to be more interactive with the user.
Here is a video of the project along with the code:  

<iframe width="560" height="315" src="https://www.youtube.com/embed/4tIKYcS4_fo" frameborder="0" allowfullscreen></iframe>

###Code Used In Video

```

// include the library code: for Adafruit RGB LCD
#include <Wire.h>
#include <Adafruit_RGBLCDShield.h>
//#include <utility/Adafruit_MCP23017.h>

Adafruit_RGBLCDShield lcd = Adafruit_RGBLCDShield();

// These #defines make it easy to set the backlight color
#define RED 0x1
#define YELLOW 0x3
#define GREEN 0x2
#define TEAL 0x6
#define BLUE 0x4
#define VIOLET 0x5
#define WHITE 0x7

#define MAX_MENU_ITEMS 8

char* Menu[] = {"1 After Another", "1 at a time", "Ping Pong",
                "Random LED", "Marquee", "Binary Count", "Increase Delay",
                "Decrease Delay"
               };

// Pin definitions:
// The 74HC595 uses a type of serial connection called SPI
// (Serial Peripheral Interface) that requires three pins:

int datapin = 2;
int clockpin = 3;
int latchpin = 4;



// We'll also declare a global variable for the data we're
// sending to the shift register:
byte data = 0;
int index = 0;								// current bit that is being acted on
int menuIndex = 0;   						// actively displayed menu item
int activePattern = 0;
int delayTime = 100;   							// delay in milliseconds
boolean PatternChanged = false;
boolean direction = true;
boolean TimeToTurnOn = true;				// used by
boolean SkipDelay = false;
unsigned long  PreviousMillis, CurrentMillis;  // will store last time LED was updated


void setup()
{
	Serial.begin(9600);
	// Set the three SPI pins to be outputs:

	pinMode(datapin, OUTPUT);
	pinMode(clockpin, OUTPUT);
	pinMode(latchpin, OUTPUT);
	pinMode(13, OUTPUT);
	// set up the LCD's number of columns and rows:
	lcd.begin(16, 2);
	lcd.setCursor(0, 0);
	lcd.print("Use up/dn buttons");

	// Timer0 is already used for millis() - we'll just interrupt somewhere
	// in the middle and call the "Compare A" function below
	OCR0A = 0xAF;
	TIMSK0 |= _BV(OCIE0A);
	lcd.clear();
	lcd.setCursor(0, 0);
	lcd.print("Use up/dn buttons");
	lcd.setCursor(0, 1);
	lcd.print(Menu[menuIndex]);


}


// Interrupt is called once a millisecond
SIGNAL(TIMER0_COMPA_vect)
{
	CurrentMillis = millis();

	if (PatternChanged == true)
	{
		PatternChanged = false;
		data = 0;
		direction = true;
		index = 0;
		TimeToTurnOn = true;
	}
	else if (CurrentMillis - PreviousMillis > delayTime || SkipDelay == true)		// is it time to update?
	{
		PreviousMillis = CurrentMillis;
		digitalWrite(13, HIGH);		// for scope trigger
		digitalWrite(13, LOW);

		switch (activePattern)
		{
			case 0:								// One after another
				if(direction == true && index < 7)
				{
					shiftWrite(index, HIGH);
					index += 1;
				}
				else if(direction == true && index == 7)
				{
					direction = false;
					shiftWrite(index, HIGH);
				}
				else if(direction == false && index > 0)
				{

					shiftWrite(index, LOW);
					index -= 1;
				}
				else if (direction == false && index == 0)
				{
					direction = true;
					shiftWrite(index, LOW);
				}
				break;

			case 1:							//  One at a time
				if(TimeToTurnOn == true)
				{
					shiftWrite(index, HIGH);
					TimeToTurnOn = false;
				}
				else						// time to turn off and update index
				{
					shiftWrite(index, LOW);
					TimeToTurnOn = true;

					if (index < 7)
					{
						index += 1;
					}
					else
					{
						index = 0;
					}

				}
				break;
			case 2:						// ping pong
				if(TimeToTurnOn == true)
				{
					shiftWrite(index, HIGH);
					TimeToTurnOn = false;
					SkipDelay = true;
				}
				else						// time to turn off and update index
				{
					shiftWrite(index, LOW);
					TimeToTurnOn = true;
					SkipDelay = false;
					if (direction == true)
					{
						if (index < 7)
						{
							index += 1;
						}
						else
						{
							direction = false;
							index -= 1;
						}
					}
					else				// direction must be false
					{
						if (index > 0)
						{
							index -= 1;
						}
						else
						{
							direction = true;
							index += 1;
						}
					}
				}
				break;

			case 3:						//random
				if(TimeToTurnOn == true)
				{
					index = random(8);
					shiftWrite(index, HIGH);
					TimeToTurnOn = false;
					SkipDelay = true;
				}
				else
				{
					shiftWrite(index, LOW);
					TimeToTurnOn = true;
					SkipDelay = false;
				}
				break;

			case 4:    // Marquee
				if(TimeToTurnOn == true)
				{
					shiftWrite(index, HIGH);
					shiftWrite(index + 4, HIGH);
					TimeToTurnOn = false;
					SkipDelay = false;
				}
				else						// time to turn off and update index
				{
					shiftWrite(index, LOW);
					shiftWrite(index + 4, LOW);
					TimeToTurnOn = true;
					SkipDelay = true;

				
					if (direction == true)
					{
						if (index < 3)
						{
							index += 1;
						}
						else
						{
							direction = false;
							index -= 1;
						}
					}
					else				// direction must be false
					{
						if (index > 0)
						{
							index -= 1;
						}
						else
						{
							direction = true;
							index += 1;
						}
					}
				}


				break;
				
			case 5:				// binary count
				digitalWrite(latchpin, HIGH);

				shiftOut(datapin, clockpin, MSBFIRST, data);

				digitalWrite(latchpin, LOW);
				data++;
		}

	}
}



void loop()
{

	uint8_t buttons = lcd.readButtons();

	if (buttons)
	{
		if (buttons & BUTTON_UP)
		{
			if(menuIndex > 0)
			{
				menuIndex -= 1;

			}
			else
			{
				//menuIndex = 0;
				menuIndex = MAX_MENU_ITEMS - 1;
			}
		}
		if (buttons & BUTTON_DOWN)
		{
			if(menuIndex < MAX_MENU_ITEMS - 1)
			{
				menuIndex += 1;
			}
			else
			{
				//menuIndex = MAX_MENU_ITEMS - 1;
				menuIndex = 0;
			}
		}

		if (buttons & BUTTON_SELECT)		//if select then assign the selected
		{
			//menu item
			if (menuIndex == 6)
			{
				delayTime += 25;
			}
			else if (menuIndex == 7)
			{
				delayTime -= 25;
			}
			else
			{
				activePattern = menuIndex;
				PatternChanged = true;			// flag the change for the ISR
			}

		}
		lcd.clear();
		lcd.setCursor(0, 0);
		lcd.print("Use up/dn buttons");
		lcd.setCursor(0, 1);
		lcd.print(Menu[menuIndex]);

	}

}

//
void shiftWrite(int desiredPin, boolean desiredState)
// This function lets you make the shift register outputs
// HIGH or LOW in exactly the same way that you use digitalWrite().
{
	bitWrite(data, desiredPin, desiredState);

	shiftOut(datapin, clockpin, MSBFIRST, data);
	digitalWrite(latchpin, HIGH);
	digitalWrite(latchpin, LOW);
}

```