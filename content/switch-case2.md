Title: Switch Case 2: A second switch-case example, showing how to take different actions based on the characters received in the serial port
Date: 2016-11-09
Category: Blog
Tags: Arduino, Programming, Tutorials
 <div class="jumbotron">
An if statement allows you to choose between two discrete options, TRUE or FALSE. When there are more than two options, you can use multiple if statements, or you can use the switch statement. Switch allows you to choose between several discrete options.

This tutorial shows you how to use switch to turn on one of several different LEDs based on a byte of data received serially. The sketch listens for serial input, and turns on a different LED for the characters a, b, c, d, or e.

####Hardware Required
* Arduino
* 5 LEDs
* 5 220 ohm resistors
* hook-up wires
* breadboard

####Circuit
Five LEDs are attached to digital pins 2, 3, 4, 5, and 6 in series through 220 ohm resistors.

To make this sketch work, your board must be connected to your computer. In the Arduino IDE open the serial monitor and send the characters a, b, c, d, or e to lit up the corresponding LED, or anything else to switch them off.

![Circuit](http://www.arduino.cc/en/uploads/Tutorial/switchCase2_bb.png)

![Arduino](http://www.arduino.cc/en/uploads/Tutorial/SwitchCase2.png)

####Code 
```
/*
  Switch statement  with serial input

 Demonstrates the use of a switch statement.  The switch
 statement allows you to choose from among a set of discrete values
 of a variable.  It's like a series of if statements.

 To see this sketch in action, open the Serial monitor and send any character.
 The characters a, b, c, d, and e, will turn on LEDs.  Any other character will turn
 the LEDs off.

 The circuit:
 * 5 LEDs attached to digital pins 2 through 6 through 220-ohm resistors

 created 1 Jul 2009
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SwitchCase2
 */

void setup()
{
    // initialize serial communication:
    Serial.begin(9600);
    // initialize the LED pins:
    for (int thisPin = 2; thisPin < 7; thisPin++)
    {
        pinMode(thisPin, OUTPUT);
    }
}

void loop()
{
    // read the sensor:
    if (Serial.available() > 0)
    {
        int inByte = Serial.read();
        // do something different depending on the character received.
        // The switch statement expects single number values for each case;
        // in this exmaple, though, you're using single quotes to tell
        // the controller to get the ASCII value for the character.  For
        // example 'a' = 97, 'b' = 98, and so forth:

        switch (inByte)
        {
            case 'a':
                digitalWrite(2, HIGH);
                break;
            case 'b':
                digitalWrite(3, HIGH);
                break;
            case 'c':
                digitalWrite(4, HIGH);
                break;
            case 'd':
                digitalWrite(5, HIGH);
                break;
            case 'e':
                digitalWrite(6, HIGH);
                break;
             default:
                // turn all the LEDs off:
                for (int thisPin = 2; thisPin < 7; thisPin++)
                {
                    digitalWrite(thisPin, LOW);
                }
        }
    }
}
```
</div>