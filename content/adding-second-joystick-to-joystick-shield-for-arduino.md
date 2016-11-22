Title: Adding Second Joystick to Joystick Shield for Arduino
Date: 2015-12-28 22:40
Category: Blog
Tags: Arduino, Projects
Author: David Riewe

![Joy Stick](/images/joystick.jpg)

Added a second joystick to the shield and use one for forward/back motion and the other for turning.  I find this setup gives better control.

Jeff Branson, from Sparkfun, saw my project on facebook and suggested I submit it to Sparkfun to be added to their project section.  I said I would if I could get some better quality joysticks, like the ones Sparkfun sells :-). I should be receiving those this week and will build up a nicer version and also add some additonal control buttons.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nJLt0zrsFyk" frameborder="0" allowfullscreen></iframe>

Below is a video of me driving the redbot using the dual joystick conroller.

<iframe width="560" height="315" src="https://www.youtube.com/embed/htI5ImI3H18" frameborder="0" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/IO01oVrnVDw" frameborder="0" allowfullscreen></iframe>

##Code for the redbot
```
/*****************************************************************
XBee_Remote_Control.ino

*****************************************************************/
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
##Code for the JoyStick Controller
```
/*****************************************************************
XBee_Remote_Controller.ino

*****************************************************************/
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
