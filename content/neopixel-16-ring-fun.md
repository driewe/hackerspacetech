Title: NeoPixel 16 Ring Fun
Date: 2016-04-18 16:50
Category: Blog
Tags: Arduino, NeoPixel, Tutorials
Author: David Riewe

![alt text](https://3.bp.blogspot.com/-2PBh6CGux-Y/Vwpq4qeIJyI/AAAAAAAAs-c/2e9IeCQiPMU2emHh5uIRqNGg7vW0GS2TA/s320/neopixel1.PNG "Logo Title Text 1")

NeoPixels are fun and amazing. In my project I connected 4 of the [AdaFruit NeoPixel](https://www.amazon.com/gp/product/B00R5CDGWA/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00R5CDGWA&linkCode=as2&tag=teammilleniumonl&linkId=a3964d7a35bee2d107a7f7cbf9d2a1ca) - 16 RGBW Leds together. What caught my attention and curiosity was that you can control each of these RGBW Leds using just one wire.This feat is accomplished with a very timing-specific protocol. Since the protocol is very sensitive to timing, it requires a real-time microconroller such as an AVR, Arduino, PIC, mbed, etc. It cannot be used with a Linux-based microcomputer or interpreted microcontroller such as the netduino or Basic Stamp. How the protocol works can be found in the WS2812 data sheet. For each RGB Led a stream of 24 bits will be sent, 8 bits for each color.
 
The value of each bit, 1 or 0, is determined by the timing of the square wave. A logic 0 is represented by a signal that is high for .35 mircorseconds followed by a low of .8 microseconds A logic 1 is represented by a signal that is high for .7 microseconds followed by a low for  6 microseconds


![alt text](https://3.bp.blogspot.com/-6OQyXqafxWA/Vwpra6QcNCI/AAAAAAAAs-k/q0cHRah4wlMCPyYk42UGNCeprTaNAFTZw/s320/neopixel2.PNG)

![alt text](https://2.bp.blogspot.com/-hHm9ooAzN3s/Vwprq8GLv6I/AAAAAAAAs-o/p9eLXHlKx5sQ2t2pAPEo0RxhZA-cFfcBQ/s640/neopixel3.PNG)

So just in the process of updating a [16 LED RGB ring](https://www.amazon.com/gp/product/B01F7YY8CY/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01F7YY8CY&linkCode=as2&tag=teammilleniumonl&linkId=b3e4158d3fd6ad50e3b40af3a61248c6) you will be sending 48 bytes of data, 3 bytes for each leds RGB value. Each byte contains a value of 0-255 indicating the value of intensity for that particularcolor (Red, Green or Blue).

Looking at the diagram above the transmission starts with D1 receiving the first 24 bits. After that D1 will pass subsequent bits on to D2. Once D2 receives it's 24 it starts passing subsequent bits onto D3.
Note that this is different than usual shift register operation. The passing on will continue until the data line is held low for 50 microseconds. Holding the data line low for 50 microseconds is a reset code indicating next sequence is for the WS2812 to process.

![alt text](https://1.bp.blogspot.com/-QhLMhMLKEVU/VwpvO5FCZqI/AAAAAAAAs-4/yILvmTcCe3o7a_GSBh-shg_b6eMqPtHWA/s640/neopixel4.PNG)"logo"

Generating the timing above is no easy feat and requires some very skilled hand-tuned assembly code that issues data to the LED drivers at a specific rate. Fortunately, Phil Burgess / Paint Your Dragon, wrote a library for Adafruit that allows us mortals to control these beauties.

Below is the code and a video of my setup. Codebender allows you to peek into the library files by holding down the CTRL key while clicking on the library header file. In this case you would hold the CTRL key and click on "Adafruit_NeoPixel.h". This will open a new tab with the NeoPixel library and related files. From there look on the left hand side and select the Adafruit_NeoPixel.cpp file to explore and learn more about this awesome library. Don't be afradid If you have any questions please [feel free to ask.](http://www.davidriewe.com/p/contact-me.html)
<div style="text-align: center;">

<iframe width="560" height="315" src="https://www.youtube.com/embed/w97qFRa2lRo" frameborder="0" allowfullscreen></iframe>
</div>

```
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PIN 6

#define NUM_LEDS 64

#define BRIGHTNESS 50

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRBW + NEO_KHZ800);

int gamma[] =
{
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
	1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
	2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
	5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
	10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
	17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
	25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
	37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
	51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
	69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
	90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 109, 110, 112, 114,
	115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 133, 135, 137, 138, 140, 142,
	144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 167, 169, 171, 173, 175,
	177, 180, 182, 184, 186, 189, 191, 193, 196, 198, 200, 203, 205, 208, 210, 213,
	215, 218, 220, 223, 225, 228, 231, 233, 236, 239, 241, 244, 247, 249, 252, 255
};
void setup()
{
	Serial.begin(115200);
	strip.setBrightness(BRIGHTNESS);
	strip.begin();
	strip.show(); // Initialize all pixels to 'off'
}
void loop()
{
	// Some example procedures showing how to display to the pixels:
	colorWipe(strip.Color(255, 0, 0), 5); // Red
	colorWipe(strip.Color(0, 255, 0), 5); // Green
	colorWipe(strip.Color(0, 0, 255), 5); // Blue
	colorWipe(strip.Color(0, 0, 0, 255), 5); // White

	whiteOverRainbow(20, 10, 7);
	whiteOverRainbow(20, 10, 7);
	whiteOverRainbow(20, 10, 7);
	pulseWhite(5);

	// fullWhite();
	// delay(2000);

	rainbowFade2White(3, 10, 1);
}
// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait)
{
	for(uint16_t i = 0; i < strip.numPixels(); i++)
	{
		strip.setPixelColor(i, c);
		strip.show();
		delay(wait);
	}
}
void pulseWhite(uint8_t wait)
{
	for(int j = 0; j < 256 ; j++)
	{
		for(uint16_t i = 0; i < strip.numPixels(); i++)
		{
			strip.setPixelColor(i, strip.Color(0, 0, 0, gamma[j] ) );
		}
		delay(wait);
		strip.show();
	}

	for(int j = 255; j >= 0 ; j--)
	{
		for(uint16_t i = 0; i < strip.numPixels(); i++)
		{
			strip.setPixelColor(i, strip.Color(0, 0, 0, gamma[j] ) );
		}
		delay(wait);
		strip.show();
	}
}


void rainbowFade2White(uint8_t wait, int rainbowLoops, int whiteLoops)
{
	float fadeMax = 100.0;
	int fadeVal = 0;
	uint32_t wheelVal;
	int redVal, greenVal, blueVal;

	for(int k = 0 ; k < rainbowLoops ; k ++)
	{

		for(int j = 0; j < 256; j++) // 5 cycles of all colors on wheel
		{

			for(int i = 0; i < strip.numPixels(); i++)
			{

				wheelVal = Wheel(((i * 256 / strip.numPixels()) + j) & 255);

				redVal = red(wheelVal) * float(fadeVal / fadeMax);
				greenVal = green(wheelVal) * float(fadeVal / fadeMax);
				blueVal = blue(wheelVal) * float(fadeVal / fadeMax);

				strip.setPixelColor( i, strip.Color( redVal, greenVal, blueVal ) );

			}

			//First loop, fade in!
			if(k == 0 && fadeVal < fadeMax - 1)
			{
				fadeVal++;
			}

			//Last loop, fade out!
			else if(k == rainbowLoops - 1 && j > 255 - fadeMax )
			{
				fadeVal--;
			}

			strip.show();
			delay(wait);
		}

	}
	delay(500);
	for(int k = 0 ; k < whiteLoops ; k ++)
	{
		for(int j = 0; j < 256 ; j++)
		{
			for(uint16_t i = 0; i < strip.numPixels(); i++)
			{
				strip.setPixelColor(i, strip.Color(0, 0, 0, gamma[j] ) );
			}
			strip.show();
		}
		delay(2000);
		for(int j = 255; j >= 0 ; j--)
		{
			for(uint16_t i = 0; i < strip.numPixels(); i++)
			{
				strip.setPixelColor(i, strip.Color(0, 0, 0, gamma[j] ) );
			}
			strip.show();
		}
	}
	delay(500);
}
void whiteOverRainbow(uint8_t wait, uint8_t whiteSpeed, uint8_t whiteLength )
{
	if(whiteLength >= strip.numPixels()) whiteLength = strip.numPixels() - 1;
	int head = whiteLength - 1;
	int tail = 0;
	int loops = 3;
	int loopNum = 0;

	static unsigned long lastTime = 0;
	while(true)
	{
		for(int j = 0; j < 256; j++)
		{
			for(uint16_t i = 0; i < strip.numPixels(); i++)
			{
				if((i >= tail && i <= head) || (tail > head && i >= tail) || (tail > head && i <= head) )
				{
					strip.setPixelColor(i, strip.Color(0, 0, 0, 255 ) );
				}
				else
				{
					strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
				}

			}

			if(millis() - lastTime > whiteSpeed)
			{
				head++;
				tail++;
				if(head == strip.numPixels())
				{
					loopNum++;
				}
				lastTime = millis();
			}

			if(loopNum == loops) return;

			head %= strip.numPixels();
			tail %= strip.numPixels();
			strip.show();
			delay(wait);
		}
	}

}
void fullWhite()
{

	for(uint16_t i = 0; i < strip.numPixels(); i++)
	{
		strip.setPixelColor(i, strip.Color(0, 0, 0, 255 ) );
	}
	strip.show();
}


// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait)
{
	uint16_t i, j;

	for(j = 0; j < 256 * 5; j++) // 5 cycles of all colors on wheel
	{
		for(i = 0; i < strip.numPixels(); i++)
		{
			strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
		}
		strip.show();
		delay(wait);
	}
}

void rainbow(uint8_t wait)
{
	uint16_t i, j;

	for(j = 0; j < 256; j++)
	{
		for(i = 0; i < strip.numPixels(); i++)
		{
			strip.setPixelColor(i, Wheel((i + j) & 255));
		}
		strip.show();
		delay(wait);
	}
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos)
{
	WheelPos = 255 - WheelPos;
	if(WheelPos < 85)
	{
		return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3, 0);
	}
	if(WheelPos < 170)
	{
		WheelPos -= 85;
		return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3, 0);
	}
	WheelPos -= 170;
	return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0, 0);
}

uint8_t red(uint32_t c)
{
	return (c >> 8);
}
uint8_t green(uint32_t c)
{
	return (c >> 16);
}
uint8_t blue(uint32_t c)
{
	return (c);
}
```

