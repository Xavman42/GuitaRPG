(
//Harm Region Growth Level 1
~harmL1 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pwhite(0.5, 1.0)*2);
	Pdefn(\play_rate, 1);
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 1000, \lag, 2, \amp, 2);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.2, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.01, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 0.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.6, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 16, \lag, 2);
	"harmL1".postln;
};
~harmL2 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pseq([0.8, 0.9, 1, 1.1, 3.2], inf));
	Pdefn(\play_rate, 1);
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 800, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.0, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 12, \lag, 2);
	"harmL2".postln;
};
~harmL3 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Prand(~harm_buff_array, inf));
	Pdefn(\duration, Pwhite(0.5, 1.0)*2);
	Pdefn(\play_rate, 1);
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 800, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 0.02, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.1, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 14, \lag, 2);
	"harmL3".postln;
};
~harmL4 = {
	for (0, ~guitar_binds.size, {arg i; ~guitar_binds[i].stop;});
	Pdefn(\bufarray, Pwalk(~harm_buff_array, Prand([-2, 1, 1, 2], inf), Pseq([1, -1])));
	Pdefn(\duration, Pseq([0.8, 0.9, 1, 1.1, 4.2], inf));
	Pdefn(\play_rate, Prand([1, 2], inf));
	Pdefn(\buf_mul, 0.1);
	~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
	~hi_pass_synth.set(\mix, 0.0, \freq, 800, \lag, 2, \amp, 4);
	~comb_synth.set(\mix, 0.0, \maxdelaytime, 0.2, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
	~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 2, \lag, 2);
	~ping_pong_synth.set(\mix, 0.0, \del, 2, \delmin, -1, \delmax, 1, \fb, 0.7, \amp, 2, \lag, 2);
	~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
	~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
	~ring_mod_synth.set(\mix, 0.0, \freq, 20.4, \lag, 2, \amp, 1);
	~reverb_synth.set(\mix, 0.2, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 14, \lag, 2);
	"harmL4".postln;
};
)