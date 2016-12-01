Title: Attendance Logger
Date: 2016-11-14
Category: Blog
Tags: Arduino, Projects, RTC, RFID
Author: Blaž Pongrac

<div class="jumbotron">

<div class="container-fluid">
<div row>
    <div class="col-sm-4">
    <img src="/images/attendance-logger/image_1.jpg"  class="img-rounded img-thumbnail">
    </div>
    <div class="col-sm-8">
        <p><h5>I made this project long time ago. It was build as proof of concept while working for local tech
        company. Since then I have used it to track my working hours on my personal projects. Here is how
        you can make one.</h5></p>

        <p><h5>Point of the project was to develop simple Attendance data logger which can log time of arrival, time
        of departure and calculate working hours and access to the data must be granted within same LAN.
        From that I conclude that I would need RTC (Real Time Clock) module and Ethernet shield. For
        identifying user I went for RFID module. I added LEDs and speaker for more user friendly functioning.</h5></p>

        <h4>To recreate this project, you'll need:</h4>
        <ul>
            <li><a href="https://www.amazon.com/gp/product/B00JTBMD7E/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00JTBMD7E&linkCode=as2&tag=hackerspacetech-20&linkId=e019c92af67ea61af617e81aa17c30d5">Arduino Mega 2560</a></li>
            <li><a href="https://www.amazon.com/gp/product/B00UUR8GJU/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00UUR8GJU&linkCode=as2&tag=hackerspacetech-20&linkId=0846e93d9644288acfee1498dfb7c5e3">DS1307 RTC module</a> (I used TinyRTC)</li>
            <li><a href="https://www.amazon.com/gp/product/B00AXVX5D0/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00AXVX5D0&linkCode=as2&tag=hackerspacetech-20&linkId=80368ee774a17a2048158c4503320a94">Ethernet shield</a>  (I used W5100)</li>
            <li><a href="https://www.amazon.com/gp/product/B014CLKOJE/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B014CLKOJE&linkCode=as2&tag=hackerspacetech-20&linkId=3ccdb0c4bbca230b0cd90cd50111d719">RFID shield</a>(I used RC522) and some tags; NFC module can be used instead</li>
            <li><a href="https://www.amazon.com/gp/product/B01F0TCXSW/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01F0TCXSW&linkCode=as2&tag=hackerspacetech-20&linkId=8206617fe1f806f6a18bbd0d8e637ab5">green and red LED</a> or two color LED (I am using two color 2 pins LED)</li>
            <li><a href="https://www.amazon.com/gp/product/B0185FGNWK/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0185FGNWK&linkCode=as2&tag=hackerspacetech-20&linkId=1e04088241310f3e56a02a198f438c2b">220 OHM resistors</a> for LEDs</li>
            <li><a href="https://www.amazon.com/gp/product/B00TX2Z4J8/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00TX2Z4J8&linkCode=as2&tag=hackerspacetech-20&linkId=4bfcb57047e2c7532ebe9c163ed42665">8-ohm speaker</a> or buzzer</li>
            <li><a href="https://www.amazon.com/gp/product/B00BPPTTU6/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00BPPTTU6&linkCode=as2&tag=hackerspacetech-20&linkId=82ba7916f18d2c8d02b599c06217e8be">9V PSU and DC connector</a></li>
            <li><a href="https://www.amazon.com/gp/product/B01HYHUEBQ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01HYHUEBQ&linkCode=as2&tag=hackerspacetech-20&linkId=d83a5aa9931efe51b29a10d462652e6e">Ethernet cable</a></li>
            <li><a href="https://www.amazon.com/gp/product/B004G605OA/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B004G605OA&linkCode=as2&tag=hackerspacetech-20&linkId=2a9ee9b8f40e70513710481f2d4c2301">microSD card</a></li>
            <li>project housing</li>
            <li>some wires to connect everything together</li>
       </ul>
    </div>
</div>
</div>


<div class="container-fluid">
<div row>
    <div class="col-sm-8">
<p><h5>Schematics are pretty simple. MicroSD card, Ethernet Shield and RC522 are using SPI interface with different CS pins, tinyRTC uses I2C interface and LEDs and speakers are controlled with digital pins. Project could be executed with Arduino UNO, but one can run out of available memory for the code. Arduino Mega 2560 was used instead. For connecting Ethernet Shield to Arduino Mega 2560 you can <a href="http://mcukits.com/2009/04/06/arduino-ethernet-shield-mega-hack">use this guide</a>. Because different modules can have different pinouts, I created table bellow so connecting everything together can be easier. Make sure Ethernet shield is inserted like on link above – only pins 13, 12 and 11 are bended away. Ethernet Shield and RC522 module are using same pins, because they both uses same SPI interface. This is something that can be dealt with simple Y wire (I made mine from breadboard wires).</h5></p>
    </div>
    <div class="col-sm-4">
    <img src="/images/attendance-logger/image_2.jpg" class="img-rounded img-thumbnail">
    </div>
