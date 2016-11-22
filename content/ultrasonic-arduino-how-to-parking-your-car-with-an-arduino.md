Title: UltraSonic Arduino How To - Parking your car with an Arduino
Date: 2015-11-21 13:28
Category: Blog
Tags: Arduino, UltraSonic, Tutorials
Author: David Riewe

![Back Up Helper](/images/utrasonic-carparker.png)

Using a Maxbotix Range Finder, Kevin Dahhar show you how to make a circuit that helps you back your car up into the garage, and put the Arduino into a super low power sleep when the circuit is not needed.

The Arduino only runs off of batteries and because it is kept in the super low power sleep mode the batteries last for months.

Only when the garage door is opened will the Arduino turn on due to the garage light activating a photocell and transistor circuit that signals an interrupt on the Arduino.

###The video below is long but well worth the watch
<iframe width="560" height="315" src="https://www.youtube.com/embed/U4D_c3fflLU" frameborder="0" allowfullscreen></iframe>

```
// Back up Helper, by Kevin Darrah v4

#include <SoftwareSerial.h>// to read the data fron the range finder on any digital pin

SoftwareSerial sonar(5, 6); // RX, TX   //we're only using the RX pin (5), so who cares about the TX pin

int huns, tens, ones, distance, returnbyte, sonar_data, i; //blah blah variables

//************CHANGED FROM VIDEO************
unsigned long time_start;//changed to unsigned long (allows to count up to 32bits-1 positive)


void wake_up(){}//  This routine does nothing but is needed by the interrupt to wake the arduino up

void setup(){ //set up stuff
 
  
  Serial.begin(9600);// for debugging and viewing distances
  pinMode(2, INPUT);//interrupt pin off of CDS
  
  // Common Anode RGB LED so writing LOW turns it ON
  pinMode(3, OUTPUT);//GREEN
  pinMode(4, OUTPUT);//RED
  pinMode(6, OUTPUT);//BLUE
  digitalWrite(3, HIGH);//off
  digitalWrite(4, HIGH);//off
  digitalWrite(6, HIGH);//off
  pinMode(7, OUTPUT);//Sonar Activate, goes to power pin of range finder
  digitalWrite(7, HIGH);//turn on range finder
   sonar.begin(9600);//start listening to range finder
   
}//setup

void go_to_sleep(){// put the arduino to sleep when called
  digitalWrite(7, LOW);//turn off range finder
   sonar.end();// IMPORTANT!  you have to stop the software serial function before sleep, or it won't sleep!
   
   // attach the interrupt on INT0 or digital pin 2, call wake_up, and do it when the pin falls from 5V to 0V
   attachInterrupt(0, wake_up, FALLING);
   
   SMCR = B00000101;//Sleep mode control register, Power Down mode and Enable Sleep
   __asm__  __volatile__("sleep");// In line assembler to execute the sleep function
  //once digital pin 2 Falls, from seeing light, the program will resume here after waking up
  
   SMCR = B00000100;// turn off bit 0 to disable the ability to sleep
   detachInterrupt(0);//turn off the interrupt, so the program doesn't go crazy when awake
   delay(1000);// let everybody get up and running for a sec
    digitalWrite(7, HIGH);//turn on the range finder
    delay(1000);//let it wake up for a sec, it goes through some self calibration stuff before its ready
    sonar.begin(9600);//start listing to the range finder
  for(i=0; i<10; i++){//flash the Blue LED letting us know everybody is ready to go
  digitalWrite(6, LOW);
  delay(50);
  digitalWrite(6, HIGH);
  delay(50);
}

//time stamp the free running timer, so we know how long we are awake for, and go back to sleep after a certain time
time_start= millis();
}//sleep over  


void loop(){// main loop

//while 1 loop here, so that we are continuously reading the range finder trying to get data, until we see an 82, more on this later
while(1){
  sonar_data=sonar.read();//read everything it sees, even garbage
  if(sonar_data==82){// as soon as we see an 82, we can read the next 4 bytes
  // an integer 82 is equal to the ASCII character R
  
 //the next 3 bytes will be ASCII characters representing the hundreds, tens, and ones place of the distance
 // the 4th byte will be a carriage return, (integer 13), we use it to check the validity of the data
  delay(20);//let the buffer fill up
  huns= sonar.read();//hundreds
  //delay(2);
  tens= sonar.read();//tens
  //delay(2);
  ones= sonar.read();//ones
  //delay(2);
  returnbyte= sonar.read();//carriage return
  
  if(returnbyte==13){// only use the data if we get the right carriage return
  //since the data comes in as ASCII characters, the integer value will not correspond to the character
  //looking at an ASCII table we see that an integer 48 is equal to an ASCII 0, which is why we subtract 48 from each value we read

    huns= (huns-48)*100;//cut off the ASCII 48, then multiply by 100
  //delay(5);
  tens= (tens-48)*10;//cut off the ASCII 48, then multiply by 10
  //delay(5);
  ones= (ones-48);//cut off the ASCII 48
    distance = huns+tens+ones;//add em all up to get the actual distance in INCHES
  Serial.print(distance); //print it out to the computer for debugging
  Serial.println(" inches");
}
  break;//we got good data so break the while loop
  }
}//the while loop


//DISTANCE CHECKER part of code
if(distance>36){//  When we're really far away light only the GREEN LED
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
  }
    else
    if(distance>12  && distance<=36){// When we get a little closer, light both GREEN and RED to make YELLOW
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
    }
  else
    if(distance<=12){//When we're close, flash the RED LED
      
  digitalWrite(3, HIGH);
  digitalWrite(4, LOW);    
  delay(25);
   digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  delay(25);
   digitalWrite(3, HIGH);
  digitalWrite(4, LOW); 
  
    }
    
    
    
    //check to see if our total awake time is greater than 60,000, 60sec, then start to go to sleep

    //**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG
    
    // GREAT BUG CATCH FOUND BY Jurriaan Petersen
    // If you time stamped time_start with millis, as millis was getting close to its overflow time of 49.71 days
    // the check for millis()-time_start>60000 could never go true, therefore never allowing the arduino to sleep
    
    //Here's a quick fix
    if (millis()-time_start<0) // means we had a roll over since time_start is greater than millis
    time_start=0;
    //**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG**BUG   
    
    if(millis()-time_start>60000){
      
     //LEDS OFF
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  
  //FLASH BLUE LED
  for(i=0; i<10; i++){
  digitalWrite(6, LOW);
  delay(50);
  digitalWrite(6, HIGH);
  delay(50);
}
 //CALL THE SLEEP FUNCTION
 go_to_sleep();
      }
}//loop
```