Title: MAX7219 8X8 Red Dot LED Matrix Kit
Date: 2015-11-20 01:52
Category: Blog
Tags: Arduino, 7219, 8x8, Matrix, Kit, Reviews
Author: David Riewe

![MAX7219 LED Matrix Kit](/images/8x8unassembled.png)

After reading up on Project #21: Creating an LED Matrix in [The Arduino Workshop](http://www.amazon.com/gp/product/1593274483/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1593274483&linkCode=as2&tag=davimakespa0e-20&linkId=ZO63GU2HQJNMIQ55)  I set out to find a 8x8 common cathode led matrix.  I saw this [MAX7219 8X8 Red Dot LED Matrix](http://www.amazon.com/gp/product/B013KVWCBK/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B013KVWCBK&linkCode=as2&tag=davimakespa0e-20&linkId=PRCVVIVUW7CZPMCZ) on Amazon and while I was looking to experiment with using two 74HC595's to control the rows and columns of the 8x8 matrix, this

[MAX7219](http://playground.arduino.cc/Main/MAX72XXHardware) chip that did it all caught my curiosity.  So I ordered the kit.  :-)

Amazon Prime delivered quickly and the kit was relatively easy to solder. Both the 8x8 display and the [MAX7219] (http://playground.arduino.cc/Main/MAX72XXHardware) are socketed so you can easily remove them if you want to use in  a different project.  From the looks of it the board can be easily cascaded with other devices to create larger displays.  John Boxall does exactly that in his book [The Arduino Workshop]() 

The [LedControl Arduino library](http://playground.arduino.cc/uploads/Main/LedControl.zip) has full support of the [MAX7219](http://playground.arduino.cc/Main/MAX72XXHardware) to control an 8x8 display.  The library does all the shifting out and multiplexing of row and column leds...All you do is tell it the and column of the led you would like to turn on or off!

One single [MAX7219](http://playground.arduino.cc/Main/MAX72XXHardware) can also control up to 8 7segment displays.  Unlike my prior example, where each 7 segment display is driven by an individual 74HC595, the MAX7219 multiplexes the 7 segment displays so that only one is on at a time.  This cuts the current usage and because of the persistence of vision it appears that all 8 digits are on constantly.

So here is a peek at my finished [MAX7219 8X8 Red Dot LED Matrix Kit](http://www.amazon.com/gp/product/B013KVWCBK/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B013KVWCBK&linkCode=as2&tag=davimakespa0e-20&linkId=PRCVVIVUW7CZPMCZ) running the test program.

<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/es18nvSmHFA" width="560"></iframe></div>

```
#include "LedControl.h" //  need the library
LedControl lc=LedControl(12,11,10,1); // 
// pin 12 is connected to the MAX7219 pin 1 - Data In
// pin 11 is connected to the CLK pin 13
// pin 10 is connected to LOAD pin 12
// 1 as we are only using 1 MAX7219
void setup()
{
    // the zero refers to the MAX7219 number, it is zero for 1 chip
    lc.shutdown(0,false);// turn off power saving, enables display
    lc.setIntensity(0,8);// sets brightness (0~15 possible values)
    lc.clearDisplay(0);// clear screen
}
void loop()
{
    for (int row=0; row<8; row++)
    {
        for (int col=0; col<8; col++)
        {
            lc.setLed(0,col,row,true); // turns on LED at col, row
            delay(25);
        }
    }
    for (int row=0; row<8; row++)
    {
        for (int col=0; col<8; col++)
        {
            lc.setLed(0,col,row,false); // turns off LED at col, row
            delay(25);
        }
    }
}

```


