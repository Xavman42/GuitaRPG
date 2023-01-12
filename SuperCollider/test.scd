

//MIDI note for E2 is 40
//MIDI note for E5 is 76

(
~pitches = Array.new;
PathName("Samples/Pitches/".resolveRelative).folders.do({
	arg folder;
	var sub_array;
	sub_array = Array.new;
	folder.entries.do({
		arg path, i;
		sub_array = sub_array.add(Buffer.read(s, path.fullPath));
	});
	~pitches = ~pitches.add(sub_array);
});
)


Env.adsr(0.001, 2, 1, 0.1).plot;

(
SynthDef.new(\guitar, {
	arg amp = 0.8, out = 0, bufnum, gate = 1, rate = 1, start = 0;
	var sig, env;
	sig = PlayBuf.ar(
		numChannels: 1,
		bufnum: bufnum,
		rate: BufRateScale.kr(bufnum) * rate,
		startPos: start

	);
	env = EnvGen.kr(Env.asr(0.001, 1.0, 0.1), gate, doneAction: 2);
	sig = sig * env;
	sig = Pan2.ar(sig);
	sig = sig * amp;
	Out.ar(out, sig);
}).add;
)

Synth(\guitar, [amp: 0.25, out: 0, bufnum: ~pitches[20].choose]);
(
~guitar_binds = List[];
for (0, 2, {arg i;
	(
		~melody = Pbind(
			\instrument, \guitar,
			\dur, Pwrand([Pseq([0.125],2), 0.25, 0.5, 1], [1, 4, 6, 1].normalizeSum, inf),
			\amp, 0.4,
			// \degree, Pwhite(-20, 16), //Full chromatic range
			\degree, Pwhite(-8, 7), //Full majorPentatonic range
			// \degree, Pwhite(-11, 8), //Full diatonic range(dorian)
			\bufnum, Pfunc({
				arg ev;
				var note, midinote;
				note = ev[\degree].degreeToKey(Scale.majorPentatonic, 12);
				midinote = note + 60;
				~pitches[midinote - 40].choose
			}),
			\sustain, Pkey(\dur, inf)+Pwrand([0, 0.1, 0.15, 0.2, 0.5], [1, 3, 7, 6, 2], inf),
			\rate, Pwhite(-0.01, 0.01).midiratio * Pwrand([1, -1], [8, 2], inf),
			\start, Pfunc({ arg ev;
				if(
					ev[\rate] < 0,
					{ ev[\bufnum].numFrames - 1 },
					{ 0 }
				);
			})
		);
		q = ~melody.play(quant:1);
		~guitar_binds.add(q);
)});
)
(
for (0, ~guitar_binds.size, {arg i;
	~guitar_binds[i].stop;
});
)


(
~chords = Pbind(
	\instrument, \guitar,
	\dur, Pseq([1.2], inf),
	\amp, 0.4,
	\degree, Ptuple([
		Prand([0,1,2,3], inf)+Pwhite(-20, 0),
		Prand([6,7,8,9], inf)+Pwhite(-20, 0),
		Prand([12,13,14,15], inf)+Pwhite(-20, 0)
	], inf)  ,
	\bufnum, Pfunc({
		arg ev;
		var note, midinote, bufs;
		note = ev[\degree].degreeToKey(Scale.chromatic, 12);
		midinote = note + 60;
		bufs = ~pitches[midinote - 40];
		bufs.collect({ arg folder; folder.choose });
	}),
	\sustain, Pwhite(0.1, 2),
	\rate, Pwhite(-0.1, 0.1).midiratio * Prand([1, 1], inf),
	\start, Pfunc({ arg ev;
		if(
			ev[\rate] < 0,
			{ ev[\bufnum].numFrames - 1 },
			{ 0 }
		);
	})

);
q = ~chords.play;
)

[ ~pitches[20], ~pitches[24], ~pitches[27] ]


q.stop;

(
var note, midinote;
note = 3.degreeToKey(Scale.major, 12);
midinote = note + 60;
//~pitches[midinote - 40].choose.bufnum
)

p.play;



Event.partialEvents[\pitchEvent][\midinote].postcs