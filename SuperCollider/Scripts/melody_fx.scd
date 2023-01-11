(
//Melody Region Growth Level 1
~meloL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	for (0, 1, {arg i;
		(
			~melody = Pbind(
				\instrument, \guitar,
				\dur, Pwrand([Pseq([0.125],2), 0.25, 0.5, 1], [1, 4, 6, 1].normalizeSum, inf),
				\amp, 0.2,
				// \degree, Pwhite(-20, 16), //Full chromatic range
				\degree, Pwhite(-7, 7), //Full majorPentatonic range
				// \degree, Pwhite(-11, 8), //Full diatonic range(dorian)
				\bufnum, Pfunc({
					arg ev;
					var note, midinote;
					note = ev[\degree].degreeToKey(Scale.majorPentatonic, 12);
					midinote = note + 59;
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
				}),
				\out, ~hi_pass_bus,
			);
			q = ~melody.play(quant:1);
			~guitar_binds.add(q);
	)});
	Pdefn(\buf_mul, 0.0);
	~mid_cut_synth.set(\mix, 0.0, \freq, 16000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.5, \freq, 1000, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 1.0, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4, \lag, 2);
	"meloL1".postln;
};

//Melody Region Growth Level 2
~meloL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	for (0, 1, {arg i;
		(
			~melody = Pbind(
				\instrument, \guitar,
				\dur, Pwrand([Pseq([0.125],2), 0.25, 0.5, 1], [1, 4, 6, 1].normalizeSum, inf),
				\amp, 0.2,
				// \degree, Pwhite(-20, 16), //Full chromatic range
				// \degree, Pwhite(-8, 7), //Full majorPentatonic range
				\degree, Pwhite(-11, 8), //Full diatonic range(dorian)
				\bufnum, Pfunc({
					arg ev;
					var note, midinote;
					note = ev[\degree].degreeToKey(Scale.dorian, 12);
					midinote = note + 59;
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
				}),
				\out, ~hi_pass_bus,
			);
			q = ~melody.play(quant:1);
			~guitar_binds.add(q);
	)});
	Pdefn(\buf_mul, 0.0);
	~mid_cut_synth.set(\mix, 0.0, \freq, 16000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.5, \freq, 1000, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.3, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.8, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4, \lag, 2);
	"meloL2".postln;
};

//Melody Region Growth Level 3
~meloL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	for (0, 3, {arg i;
		(
			~melody = Pbind(
				\instrument, \guitar,
				\dur, Pwrand([Pseq([0.125],2), 0.25, 0.5, 1], [1, 4, 6, 1].normalizeSum, inf),
				\amp, 0.2,
				// \degree, Pwhite(-20, 16), //Full chromatic range
				// \degree, Pwhite(-8, 7), //Full majorPentatonic range
				\degree, Pwhite(-11, 8), //Full diatonic range(dorian)
				\bufnum, Pfunc({
					arg ev;
					var note, midinote;
					note = ev[\degree].degreeToKey(Scale.dorian, 12);
					midinote = note + 59;
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
				}),
				\out, ~hi_pass_bus,
			);
			q = ~melody.play(quant:1);
			~guitar_binds.add(q);
	)});
	Pdefn(\buf_mul, 0.0);
	~mid_cut_synth.set(\mix, 0.0, \freq, 16000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.5, \freq, 1000, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.5, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.5, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.5, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4, \lag, 2);
	"meloL3".postln;
};


//Melody Region Growth Level 4
~meloL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	~guitar_binds = List[];
	for (0, 2, {arg i;
		(
			~melody = Pbind(
				\instrument, \guitar,
				\dur, Pwrand([Pseq([0.125],2), 0.25, 0.5, 1], [1, 4, 6, 1].normalizeSum, inf),
				\amp, 0.2,
				\degree, Pwhite(-20, 16), //Full chromatic range
				// \degree, Pwhite(-8, 7), //Full majorPentatonic range
				//\degree, Pwhite(-11, 8), //Full diatonic range(dorian)
				\bufnum, Pfunc({
					arg ev;
					var note, midinote;
					note = ev[\degree].degreeToKey(Scale.chromatic, 12);
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
				}),
				\out, ~hi_pass_bus,
			);
			q = ~melody.play(quant:1);
			~guitar_binds.add(q);
	)});
	Pdefn(\buf_mul, 0.0);
	~mid_cut_synth.set(\mix, 0.5, \freq, 16000.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.5, \freq, 1000, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.2, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.5, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.2, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.1, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.5, \freq, 30, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4, \lag, 2);
	"meloL4".postln;
};
)