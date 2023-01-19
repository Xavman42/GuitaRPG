(
//Advanced Harmony Region Growth Level 1
~adv_harmL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	~chords = Pbind(
		\instrument, \guitar,
		\dur, Pseq([1, 0.75, 1.75], inf) * Pwhite(0.9, 1.1),
		\amp, 0.4,
		\degree, Prand([
			Pseq([[5, 8, 12, 14], [5, 8, 11, 15], [3, 7, 10, 14]]),
			Pseq([[5, 12, 16], [5, 11, 16], [4, 11, 14]]),
			Pseq([[0, 5, 9], [-1, 5, 9], [-1, 4, 8]])
		], inf) + Pdup(3, Pwhite(-19,0)),
		\bufnum, Pfunc({
			arg ev;
			var note, midinote, bufs;
			note = ev[\degree].degreeToKey(Scale.chromatic, 12);
			midinote = note + 60;
			bufs = ~pitches[midinote - 40];
			bufs.collect({ arg folder; folder.choose });
		}),
		\sustain, Pkey(\dur)-0.1,
		\rate, Pwhite(-0.1, 0.1).midiratio * Prand([1, 1], inf),
		\start, Pfunc({ arg ev;
			if(
				ev[\rate] < 0,
				{ ev[\bufnum].numFrames - 1 },
				{ 0 }
			);
		}),
		\out, ~hi_pass_bus,

	);
	q = ~chords.play;
	~guitar_binds.add(q);
	Pdefn(\buf_mul, 0.0);
	~mid_cut_synth.set(\mix, 0.0, \freq, 16000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 400, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.0, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4, \lag, 2);
	"adv_harmL1".postln;
};


//Level 2 just diminished chords

//Level 3 back to 2-5-1s but with 9s

//Level 4 quartal and quintal harmony
)