</div>
</div>

<br>

<div class="container-fluid">
<div row>
    <div class="col-sm-6">
    <img src="/images/attendance-logger/image_3.jpg" class="img-rounded img-thumbnail">
    </div>
    <div class="col-sm-6">
    <img src="/images/attendance-logger/table.png" class="img-rounded img-thumbnail">
    </div>
</div>
</div>


<p><h5>Arduino code is build according to flow chart below. Program runs in loop. First step in the loop is to check RFID module. If module is sensing known tag, step two is in place – getting data from RTC module and storing it onto microSD card. Step three is performed when HTTP request is received. Data is collected from microSD card and it is combined with HTML/CSS code to be displayed in client’s browser.</h5></p>
<center>
<img src="/images/attendance-logger/flowchart.jpeg" class="img-rounded img-thumbnail">


<h4>Here is short video from first test of this device.</h4>

<iframe width="560" height="315" src="https://www.youtube.com/embed/qQ855Dht2_U" frameborder="0" allowfullscreen></iframe>
</center>
<h4>And here is the Arduino code.</h4>

```
/* RFID TAG READER
Author: vonPongrac

Short description: Program read RFID tags. If tags UID is not familiar, sets new user

Hardware: Arduino Mega 2560, LED, Buzzer, RFID module RC522 with tags

Arduino IDE v1.6.3

Copyrights by vonPongrac
*/
// Include librarys
#include <SPI.h>
#include <MFRC522.h>  // RFID module library
#include <RTClib.h>  // RTC library
#include <Wire.h>  // i2C/1-wire library
#include <SD.h>  // SD card library
#include <Ethernet.h>  // Etrhenret library

#define RST_PIN		6  // RST pin for RFID module
#define SS_PIN		7  // Slave Select pine for RFID module

MFRC522 mfrc522(SS_PIN, RST_PIN);  // define RFID reader class
RTC_DS1307 RTC;  // define RTC class

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; // MAC address 
IPAddress ip(192, 168, 1, 177); // IP address
EthernetServer server(80); // define server class in port 80 - HTTP port

int buzzer = 8;  // speaker or buzzer on pin 8
int led_pos = 3; // green LED on pin 3
int led_neg = 2; // red LED on pin 2
String UID_tagA = "856a8b45";  // UID of tag that we are using
unsigned int MinsA = 0, HoursA = 0;  // working minutes and hours for tag A
String readTag = "";  
int readCard[4];
short UIDs_No = 1;
boolean TimeFlag[2] = {false, false};
DateTime arrival[2];  // tiem class for arrival
DateTime departure[2];  // time class for departure
int LastMonth=0;  // working hours till now in a month
char DataRead=0;

// Declaration of the functions
void redLED(); // red LED on
void greenLED(); // green LED + buzzer on
int getID();  // read tag
boolean checkTag();  // check if tag is unknown
void errorBeep();  // error while reading (unknown tag)
void StoreData();  // store data to microSD

File myFile; // class file for reading/writing to file on SD card


// SETUP
void setup() {
//  Serial.begin(9600); // for testing and debugging
  SPI.begin();  // run SPI library first; if not, RFID will not work
  mfrc522.PCD_Init();  // initializing RFID, start RFID library
  Wire.begin();  // start i2c library; if not, RTC will not work
  RTC.begin();  // start RTC library
  RTC.adjust(DateTime(__DATE__, __TIME__));  // set RTC time to compiling time
  Ethernet.begin(mac, ip);  // start Ethernet library 
  server.begin();  // start server 
//  Serial.print("server is at ");
//  Serial.println(Ethernet.localIP());
  SD.begin(4);  // start SD library
// setting DI/O
  pinMode(led_pos, OUTPUT);
  pinMode(led_neg, OUTPUT);
}

// MAIN PROGRAM
void loop() {
  int succesRead = getID(); // read RFID tag
  if(succesRead==1){ // if RFID read was succesful
    //greenLED();
    if (checkTag()){ // if tag is known, store data
      greenLED();
      StoreData();
    } else { // beeb an error; if new tag, then exit
      errorBeep();
    }
  } else {
    redLED();
  }
  // Web server
  EthernetClient client = server.available();  // check for HTTP request
  if (client) { // if HTTP request is available
//    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
 //       Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
        //  client.println("Refresh: 10");  // refresh the page automatically every 5 sec
          client.println();
          client.println("<!DOCTYPE html>");
          client.println("<html><head><title>Office Atendance Logger</title><style>");
          client.println(".jumbotron{margin: 1% 3% 1% 3%; border: 1px solid none; border-radius: 30px; background-color: #AAAAAA;}");
          client.println(".dataWindow{margin: 1% 3% 1% 3%; border: 1px solid none; border-radius: 30px; background-color: #AAAAAA;padding: 1% 1% 1% 1%;}");
          client.println("</style></head><body style=\"background-color: #E6E6E6\">");
          client.println("<div class=\"jumbotron\"><div style=\"text-align: center\"> <h1>  Office Atendance Logger </h1> </div> ");
          client.println("</div><div class=\"dataWindow\"><div style=\"text-align: center\"> <h2> User A </h2>");
          myFile = SD.open("A.txt");
          if(myFile){
            
            while(myFile.available()){
                client.print("<p>");
                while(DataRead != 59){
                  DataRead = (char)myFile.read();
                  client.print(DataRead);
            //      client.print(myFile.read());
                }
                client.println("</p>");
                DataRead = 0;
            }  
            
            myFile.close();
          }
          client.println("</div></body></html>");    
          break;     
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        }
        else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
//    Serial.println("client disconnected");
  }   
  delay(1000);
}

// FUNCTIONS
void redLED(){ // red LED on, green LED off
  digitalWrite(led_pos, LOW);
  digitalWrite(led_neg, HIGH);
}

void greenLED(){ // red LED off, green LED on
  digitalWrite(led_pos, HIGH);
  digitalWrite(led_neg, LOW);
  tone(buzzer, 440, 50); // sound; frequency of tone: 440 Hz, duration of tone: 50 ms
}

boolean checkTag(){ // check if tag is unknown
  if(readTag == UID_tagA){UIDs_No = 1; return true;}
//  else if(readTag == UID_tagB){UIDs_No = 2; return true;}
  else {return false;}
}

void errorBeep(){ // error option
  digitalWrite(led_pos, LOW);
  digitalWrite(led_neg, LOW);
  delay(150);
  digitalWrite(led_neg, HIGH);
  tone(buzzer, 440, 50);
  delay(150);
  digitalWrite(led_neg, LOW);
  delay(150);
  digitalWrite(led_neg, HIGH);
  tone(buzzer, 440, 50);
}

int getID() { // Read RFID
    // Getting ready for Reading PICCs
  if ( ! mfrc522.PICC_IsNewCardPresent()) { //If a new PICC placed to RFID reader continue
    return 0;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {   //Since a PICC placed get Serial and continue
    return 0;
  }
  // There are Mifare PICCs which have 4 byte or 7 byte UID care if you use 7 byte PICC
  // I think we should assume every PICC as they have 4 byte UID
  // Until we support 7 byte PICCs
//  Serial.println(F("Scanned PICC's UID:"));
  readTag = "";
  for (int i = 0; i < 4; i++) {  //
    readCard[i] = mfrc522.uid.uidByte[i];
//    Serial.print(readCard[i], HEX);
    readTag=readTag+String(readCard[i], HEX);
  }
  // Serial.println(readTag);
//  Serial.println("");
  mfrc522.PICC_HaltA(); // Stop reading
  return 1;
}

void StoreData(){ // calculate and store data to SD card
  DateTime time = RTC.now(); // read time from RTC
  if(LastMonth != time.month()){ // check if there is a new month
    LastMonth = time.month();
    SD.remove("hoursA.txt");
  }
  switch(UIDs_No){ // this is set for multiple tags, as of right now is made only for one tag
    case 1:
      if(TimeFlag[0]){ // departure
        departure[0] = time;  // save departure time
        // calculate working hours and minutes
        int dh = abs(departure[0].hour()-arrival[0].hour()); 
        int dm = abs(departure[0].minute()-arrival[0].minute()); 
        unsigned int work = dh*60 + dm; // working hours in minutes
        MinsA = MinsA + work; // add working hours in minutes to working hours from this month
        HoursA = (int)MinsA/60; // calculate working hours from minutes
        myFile = SD.open("A.txt", FILE_WRITE); // open file with history and write to it
        if(myFile){ // format = " MM-DD-YYYY hh:mm (arrival), hh:mm (departure), hh (working hours today), hh (working hours this month);
          myFile.print(arrival[0].month(),DEC);
          myFile.print("-");
          myFile.print(arrival[0].day(),DEC);
          myFile.print("-");
          myFile.print(arrival[0].year(),DEC);
          myFile.print(" ");
          myFile.print(arrival[0].hour(),DEC);
          myFile.print(":");
          myFile.print(arrival[0].minute(),DEC);
          myFile.print(", ");
          myFile.print(departure[0].hour(),DEC);
          myFile.print(":");
          myFile.print(departure[0].minute(),DEC);
          myFile.print(", ");
          myFile.print(dh,DEC);
          myFile.print(":");
          myFile.print(dm,DEC);
          myFile.print(", ");
          myFile.print(HoursA,DEC);
          myFile.print(";");
          myFile.close();
        }
        TimeFlag[0] = false; // set time flag to false
      } else { // arrival; 
        arrival[0] = time;  // save time of arrival 
        TimeFlag[0] = true;  // set time flag to true
      }
      break;  
  }
}
```

<a href="http://www.instructables.com/id/Arduino-attendence-logger/" target="_blank">Visit project’s homepage for more information.</a>

</div>