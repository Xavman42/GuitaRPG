(
//Rake Region Growth Level 1
~rakeL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pseq([
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.5, 3.0, 1)], inf));
	Pdefn(\play_rate, Prand([0.5, 1, 2, 4, 8], inf));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 1000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.2, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 0.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 12, \lag, 2);
	"rakeL1".postln;
};
~rakeL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pseq([
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(2.5, 3.0, 1)], inf));
	Pdefn(\play_rate, Prand([0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8], inf));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 1000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.2, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 0.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 12, \lag, 2);
	"rakeL2".postln;
};
~rakeL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pseq([
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.21, 0.3, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.21, 0.3, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.5, 1.0, 1)], inf));
	Pdefn(\play_rate, Prand([0.5, 4/6, 5/6, 1, 4/3, 5/3, 2, 8/3, 10/3, 4, 16/3, 20/3, 8], inf));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 1000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.2, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 0.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 12, \lag, 2);
	"rakeL3".postln;
};
~rakeL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pseq([
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.11, 0.2, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.11, 0.2, 1),
		Pwhite(0.01, 0.1, 1),
		Pwhite(0.1, 2.0, 1)], inf));
	Pdefn(\play_rate, Prand([0.5, 4/6, 0.75, 5/6, 1, 4/3, 1.5, 5/3, 2, 8/3, 3, 10/3, 4, 16/3, 6, 20/3, 8], inf));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 1000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.2, \maxdelaytime, 0.1, \delaytime, 0.3, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 0.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 12, \lag, 2);
	"rakeL4".postln;
};
)