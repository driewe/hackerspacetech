Title: Adafruit Wave Shield
Date: 2016-01-03 01:47
Category: Blog
Tags: Arduino, Reviews
Author: David Riewe



![wave Shield](/images/waveshield.jpg)

Here is a shield for Arduino that makes adding quality sound to your products easy.

It can play up to 22KHz, 12bit uncompressed audio files of any length. 

It's low cost, available as an easy-to-make kit. 

It has an onboard DAC, filter and op-amp for high quality output. 

Audio files are read off of an SD/MMC card, which are available at nearly any store. 

Volume can be controlled with the onboard thumbwheel potentiometer.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6pQ4D-DPh3Q" frameborder="0" allowfullscreen></iframe>
*Click on the play button to watch a demo of the wave shield playing
assorted audio through a small speaker.*

The shield comes with an Arduino library for easy use; simply drag uncompressed wave files onto the SD card and plug it in. Then use the library to play audio when buttons are pressed, or when a sensor goes off, or when serial data is received, etc. Audio is played asynchronously as an interrupt, so the Arduino can perform tasks while the audio is playing.

Can play any uncompressed 22KHz, 12bit, mono Wave (.wav) files of any
size. While it isnt CD quality, it is certainly good enough to play
music, have spoken word, or audio effects.

Output is mono, into L and R channels, standard 3.5mm headphone jack and
a connection for a speaker that is switched on when the headphones are
unplugged.

Files are read off of [FAT16 formatted SD/MMC card](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino/sd-card).

Included library makes playing audio easy.

While the shield has been tested and works well, here are some points to keep in mind:

-  The audio playback library uses 10K of flash - so if you want to use
   an NG arduino, you'll need to upgrade to an Atmega168 chip.
-  About 600 bytes of SRAM are used to buffer the audio and keep track
   of file data, so RAM-heavy projects may not work well.
-  The shield can't play MP3, WMA, Ogg or other compressed audio files.
   It can only play uncompressed PCM/WAV files. [Converting audio to WAV format](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino/convert-files) is very easy, and is often the default format for many audio
   programs.
-  Files are stored as 8.3 name format, and can only be placed in the
   root directory. That means you can only have ~512 files (but they can
   be any size).

Ideas for what you can use it for...

-  Make a portable audio player
-  Use the AT&T text-to-speech site to make snippets of speech that you
   string together for a talking project, like..
-  Talking temperature sensor
-  Talking clock
-  Interfaces for sight-impared people
-  Doorbell that plays a cool tune
-  Jukebox/music-box that plays a song when its opened, or a coin is
   inserted
-  Security system that warns the intruder
-  Audio looper for musical effects and performances
-  Synthesizer with different sounds
-  Really freaky halloween props that scream
-  Display (like a point-of-sale box) that you can plug into to hear the
   message

