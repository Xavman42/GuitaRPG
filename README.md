# GuitaRPG

## Description

GuitaRPG is an interactive 2-dimensional score through which the performer may freely navigate.
Taking inspiration from Role Playing Games (RPGs), the performer may move through regions of the score at their own 
pace, each region featuring its own distinct soundscape. 
Upon encountering a new region, the performer will be presented with a new sound or technique to explore on their 
instrument, accumulating sounds all the way until the climax at the end of the piece.
The more times a performer encounters a particular technique, the more they 'level-up' and unlock more variations of 
that technique.

The piece is ultimately a meditative sight-reading experience with elements of improvisation.
Even in a performance setting, this piece is being sightread, though individual elements must be rehearsed ahead of 
time.
This is an improvisatory piece in that the performer engages reactively with the electronic sounds, allowing them 
to influence the interpretation of the sight-read elements.
What differentiates this improvisation from many other improvisatory works is that memorization is not required;
the meandering form of the piece is determined by the performer in the moment, and the thing to play at any time is 
presented on screen.

## Demo
An early video-demo of this piece in video form can be found here:
https://youtube.com/watch?v=t3ycuHPp22I&feature=shares

The current working version of the code is stored here: 
https://github.com/Xavman42/GuitaRPG

## Program note

GuitaRPG is an interactive 2-dimensional score through which the performer may freely navigate.
Taking inspiration from Role Playing Games (RPGs), the performer may move through regions of the score at their own 
pace, each region featuring its own distinct soundscape. 
Upon encountering a new region, the performer will be presented with a new sound or technique to explore on their 
instrument, accumulating sounds all the way until the climax at the end of the piece.
The more times a performer encounters a particular technique, the more they 'level-up' and unlock more variations of 
that technique. 

This piece was commissioned by Craig Vear and the *Digiscore* research project, 
and created using the *neoscore* python library, developed principally by Andrew Yoon.


## 100-word biography
Xavier Davenport (b. 1995) writes music that is meticulously structured, technologically 
experimental, humorous, theatrical, often improvisatory, and sometimes entertaining. 

Born in Ohio, he attended Wittenberg University where he was awarded the Sara Krieg Music 
Scholarship, and later the Huebner Scholarship. In his four years as an undergraduate 
student, he obtained degrees in Chinese language & culture, physics, and music. He next 
obtained a master’s degree in electrophysics from the National Chiao-Tung University in 
2020, then another master's degree in music composition in 2022 from DePaul University. 
Davenport is now working towards a DMA at the University of Illinois at Urbana-Champaign.


## Duration

Minimum duration ~ 4 minutes

No maximum duration

I will perform this piece for 10 minutes.

## How to play

First, intall Python and SuperCollider. Following the procedures linked here is a good idea for the Python side of things: 
https://neoscore.org/getting_started.html
Be sure to install the Python dependencies listed in requirements.txt.

For SuperCollider, you can download here: 
https://supercollider.github.io/downloads.html
For assistance in learning how to navigate the SuperCollider IDE, check out at least the first tutorial here:
https://youtu.be/ntL8QDOhhL8

Open the file `SuperCollider/GuitaRPG.scd`, place your cursor somewhere between lines 4 and 117 and run that block of code.

Next, in the same SuperCollider file, place your cursor somewhere between lines 119 and 243 and run the second block of code. You should hear sounds now, though they may be faint.

Next, run `NeoScore/main.py`. Two screens should appear, one is the main score window and the other is a HUD to help with navigating the score.
With the main score window selected, press the `a` key to manually decide which direction to go. You are now playing the piece!

If you should wish to peruse all the symbols which can appear on the screen and read a short description of my interpretation of each symbol, just run `NeoScore/cells.py`.
