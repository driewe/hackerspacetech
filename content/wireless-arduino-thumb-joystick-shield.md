Title: Wireless Arduino Thumb Joystick Shield
Date: 2015-12-17 
Category: Blog
Tags: Arduino, Wireless, Shield, Projects
Author: David Riewe

![Joystick Shield](/images/joystick.jpg)

This shield provides the necessary connections between the joystick and the Arduino so that it can read the joysticks X, Y and Switch readings on it's analog inputs.  I chose to mount the joystick on it's own proto shield instead of mounting it to the prototype area of my XBee shield.

Looking at the picture to the left you can see three yellow wires that connect to A0, A1 and A2.  These correspond to the VRx, VRy and SW outputs from the joystick. 

In the video I mount the shield to an XBee Wireless shield then mount that to the Arduino that acts as the brain for this wireless joystick controller.  The XBee shield has it's serial switch set so that it looks for serial data D2 and D3, requiring the use of the Software Serial library, leaving the hardware UART on the arduino free for programming and debugging. 

The Arduino program polls the status of the joystick every 40 ms (about 20 times a second) then transmits the X, Y and Switch readings over via the XBee wireless module to an XBee wireless module on a Sparkfun redbot.  The program on the Sparkfun Redbot receives the values then makes the necessary adjustment to the power and direction of it's left and right wheels causing the redbot to go forward, backwards or turn.

Software on controller:

https://codebender.cc/sketch:203681

```
// SoftwareSerial is used to communicate with the XBee
#include <SoftwareSerial.h>

// XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
// XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
SoftwareSerial XBee(2, 3); // RX, TX

//values read from joy stick i.e. (0-1023)
int xval = 0;
int yval = 0;
int swval = 0;
int xval2 = 0;
int yval2 = 0;
int swval2 = 0;
float temp;

const int xpin = A1;
const int ypin = A2;
const int swpin = A0;   // this is the

const int xpin2 = A4;
const int ypin2 = A5;
const int swpin2 = A3;

void setup()
{
	// Initialize XBee Software Serial port. Make sure the baud
	// rate matches your XBee setting (9600 is default).
	XBee.begin(9600);
	Serial.begin(9600);
	
	// enable pull up on analog pins that are connected to the SEL output
	// of the joystick
	//digitalWrite(A0, HIGH);
	//digitalWrite(A3, HIGH);
}

void loop()
{
	xval = analogRead(xpin);
	temp = (float)xval / (float)1023;
	xval = 255 * temp;

	swval = analogRead(swpin);			// only concered if swval is 0
	if (swval != 0) swval = 255;

	yval2 = analogRead(ypin2);
	temp = (float)yval2 / (float)1023;
	yval2 = 255 * temp;

	swval2 = analogRead(swpin2);


	if (swval2 != 0) swval2 = 255;


	XBee.write(xval);  // This first code will be interpreted for steering
	XBee.write(yval2);  // motor drive
	XBee.write(swval);

	Serial.print("swval = ");
	Serial.println(swval);
	delay(50);
	if (swval == 0) delay(600);  // horn was pressed, give user time to release'

}
```

Software on Redbot

https://codebender.cc/sketch:202598

