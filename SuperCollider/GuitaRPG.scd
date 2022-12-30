Server.killAll;
s.options.inDevice = "MME : Microphone (H4)";

(
s.waitForBoot({
	~path = PathName(thisProcess.nowExecutingPath).parentPath;
	s.options.memSize_(2.pow(20));

	ServerTree.removeAll;

	(~path ++ "Scripts/make_buffers.scd").load;
	(~path ++ "Scripts/make_synthDefs.scd").load;

	s.sync;

	~init = {
		~ppbuf.zero;
		~source_group = Group.new;
		~fx_group = Group.after(~source_group);

		~reverb_synth = Synth(\reverb, [\in, ~reverb_bus], ~fx_group);
		~ring_mod_synth = Synth(\ring, [\in, ~ring_mod_bus, \out, ~reverb_bus], ~fx_group);
		~chorus_synth = Synth(\chorus, [\in, ~chorus_bus, \out, ~ring_mod_bus], ~fx_group);
		~pitch_shift_synth = Synth(\shift, [\in, ~pitch_shift_bus, \out, ~chorus_bus], ~fx_group);
		~ping_pong_synth = Synth(\ping, [\in, ~ping_pong_bus, \out, ~pitch_shift_bus, \buf, ~ppbuf], ~fx_group);
		~random_delay_synth = Synth(\delay, [\in, ~random_delay_bus, \out, ~ping_pong_bus], ~fx_group);
		~comb_synth = Synth(\comb, [\in, ~comb_bus, \out, ~random_delay_bus], ~fx_group);
		~hi_pass_synth = Synth(\hi, [\in, ~hi_pass_bus, \out, ~comb_bus], ~fx_group);
		~mid_cut_synth = Synth(\mids, [\in, ~mid_cut_bus, \out, ~hi_pass_bus], ~fx_group);

		d = Synth(\live_delay, [in: ~live_delay_bus, out: 0, mix: 1]);
		r = Synth(\live_reverb, [in: ~live_reverb_bus, out: 0, mix: 1]);
		c = Synth(\live_chorus, [in: ~live_chorus_bus, out: 0, mix: 1]);
		m = Synth(\mic, [in0: 0, in1: 1, out0: ~live_reverb_bus, out1: ~live_delay_bus, out2: ~live_chorus_bus]);
	};

	ServerTree.add(~init);
	ServerTree.run;

	s.sync;

	(~path ++ "Scripts/scrape_fx.scd").load;
	(~path ++ "Scripts/perc_fx.scd").load;
	(~path ++ "Scripts/tamb_fx.scd").load;
	(~path ++ "Scripts/bart_fx.scd").load;

	~piece = ();
	~piece.scrape = ();
	~piece.scrape.l1 = ~scrapeL1;
	~piece.scrape.l2 = ~scrapeL2;
	~piece.scrape.l3 = ~scrapeL3;
	~piece.scrape.l4 = ~scrapeL4;
	~piece.scrape.l5 = ~scrapeL5;
	~piece.perc = ();
	~piece.perc.l1 = ~percL1;
	~piece.perc.l2 = ~percL2;
	~piece.perc.l3 = ~percL3;
	~piece.perc.l4 = ~percL4;
	~piece.perc.l5 = ~percL5;
	~piece.tamb = ();
	~piece.tamb.l1 = ~tambL1;
	~piece.tamb.l2 = ~tambL2;
	~piece.tamb.l3 = ~tambL3;
	~piece.tamb.l4 = ~tambL4;
	~piece.tamb.l5 = ~tambL5;
	~piece.bart = ();
	~piece.bart.l1 = ~bartL1;
	~piece.bart.l2 = ~bartL2;
	~piece.bart.l3 = ~bartL3;
	~piece.bart.l4 = ~bartL4;
	~piece.bart.l5 = ~bartL5;
});
)

