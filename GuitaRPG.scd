(

SynthDef(\bpfsaw, {
	arg atk=2, sus=10, rel=3, c1=1, c2=(-1),
	freq=500, detune=0.2, pan=0,
	cfmin=500, cfmax=2000, rqmin=0.1, rqmax=0.2, amp=1, out=0;
	var sig, env;
	env = EnvGen.kr(Env([0,1,1,0],[atk,sus,rel],[c1,0,c2]),doneAction:2);
	sig = Saw.ar(freq * LFNoise1.kr(0.5,detune).midiratio);
	sig = BPF.ar(sig,
		LFNoise1.kr(0.2).exprange(cfmin, cfmax),
		LFNoise1.kr(0.1).exprange(rqmin, rqmax)
	);
	sig = Pan2.ar(sig, pan);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;



~plinky_wood = {Synth(
	\bpfsaw,
	[
		\freq, (1/32)*10.60+rrand(-1.0,1.0),
		\amp, 0.4,
		\cfmin, 50*20,
		\cfmax, 50*50,
		\rqmin, 0.005,
		\rqmax, 0.03,
		\pan, rrand(-1.0,1.0),
	],
);};



~scratchy_string = {Synth(
	\bpfsaw,
	[
		\freq, 4*10.60+rrand(-10.0,10.0),
		\amp, 0.2,
		\cfmin, 50*4,
		\cfmax, 50*50,
		\rqmin, 0.05,
		\rqmax, 0.3,
		\pan, rrand(-1.0,1.0),
	],
);};



x = OSCFunc( { | msg, time, addr, port |
	var synthType;

	synthType = msg[1].asString;
	synthType.postln;
	( "attempting to play synth" + synthType ).postln;
	case
	{ synthType == "plinky_wood"} {10.do(~plinky_wood)}
	{ synthType == "scratchy_string"} {10.do(~scratchy_string)}
	{ synthType == "Region_1_effect"} {~delSynth.set(\decay, 4)}
	{ synthType == "Region_2_effect"} {~delSynth.set(\decay, 40)}
	{ synthType == "Region_3_effect"} {~delSynth.set(\mix, -1);~sftSynth.set(\width, 2.0);};

}, "/print" );



//mic synthdef
(
SynthDef.new(\mic, {
	arg in=0, out=0, amp=1;
	var sig;
	sig = SoundIn.ar(in!2) * amp;
	Out.ar(out, sig);
}).add;
);

//pitch shift synthdef
(
SynthDef.new(\pitchshift, {
	arg in=0, out=0, mix(0.5), amp=1, width=0;
	var sig, shift1, shift2, shiftbal;
	sig = In.ar(in, 2);
	shift1 = PitchShift.ar(in: sig, pitchRatio: 1.3333+width);// SinOsc.kr(0.5).exprange(0.5, 1.5));
	shift2 = PitchShift.ar(in: sig, pitchRatio: 0.6667-width);
	shiftbal = XFade2.ar(inA: shift1, inB: shift2, pan: 0.5);
	sig = XFade2.ar(inA: sig, inB: shiftbal, pan: mix) * amp; //mixes the input and shift signals.
	Out.ar(out, sig);
}).add;
);

//delay synthdef
(
SynthDef.new(\delay, {
	arg in=0, out=0, mix=(0.5), decay=10, amp=1, delHz=0.26, delMin=0.20, delMax=0.26, addfactors=1;
	var sig, delay;
	sig = In.ar(in, 2);
	delay = CombL.ar(
		in: sig,
		maxdelaytime: 0.5,
		delaytime: Select.kr(addfactors > 0.5, [SinOsc.kr([delHz,delHz*0.9]),
			SinOsc.kr([delHz,delHz*0.9])
			+ SinOsc.kr(1.8*[delHz,delHz*0.9])
			+ SinOsc.kr(2.5*[delHz,delHz*0.9])
			+ SinOsc.kr(2.6*[delHz,delHz*0.9])].exprange(delMin,delMax)),
		decaytime: decay
	);
	sig = XFade2.ar(inA: sig, inB: delay, pan: mix) * amp; //mixes the input and delay signals.
	Out.ar(out, sig);
}).add;
);

//create busses
(
~sftBus = Bus.audio(s, 2);
~delBus = Bus.audio(s, 2);
~smpsftBus = Bus.audio(s, 2);
~smpdelBus = Bus.audio(s, 2);
);

//generate group order and turn on microphone
(
~micGrp = Group.new;
~sftGrp = Group.after(~micGrp);
~delGrp = Group.after(~sftGrp);

~micSynth = Synth(\mic, [\in, 0, \out, ~sftBus], ~micGrp);
~sftSynth = Synth(\pitchshift, [\in, ~sftBus, \out, ~delBus], ~sftGrp);
~delSynth = Synth(\delay, [\in, ~delBus, \out, 0], ~delGrp);

~smpGrp = Group.new;
~smpsftGrp = Group.after(~smpmicGrp);
~smpdelGrp = Group.after(~smpsftGrp);

~smpsftSynth = Synth(\pitchshift, [\in, ~smpsftBus, \out, ~smpdelBus], ~smpsftGrp);
~smpdelSynth = Synth(\delay, [\in, ~smpdelBus, \out, 0], ~smpdelGrp);
);


~delSynth.set(\mix, -0.5);
~delSynth.set(\addfactors, 0.0);
~delSynth.set(\decay, 4);
~delSynth.set(\delMin, 10.1);
~delSynth.set(\delMin, 10.5);
~sftSynth.set(\width, 0.0);
~smpdelSynth.set(\mix, 0.5);
~smpdelSynth.set(\addfactors, 0.0);
~smpdelSynth.set(\decay, 5);
~smpsftSynth.set(\width, 0.0);
)

