/*
(
//Create arrays
~e2 = Array.new;
~f2 = Array.new;
~fs2 = Array.new;
~g2 = Array.new;
~gs2 = Array.new;
~a2 = Array.new;
~as2 = Array.new;
~b2 = Array.new;
~c3 = Array.new;
~cs3 = Array.new;
~d3 = Array.new;
~ds3 = Array.new;
~e3 = Array.new;
~f3 = Array.new;
~fs3 = Array.new;
~g3 = Array.new;
~gs3 = Array.new;
~a3 = Array.new;
~as3 = Array.new;
~b3 = Array.new;
~c4 = Array.new;
~cs4 = Array.new;
~d4 = Array.new;
~ds4 = Array.new;
~e4 = Array.new;
~f4 = Array.new;
~fs4 = Array.new;
~g4 = Array.new;
~gs4 = Array.new;
~a4 = Array.new;
~as4 = Array.new;
~b4 = Array.new;
~c5 = Array.new;
~cs5 = Array.new;
~d5 = Array.new;
~ds5 = Array.new;
~e5 = Array.new;

//Fill arrays with buffers
PathName("Samples/Pitches/E2/".resolveRelative).entries.do({
	arg path;
	~e2 = ~e2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/F2/".resolveRelative).entries.do({
	arg path;
	~f2 = ~f2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/F#2/".resolveRelative).entries.do({
	arg path;
	~fs2 = ~fs2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/G2/".resolveRelative).entries.do({
	arg path;
	~g2 = ~g2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/G#2/".resolveRelative).entries.do({
	arg path;
	~gs2 = ~gs2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/A2/".resolveRelative).entries.do({
	arg path;
	~a2 = ~a2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/A#2/".resolveRelative).entries.do({
	arg path;
	~as2 = ~as2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/B2/".resolveRelative).entries.do({
	arg path;
	~b2 = ~b2.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/C3/".resolveRelative).entries.do({
	arg path;
	~c3 = ~c3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/C#3/".resolveRelative).entries.do({
	arg path;
	~cs3 = ~cs3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/D3/".resolveRelative).entries.do({
	arg path;
	~d3 = ~d3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/D#3/".resolveRelative).entries.do({
	arg path;
	~ds3 = ~ds3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/E3/".resolveRelative).entries.do({
	arg path;
	~e3 = ~e3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/F3/".resolveRelative).entries.do({
	arg path;
	~f3 = ~f3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/F#3/".resolveRelative).entries.do({
	arg path;
	~fs3 = ~fs3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/G3/".resolveRelative).entries.do({
	arg path;
	~g3 = ~g3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/G#3/".resolveRelative).entries.do({
	arg path;
	~gs3 = ~gs3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/A3/".resolveRelative).entries.do({
	arg path;
	~a3 = ~a3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/A#3/".resolveRelative).entries.do({
	arg path;
	~as3 = ~as3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/B3/".resolveRelative).entries.do({
	arg path;
	~b3 = ~b3.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/C4/".resolveRelative).entries.do({
	arg path;
	~c4 = ~c4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/C#4/".resolveRelative).entries.do({
	arg path;
	~cs4 = ~cs4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/D4/".resolveRelative).entries.do({
	arg path;
	~d4 = ~d4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/D#4/".resolveRelative).entries.do({
	arg path;
	~ds4 = ~ds4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/E4/".resolveRelative).entries.do({
	arg path;
	~e4 = ~e4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/F4/".resolveRelative).entries.do({
	arg path;
	~f4 = ~f4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/F#4/".resolveRelative).entries.do({
	arg path;
	~fs4 = ~fs4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/G4/".resolveRelative).entries.do({
	arg path;
	~g4 = ~g4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/G#4/".resolveRelative).entries.do({
	arg path;
	~gs4 = ~gs4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/A4/".resolveRelative).entries.do({
	arg path;
	~a4 = ~a4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/A#4/".resolveRelative).entries.do({
	arg path;
	~as4 = ~as4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/B4/".resolveRelative).entries.do({
	arg path;
	~b4 = ~b4.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/C5/".resolveRelative).entries.do({
	arg path;
	~c5 = ~c5.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/C#5/".resolveRelative).entries.do({
	arg path;
	~cs5 = ~cs5.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/D5/".resolveRelative).entries.do({
	arg path;
	~d5 = ~d5.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/D#5/".resolveRelative).entries.do({
	arg path;
	~ds5 = ~ds5.add(Buffer.read(s, path.fullPath));
});
PathName("Samples/Pitches/E5/".resolveRelative).entries.do({
	arg path;
	~e5 = ~e5.add(Buffer.read(s, path.fullPath));
});

~big_array = Array.new;
~big_array = ~big_array.add(~e2);
~big_array = ~big_array.add(~f2);
~big_array = ~big_array.add(~fs2);
~big_array = ~big_array.add(~g2);
~big_array = ~big_array.add(~gs2);
~big_array = ~big_array.add(~a2);
~big_array = ~big_array.add(~as2);
~big_array = ~big_array.add(~b2);
~big_array = ~big_array.add(~c3);
~big_array = ~big_array.add(~cs3);
~big_array = ~big_array.add(~d3);
~big_array = ~big_array.add(~ds3);
~big_array = ~big_array.add(~e3);
~big_array = ~big_array.add(~f3);
~big_array = ~big_array.add(~fs3);
~big_array = ~big_array.add(~g3);
~big_array = ~big_array.add(~gs3);
~big_array = ~big_array.add(~a3);
~big_array = ~big_array.add(~as3);
~big_array = ~big_array.add(~b3);
~big_array = ~big_array.add(~c4);
~big_array = ~big_array.add(~cs4);
~big_array = ~big_array.add(~d4);
~big_array = ~big_array.add(~ds4);
~big_array = ~big_array.add(~e4);
~big_array = ~big_array.add(~f4);
~big_array = ~big_array.add(~fs4);
~big_array = ~big_array.add(~g4);
~big_array = ~big_array.add(~gs4);
~big_array = ~big_array.add(~a4);
~big_array = ~big_array.add(~as4);
~big_array = ~big_array.add(~b4);
~big_array = ~big_array.add(~c5);
~big_array = ~big_array.add(~cs5);
~big_array = ~big_array.add(~d5);
~big_array = ~big_array.add(~ds5);
~big_array = ~big_array.add(~e5);
)
*/


