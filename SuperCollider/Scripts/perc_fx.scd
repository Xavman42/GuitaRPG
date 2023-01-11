(
//Perc Region Growth Level 1
~percL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_2, inf));
	Pdefn(\duration, Pwhite(0.5, 1.0));
	Pdefn(\play_rate, Pwhite(0.8, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 600, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 1.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.2, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.8, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 2.0, \lag, 2);
	"percL1".postln;
};

//Perc Region Growth Level 2
~percL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_2, inf));
	Pdefn(\duration, Pwhite(0.1, 1.0));
	Pdefn(\play_rate, Pwhite(0.1, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 600, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 1.0, \del, 0.001, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.5, \predelay, 0.08, \speed, 4.0, \depth, 0.1, \ph_diff, 0.001, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.5, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 2.0, \lag, 2);
	"percL2".postln;
};

//Perc Region Growth Level 3
~percL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_2, inf));
	Pdefn(\duration, Pwhite(0.1, 1.0));
	Pdefn(\play_rate, Pwhite(0.1, 1.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 600, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 1.0, \del, 4.0, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 1.0, \predelay, 0.08, \speed, 0.001, \depth, 0.1, \ph_diff, 0.1, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.98, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 1.5, \lag, 2);
	"percL3".postln;
};

//Perc Region Growth Level 4
~percL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_2, inf));
	Pdefn(\duration, Pwhite(1.0, 2.0));
	Pdefn(\play_rate, Pwhite(0.1, 5.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 600, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2, \amp, 1);
	~ping_pong_synth.set(\mix, 1.0, \del, 0.01, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 1.0, \predelay, 0.08, \speed, 0.0001, \depth, 0.1, \ph_diff, 0.1, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.5, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 1.5, \lag, 2);
	"percL4".postln;
};

//Perc Region Growth Level 5
~percL5 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_2, inf));
	Pdefn(\duration, Pwhite(1.0, 5.0));
	Pdefn(\play_rate, Pwhite(0.1, 2.2));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 600, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 1.0, \del, 0.01, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.1, \predelay, 0.08, \speed, 0.01, \depth, 0.1, \ph_diff, 0.001, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 2, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.1, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 2, \lag, 2);
	"percL5".postln;
};
)