(
Pbind(
	\instrument, \play_buf,
	\dur, Pdefn(\duration, Pwhite(0.1, 1.5)),
	\out, ~hi_pass_bus,
	\bufnum, Pdefn(\bufarray, Prand(~buff_array_1, inf)),
	\rate, Pdefn(\play_rate, Pwhite(0.8, 1.2))
).play;

x = OSCFunc( { | message, time, addr, port |
	var area, region, level;

	area = message[1].asString;
	region = message[2].asString;
	level = message[3].asInteger;
	( "attempting to play synth" + region ).postln;
	case
	{ region == "scrape"} {
		case
		{ level == 1}{~piece.scrape.l1}
		{ level == 2}{~piece.scrape.l2}
		{ level == 3}{~piece.scrape.l3}
		{ level == 4}{~piece.scrape.l4}
		{ level == 5}{~piece.scrape.l5}
	}
	{ region == "perc"} {
		case
		{ level == 1}{~piece.perc.l1}
		{ level == 2}{~piece.perc.l2}
		{ level == 3}{~piece.perc.l3}
		{ level == 4}{~piece.perc.l4}
		{ level == 5}{~piece.perc.l5}
	}
	{ region == "tamb"} {
		case
		{ level == 1}{~piece.tamb.l1}
		{ level == 2}{~piece.tamb.l2}
		{ level == 3}{~piece.tamb.l3}
		{ level == 4}{~piece.tamb.l4}
		{ level == 5}{~piece.tamb.l5}
	}
	{ region == "bart"} {
		case
		{ level == 1}{~piece.bart.l1}
		{ level == 2}{~piece.bart.l2}
		{ level == 3}{~piece.bart.l3}
		{ level == 4}{~piece.bart.l4}
		{ level == 5}{~piece.bart.l5}
	}

}, "/print" );

)

~piece.scrape.l3.();
~piece.perc.l5.();
~piece.tamb.l3.();
~piece.bart.l5.();

(
//All effects off
Pdefn(\duration, Pwhite(3.0, 4.4));
Pdefn(\play_rate, Pwhite(0.9, 1.0));
~mid_cut_synth.set(\mix, 0.0, \freq, 440.0, \rq, 1.0, \lag, 2, \amp, 1);
~hi_pass_synth.set(\mix, 0.0, \freq, 600, \lag, 2, \amp, 1);
~comb_synth.set(\mix, 0.0, \maxdelaytime, 02, \delaytime, 0.2, \decaytime, 1.0, \lag, 2, \amp, 1);
~random_delay_synth.set(\mix, 0.0, \min, -40, \max, -6, \del, 0.25, \amp, 1, \lag, 2);
~ping_pong_synth.set(\mix, 0.0, \del, 0.5, \fb, 0.7, \amp, 1, \lag, 2);
~chorus_synth.set(\mix, 0.0, \predelay, 0.08, \speed, 0.03, \depth, 0.1, \ph_diff, 0.05, \lag, 2, \amp, 1);
~pitch_shift_synth.set(\mix, 0.0, \amp, 1, \lag, 2);
~ring_mod_synth.set(\mix, 0.0, \freq, 20, \lag, 2, \amp, 1);
~reverb_synth.set(\mix, 0.0, \predelay, 1, \revtime, 10, \lpf, 500, \amp, 1, \lag, 2);
)

(
//All effects on
Pdefn(\duration, Pwhite(0.9, 1.0));
Pdefn(\play_rate, Pwhite(0.8, 1.2));
~mid_cut_synth.set(\mix, 1.0 );
~hi_pass_synth.set(\mix, 1.0 );
~comb_synth.set(\mix, 1.0 );
~random_delay_synth.set(\mix, 1.0 );
~ping_pong_synth.set(\mix, 1.0 );
~chorus_synth.set(\mix, 1.0 );
~pitch_shift_synth.set(\mix, 1.0 );
~ring_mod_synth.set(\mix, 1.0 );
~reverb_synth.set(\mix, 1.0 );
)

Server.killAll;


