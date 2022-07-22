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
)

(
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
)

(
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
)

10.do(~scratchy_string)

(
x = OSCFunc( { | msg, time, addr, port |
    var synthType;

    synthType = msg[1].asString;
	synthType.postln;
	( "attempting to play synth" + synthType ).postln;
	case
	{ synthType == "plinky_wood"} {10.do(~plinky_wood)}
	{ synthType == "scratchy_string"} {10.do(~scratchy_string)};

}, "/print" );
)

