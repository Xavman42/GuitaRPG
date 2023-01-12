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

## Technical requirements
See tech rider for a stage plot.

I will need two microphones: a pair of SM81s, a pair of KM 184s, or a pair of similar microphones.
Optimally, these will be provided by the venue, but I can provide these if necessary.
These microphones are routed into an audio interface. 
A Scarlett 2i2 would work, but anything that can plug into my Linux laptop via USB is fine.
(I will bring the Scarlett as a backup.) The interface is connected to my laptop via USB. 
My computer sends processed audio back to the interface and out to the house mix.
My laptop also sends a video signal via HDMI to a projector or television for the audience to see.
Depending on the size of the space, it may be a good idea to send the unprocessed microphone signals to the house mix 
as well.
If possible, I would like a mono mix of the house mix sent to me for in-ear monitoring.


## Duration

Minimum duration ~ 4 minutes

No maximum duration

I will perform this piece for 10 minutes.

## How to play

After installing dependencies listed in requirements.txt, run the python file `NeoScore/main.py`.
Press the `a` key to manually decide which direction to go.

I will update this later to include how to get the SuperCollider part up and running.