//MIDI note for E2 is 40
//MIDI note for E5 is 76

(
~pitches = Array.new;
PathName("Samples/Pitches/".resolveRelative).folders.do({
	arg folder;
	var sub_array;
	sub_array = Array.new;
	folder.entries.do({
		arg path, i;
		sub_array = sub_array.add(Buffer.read(s, path.fullPath));
	});
	~pitches = ~pitches.add(sub_array);
});
)

~pitches[36][2].play;

Env.adsr(0.001, 2, 1, 0.1).plot;
(
SynthDef.new(\guitar, {
	arg midinum = 40, rate = 1.0, amp = 0.8, out = 0, sustain = 0.2, timbre = 0;
	var sig, env, bufnum = 0;
	bufnum = SelectX.kr(timbre, Select.kr(midinum-40,~pitches));
	sig = PlayBuf.ar(
		numChannels: 1,
		bufnum: bufnum,
		rate: BufRateScale.kr(bufnum) * rate,
		doneAction: 2);
	//env = EnvGen.kr(Env.adsr(0.001, sustain, 1.0, 0.1)); //envs don't work with buffers like this
	//sig = sig * env;
	sig = Pan2.ar(sig);
	sig = sig * amp;
	Out.ar(out, sig);
}).add;
)

Synth(\guitar, [50, 1, 0.8, 0.2]);

(
p = Pbind(
	\instrument, \guitar,
	\dur, Pseq([0.5], inf),
	\amp, 0.8,
	\midinum, Pseq((40..76)),//[0, 4, 7] + Pseq((40..69)),
	\sustain, 0.1, // no effect
	\timbre, Pwhite(0,8),
);
)

p.play;