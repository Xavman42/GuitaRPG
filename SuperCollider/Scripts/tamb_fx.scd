(
//Tambura Region Growth Level 1
~tambL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_3, inf));
	Pdefn(\duration, Pwhite(0.5, 2.0));
	Pdefn(\play_rate, Pwhite(0.5, 2.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 500.0, \rq, 1.0, \lag, 2, \amp, 4);
	~hi_pass_synth.set(\mix, 1.0, \freq, 300, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.05, \decaytime, 4.0, \lag, 2, \amp, 4);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.001, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.5, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.6, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 8.0, \lag, 2);
	"tambL1".postln;
};

//Tambura Region Growth Level 2
~tambL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_3, inf));
	Pdefn(\duration, Pwhite(0.5, 5.0));
	Pdefn(\play_rate, Pwhite(0.5, 2.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 200.0, \rq, 1.0, \lag, 2, \amp, 4);
	~hi_pass_synth.set(\mix, 1.0, \freq, 200, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.04, \decaytime, 5.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.5, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.001, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.5, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 8.0, \lag, 2);
	"tambL2".postln;
};

//Tambura Region Growth Level 3
~tambL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_3, inf));
	Pdefn(\duration, Pwhite(0.2, 0.7));
	Pdefn(\play_rate, Pwhite(0.1, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 500.0, \rq, 0.01, \lag, 2, \amp, 4);
	~hi_pass_synth.set(\mix, 1.0, \freq, 150, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.06, \decaytime, 3.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.20, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.001, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.5, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 8.0, \lag, 2);
	"tambL3".postln;
};

//Tambura Region Growth Level 4
~tambL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_3, inf));
	Pdefn(\duration, Pwhite(0.01, 0.5));
	Pdefn(\play_rate, Pwhite(1.0, 10.0));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 1000.0, \rq, 0.01, \lag, 2, \amp, 4);
	~hi_pass_synth.set(\mix, 1.0, \freq, 500, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.04, \decaytime, 2.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.20, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.001, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.5, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.7, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 10.0, \lag, 2);
	"tambL4".postln;
};


//Tambura Region Growth Level 5
~tambL5 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_3, inf));
	Pdefn(\duration, Pwhite(1.3, 2.5));
	Pdefn(\play_rate, Pwhite(0.1, 2.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 1.0, \freq, 10000.0, \rq, 1.0, \lag, 2, \amp, 2);
	~hi_pass_synth.set(\mix, 1.0, \freq, 150, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.01, \decaytime, 4.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.001, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.5, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.9, \predelay, 1, \revtime, 10, \lpf, 800, \amp, 10.0, \lag, 2);
	"tambL5".postln;
};

)