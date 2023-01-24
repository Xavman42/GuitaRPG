(
//Rasg Region Growth Level 1
~rasgL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	~chords = Pbind(
		\instrument, \guitar,
		\dur, Prand([2, Pseq([1,1])], inf),
		\amp, 0.4,
		\degree, Pseq([[0, 7, 12, 16, 19, 24]-20], inf),
		\bufnum, Pfunc({
			arg ev;
			var note, midinote, bufs;
			note = ev[\degree].degreeToKey(Scale.chromatic, 12);
			midinote = note + 60;
			bufs = ~pitches[midinote - 40];
			bufs.collect({ arg folder; folder.choose });
		}),
		\sustain, Pkey(\dur),
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
	~mid_cut_synth.set(\mix, 0.0, \freq, 6000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.4, \freq, 400, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 4, \lpf, 500, \amp, 14, \lag, 2);
	"rasgL1".postln;
};
~rasgL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	~chords = Pbind(
		\instrument, \guitar,
		\dur, Prand([2, Pseq([1,1]), Pseq([2/3,2/3,2/3])], inf),
		\amp, 0.4,
		\degree, Prand([[1, 8, 13, 17, 19, 24]-20, [0, 7, 12, 16, 19, 24]-20], inf),
		\bufnum, Pfunc({
			arg ev;
			var note, midinote, bufs;
			note = ev[\degree].degreeToKey(Scale.chromatic, 12);
			midinote = note + 60;
			bufs = ~pitches[midinote - 40];
			bufs.collect({ arg folder; folder.choose });
		}),
		\sustain, Pkey(\dur),
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
	~mid_cut_synth.set(\mix, 0.0, \freq, 6000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.4, \freq, 400, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.15, \predelay, 1, \revtime, 4, \lpf, 500, \amp, 14, \lag, 2);
	"rasgL1".postln;
};
~rasgL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	~chords = Pbind(
		\instrument, \guitar,
		\dur, Prand([2, Pseq([1,1]), Pseq([2/3,2/3,2/3]), Pseq([0.5, 0.5, 0.5, 0.5])], inf),
		\amp, 0.4,
		\degree, Prand([[1, 8, 13, 17, 19, 24]-20, [0, 7, 12, 16, 19, 24]-20, [3, 10, 15, 19, 19, 24]-20], inf),
		\bufnum, Pfunc({
			arg ev;
			var note, midinote, bufs;
			note = ev[\degree].degreeToKey(Scale.chromatic, 12);
			midinote = note + 60;
			bufs = ~pitches[midinote - 40];
			bufs.collect({ arg folder; folder.choose });
		}),
		\sustain, Pkey(\dur),
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
	~mid_cut_synth.set(\mix, 0.0, \freq, 6000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.4, \freq, 400, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.1, \predelay, 1, \revtime, 4, \lpf, 500, \amp, 14, \lag, 2);
	"rasgL1".postln;
};
~rasgL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	~chords = Pbind(
		\instrument, \guitar,
		\dur, Prand([2, Pseq([1,1]), Pseq([2/3,2/3,2/3]), Pseq([0.5, 0.5, 0.5, 0.5]), Pseq([2/5, 2/5, 2/5, 2/5, 2/5])], inf),
		\amp, 0.4,
		\degree, Prand([[1, 8, 13, 17, 19, 24]-20, [0, 7, 12, 16, 19, 24]-20, [3, 10, 15, 19, 19, 24]-20, [5, 12, 17, 20, 24]-20], inf),
		\bufnum, Pfunc({
			arg ev;
			var note, midinote, bufs;
			note = ev[\degree].degreeToKey(Scale.chromatic, 12);
			midinote = note + 60;
			bufs = ~pitches[midinote - 40];
			bufs.collect({ arg folder; folder.choose });
		}),
		\sustain, Pkey(\dur),
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
	~mid_cut_synth.set(\mix, 0.0, \freq, 6000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.4, \freq, 400, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.05, \predelay, 1, \revtime, 4, \lpf, 500, \amp, 14, \lag, 2);
	"rasgL1".postln;
};
)