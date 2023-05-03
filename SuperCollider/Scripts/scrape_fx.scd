(
//Scrape Region Growth Level 1
~scrapeL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_1, inf));
	Pdefn(\duration, Pwhite(3.0, 10.4));
	Pdefn(\play_rate, Pwhite(0.15, 0.3));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 1.0, \freq, 100, \lag, 2, \amp, 1);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.5, \min, -40, \max, -6, \del, 0.25, \amp, 4, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.4, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 1.0, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4.0, \lag, 2);
	"scrapeL1".postln;
};

//Scrape Region Growth Level 2
~scrapeL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_1, inf));
	Pdefn(\duration, Pwhite(0.5, 4.4));
	Pdefn(\play_rate, Pwhite(0.1, 0.5));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 1.0, \freq, 1200, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.15, \decaytime, 1.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 0.2, \predelay, 0.08, \speed, 10.0, \depth, 0.3, \ph_diff, 0.05, \lag, 2, \amp, 2);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.8, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 4.2, \lag, 2);
	"scrapeL2".postln;
};

//Scrape Region Growth Level 3
~scrapeL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_1, inf));
	Pdefn(\duration, Pwhite(0.5, 4.4));
	Pdefn(\play_rate, Pwhite(0.1, 0.5));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 1.0, \freq, 600, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.15, \decaytime, 1.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 3, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 1.0, \predelay, 0.08, \speed, 5.0, \depth, 0.3, \ph_diff, 0.05, \lag, 2, \amp, 2);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.9, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 1.5, \lag, 2);
	"scrapeL3".postln;
};

//Scrape Region Growth Level 4
~scrapeL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_1, inf));
	Pdefn(\duration, Pwhite(0.5, 2.5));
	Pdefn(\play_rate, Pwhite(0.2, 1.0));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 1.0, \freq, 200, \lag, 2, \amp, 3);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.15, \decaytime, 1.0, \lag, 2, \amp, 3);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
	~chorus_synth.set(\mix, 1.0, \predelay, 0.08, \speed, 2.0, \depth, 0.7, \ph_diff, 0.05, \lag, 2, \amp, 1.5);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 1.0, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 1.0, \lag, 2);
	"scrapeL4".postln;
};

//Scrape Region Growth Level 5
~scrapeL5 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~buff_array_1, inf));
	Pdefn(\duration, Pwhite(0.5, 1.5));
	Pdefn(\play_rate, Pwhite(0.2, 1.0));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 1.0, \freq, 150, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 1.0, \maxdelaytime, 0.2, \delaytime, 0.1, \decaytime, 1.0, \lag, 2, \amp, 2);
	~random_delay_synth.set(\mix, 1.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 1.0, \predelay, 0.08, \speed, 30.0, \depth, 0.7, \ph_diff, 0.05, \lag, 2, \amp, 2);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.9999, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 1.0, \lag, 2);
	"scrapeL5".postln;
};
)