```

#include <RedBot.h>  // This line "includes" the RedBot library into your sketch.
// Provides special objects, methods, and functions for the RedBot.
RedBotMotors motors; // Instantiate the motor control object. This only needs

#include "notes.h"  // Individual "notes" have been #defined in the notes.h tab to make
// playing sounds easier. noteC4, for example, is defined as 262, the
// frequency for middle C. See the tab above?

RedBotSoftwareSerial XBee;  // version of SoftwareSerial that will work with Redbot

const int buzzerPin = 9;

int xval;
int yval;
int swval=1023;
int leftmotorspeed;
int rightmotorspeed;

float temp;

void setup()
{
	// Initialize XBee Software Serial port. Make sure the baud
	// rate matches your XBee setting (9600 is default).
	XBee.begin(9600);
	Serial.begin(9600);
	pinMode(buzzerPin, OUTPUT);
}

void loop()
{

//	if (XBee.available())
	if (XBee.available())
	{
		xval = XBee.read();
		yval = XBee.read();
		swval = XBee.read();
		//xval = Serial.read();
		//yval = Serial.read();
		//swval = Serial.read();

		//normalize the values to a 1 byte value

		temp = (float)xval / (float)255;
		xval = temp * 1023;

		temp = (float)yval / (float)255;
		yval = temp * 1023;

		temp = (float)swval / (float)255;
		swval = temp * 1023;

		xval = map(xval, 0, 1023, -255, 255);
		yval = map(yval, 0, 1023, -255, 255);

	}

	if(swval == 0) 
	{
		XBee.end();
	//	playSmallWorld();
		blowhorn();
		XBee.begin(9600);
	}
	
	if (xval > -40 && xval < 40)  			// If we are not turning
	{										
		if ((yval < -40) || (yval > 40))    // set motor speed
		{
			rightmotorspeed = yval;
			leftmotorspeed = -yval; 
		}
		else
		{
			rightmotorspeed = 0;
			leftmotorspeed = 0;		
		}
     
	}
	else if (xval>40)  // Turning Left, are we moving while turning left or 
	{					// spinning
		if ((yval < -40) || (yval > 40)) // User is moving forward or backwards
		{
			rightmotorspeed = yval; 	// drive right motor 100% forward
			leftmotorspeed = -yval/2;	// runt left by slowing left wheel
		}
		else    						// spin
		{
			rightmotorspeed = 200;
			leftmotorspeed = 200;
		}
	}
	else			// We are not going straight or turning left, must be right
	{
		if ((yval < -40) || (yval > 40))    // user is moving forward or backwards
		{
			leftmotorspeed = -yval;
			rightmotorspeed = yval/2;
		}
		else
		{
			rightmotorspeed = -200;
			leftmotorspeed = -200;
		}
	}

	motors.rightMotor(rightmotorspeed);
	motors.leftMotor(leftmotorspeed);
	delay(50);
}

void blowhorn()
{
	tone(buzzerPin, 1000);   // Play a 1kHz tone on the pin number held in
	//  the variable "buzzerPin".
	delay(125);   // Wait for 125ms.
	noTone(buzzerPin);   // Stop playing the tone.

	tone(buzzerPin, 2000);  // Play a 2kHz tone on the buzzer pin

	delay(500);   // delay for 1000 ms (1 second)

	noTone(buzzerPin);       // Stop playing the tone.

}

void playSmallWorld()
{
	// we use a custom function below called playNote([note],[duration])
	// to play a note and delay a certain # of milliseconds.
	//
	// Both notes and durations are #defined in notes.h -- WN = whole note,
	// HN = half note, QN = quarter note, EN = eighth note, SN = sixteenth note.
	//
	playNote(noteG5, HN + QN);
	playNote(noteG5, QN);
	playNote(noteB5, HN);
	playNote(noteG5, HN);
	playNote(noteA5, HN + QN);
	playNote(noteA5, QN);
	playNote(noteA5, HN + QN);
	playNote(Rest, QN);
	playNote(noteA5, HN + QN);
	playNote(noteA5, QN);
	playNote(noteC6, HN);
	playNote(noteA5, HN);
	playNote(noteB5, HN + QN);
	playNote(noteB5, QN);
	playNote(noteB5, HN + QN);
	playNote(Rest, QN);
	playNote(noteB5, HN + QN);
	playNote(noteB5, QN);
	playNote(noteD6, HN);
	playNote(noteB5, HN);
	playNote(noteC6, HN + QN);
	playNote(noteC6, QN);
	playNote(noteC6, HN);
	playNote(noteB5, QN);
	playNote(noteA5, QN);
	playNote(noteD5, WN);
	playNote(noteFs5, WN);
	playNote(noteG5, WN);
}

void playNote(int note, int duration)
// This custom function takes two parameters, note and duration to make playing songs easier.
// Each of the notes have been #defined in the notes.h file. The notes are broken down by
// octave and sharp (s) / flat (b).
{
	tone(buzzerPin, note, duration);
	delay(duration);
}
```

Learn Arduino

http://goo.gl/5Uv71f

[UPDATE 3/19/2016]

Controlling with one joystick felt kinda squirelly so I added a second
one then adjusted the programming so one joystick was used for
forward/backwards and the other for left right. This gave it much more
stability and made it more fun to drive.  Shortly after completing the
build Jeff Branson with sparkfun sent me some better joysticks so I
built a second shield.  Here is a video I shot part way into the second
build:


Here is a video of the redbot in action using the new and improved dual
joystick xbee controller!

