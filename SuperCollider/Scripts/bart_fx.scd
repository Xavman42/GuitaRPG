(
//Bartok Region Growth Level 1
~bartL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_4, inf));
	Pdefn(\duration, Pwhite(0.01, 0.2));
	Pdefn(\play_rate, Pwhite(0.4, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 16000.0, \rq, 1.0, \lag, 2, \amp, 2);
	~hi_pass_synth.set(\mix, 1.0, \freq, 8000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 02, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.5, \freq, 30, \lag, 2, \amp, 2);
	~reverb_synth.set(\mix, 0.8, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 8, \lag, 2);
	"bartL1".postln;
};

//Bartok Region Growth Level 2
~bartL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_4, inf));
	Pdefn(\duration, Pwhite(0.01, 0.4));
	Pdefn(\play_rate, Pwhite(0.4, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 10000.0, \rq, 1.0, \lag, 2, \amp, 2);
	~hi_pass_synth.set(\mix, 1.0, \freq, 3000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.9, \maxdelaytime, 20, \delaytime, 1.1, \decaytime, 10.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.5, \freq, 40, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.5, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 8, \lag, 2);
	"bartL2".postln;
};

//Bartok Region Growth Level 3
~bartL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_4, inf));
	Pdefn(\duration, Pwhite(0.5, 1.4));
	Pdefn(\play_rate, Pwhite(0.4, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 2000.0, \rq, 100.0, \lag, 2, \amp, 2);
	~hi_pass_synth.set(\mix, 1.0, \freq, 1000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.1, \maxdelaytime, 20, \delaytime, 0.02, \decaytime, 10.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.5, \freq, 3, \lag, 2, \amp, 2);
	~reverb_synth.set(\mix, 0.8, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 5, \lag, 2);
	"bartL3".postln;
};

//Bartok Region Growth Level 4
~bartL4 = {
	Pdefn(\bufarray, Prand(~buff_array_4, inf));
	Pdefn(\duration, Pwhite(0.4, 1.8));
	Pdefn(\play_rate, Pwhite(0.1, 0.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 2000.0, \rq, 100.0, \lag, 2, \amp, 2);
	~hi_pass_synth.set(\mix, 1.0, \freq, 500, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.1, \maxdelaytime, 20, \delaytime, 2, \decaytime, 10.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2, \amp, 1);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.8, \freq, 4, \lag, 2, \amp, 2);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 5, \lag, 2);
	"bartL4".postln;
};

//Bartok Region Growth Level 5
~bartL5 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_4, inf));
	Pdefn(\duration, Pwhite(0.1, 0.14));
	Pdefn(\play_rate, Pwhite(0.1, 8.0));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 1000.0, \rq, 1.0, \lag, 2, \amp, 2);
	~hi_pass_synth.set(\mix, 1.0, \freq, 100, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.1, \maxdelaytime, 20, \delaytime, 0.5, \decaytime, 10.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2, \amp, 1);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.8, \freq, 4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 400, \amp, 5, \lag, 2);
	"bartL5".postln;
};
)