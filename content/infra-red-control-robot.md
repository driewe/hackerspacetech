Title: Infra Red Controlled Robot
Date: 2015-11-02
Category: Blog
Tags: Arduino, Robot, infrared, Tutorials
Author: David Riewe

This is the first experiment I tried with the board of education arduuino robot shield.  The experiment involves using [Ken Shirrifs IR Library](https://github.com/z3t0/Arduino-IRremote) along with any IR Receiver.  In order to use this example you will first need to determine what the IR codes are for the transmitter you wish to use.  The examples/IRrecvDemo sketch in the library provides a simple example of how to receive codes.  See [Kens Blog](http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html) for more info.

<iframe width="560" height="315" src="https://www.youtube.com/embed/fsBSJAT_SEQ" frameborder="0" allowfullscreen></iframe>

The motors on the robot are 360 degree servos that are controlled by sending them a digital pulse ranging in duration from 1300 to 1700 microseconds every 20milliseconds.  The width of the pulse determines the speed and direction they rotate.  1500 would be no motion at all, 1300 full speed counter clockwise and 1700 full speed counter clockwise.  While this is modifying the width of the pulse it is not the same as the PWM functions found in the Arduino library.

When polling for commands from the IR receiver I found that that this particular remote requires me give it at least 175 ms before attempting to read its next transmission.   That, combined with the IR remote being single channel makes for a choppy RC because within 200 ms the servos have already repeated the last command 10 times.

Oh and if you are wondering why no beeping from the Robot it is because the tone function is unable to access TIMER2 because it is being used by the IR Library   The servo library uses TIMER1.


[Source Code](https://github.com/driewe/RemoteControlRobotIR/blob/master/sourcecode/RemoteRobotWithFunctions.ino)

```
/*
 * Remote control Robot
 *
 */

#include <IRremote.h>
#include <Servo.h> 


int RECV_PIN = 2;

/* this is for the old clarion remote controller I am using
 * the button names correspond with the names on the controller
 * but not with the function I will be using them for.  Hence
 * names like "backbutton" for what will be used to command
 * the robot to turn left
 */
 
const long backbutton = 0x6106C03F;		// Turn Left
const long uparrow = 0x6106D827;		// Forward
const long menu = 0x6106D02F;			// Turn Right
const long leftarrow = 0x61066897;	// Spin Left
const long ok = 0x610610EF;			// pause
const long rightarrow = 0x6106E817;	// Spin Right
const long downarrow = 0x6106B847;	// backwards

IRrecv irrecv(RECV_PIN);
decode_results results;
Servo servoLeft;        // Declare Left Servo
Servo servoRight;       // Declare Right Servo
int lastcommand;


void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if (results.value == backbutton)    // Turn Left
    {
      TurnLeft(20);
    } 
    else if (results.value == uparrow)  // Move Forward, ramp 
    {
      MoveForward(200); 
    }
    else if (results.value == menu)    // Turn Right
    {
      TurnRight(20);
    }
    else if (results.value == leftarrow)  // Spin Left
    {
      SpinLeft(40);
    }
    else if (results.value == ok)   // do nothing
    {
      StayStill();
    }
    else if (results.value == rightarrow)   // Spin right
    {
      SpinRight(40);
    }
    else if (results.value == downarrow)   // move backwards
    {
      MoveBackwards(200);
    }
  } 
  else 
  {
    StayStill();
  }
  irrecv.resume();
  delay(200);
}


void MoveForward(int msTime)
{
  maneuver(100, 100, msTime);
}

void MoveBackwards(int msTime)
{
  maneuver(-100,-100, msTime);
}

void SpinRight(int msTime)
{
  maneuver(100, -100, msTime);
}

void TurnRight(int msTime)
{
  maneuver(100, 0, msTime);
}

void StayStill()
{
  maneuver(0, 0, 20);
}

void SpinLeft(int msTime)
{
  maneuver(-100, 100, msTime);
}
void TurnLeft(int msTime)
{
  maneuver(0, 100, msTime);
}

void maneuver(int speedLeft, int speedRight, int msTime)
{
  // speedLeft, speedRight ranges: Backward  Linear  Stop  Linear   Forward
  //                               -200      -100......0......100       200
  servoLeft.writeMicroseconds(1500 + speedLeft);   // Set Left servo speed
  servoRight.writeMicroseconds(1500 - speedRight); // Set right servo speed
  if(msTime==-1)                                   // if msTime = -1
  {
    servoLeft.detach();                            // Stop servo signals
    servoRight.detach();
  }
  delay(msTime);                                   // Delay for msTime
}
```
