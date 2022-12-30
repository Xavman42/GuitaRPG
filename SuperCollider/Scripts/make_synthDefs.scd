(
// Play Buffer
SynthDef(\play_buf, {| bufnum = 0, out = 0, rate = 1, mul = 0.1|
	var frames;
	frames = BufFrames.kr(bufnum);
	Out.ar(out,
		PlayBuf.ar(1,
			bufnum,
			BufRateScale.kr(bufnum),
			doneAction: Done.freeSelf,
			rate: rate,
			//startPos: (((rate>0).binaryValue*0) + ((rate<0).binaryValue*1))*frames
		)*mul;
	)
}).add;

// Mids cut filter
SynthDef(\mids, { |in, out, freq = 440.0, rq = 1.0, mix = 0.5, lag = 2, amp = 1|
	var dry, wet, sig;
	dry = In.ar(in, 1);
	wet = BRF.ar(dry, freq.varlag(lag), rq.varlag(lag));
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// High pass filter
SynthDef(\hi, { |in, out, freq = 600, mix = 0.5, lag = 2, amp = 1|
	var dry, wet, sig;
	dry = In.ar(in, 1);
	wet = HPF.ar(dry, freq.varlag(lag));
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// Comb filter
SynthDef(\comb, { |in, out, maxdelaytime = 0.2, delaytime = 0.2, decaytime = 1.0, mix = 0.5, lag = 2, amp = 1|
	var dry, wet, sig;
	dry = In.ar(in, 1);
	wet = CombN.ar(dry, maxdelaytime.varlag(lag), delaytime.varlag(lag), decaytime.varlag(lag));
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	sig = LeakDC.ar(sig);
	Out.ar(out, sig)*amp;
}).add;

// Randomized delay
SynthDef(\delay, { |min = -40, max = -6, in, del = 0.25, mix = 0.7, amp = 1, out, buf, lag = 2|
	var dry, wet, sig, dels, delamps;
	dels = \dels.kr(Array.geom(10, 0.1, 1.5));
	delamps = \delamps.kr(Array.series(10, -3, -3).dbamp);
	dry = In.ar(in, 1);
	wet = 2.collect({
		|index|
		DelayN.ar(dry, 2, dels.at(index), delamps.at(index))
	}).sum;
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// Ping-pong Delay
SynthDef(\ping, { |in, buf, del = 0.5, delmin = 0.1, delmax = 0.5, fb = 0.7, out, mix = 0.5, amp = 1, lag = 2|
	var dry, dry2, sig;
	dry = [ In.ar(in, 1), Silent.ar ];
	dry2 = In.ar(in, 1) ! 2;
	sig = PingPong.ar(buf, dry, SinOsc.kr(LFTri.kr(del).range(0.1, 0.5)).range(delmin, delmax), fb, 1);
	sig = XFade2.ar(dry2, sig, mix.varlag(lag)*2-1, amp);
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// Pitch Shift
SynthDef(\shift, { |in, out, amp = 1, mix = 0.7, lag = 2|
	var dry, wet, sig, pitch_ratio = 1.2;
	dry = In.ar(in, 2);
	wet = PitchShift.ar(dry, 0.2, pitch_ratio);
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// Chorus
SynthDef(\chorus, { |in, out, predelay = 0.08, speed = 0.03, depth = 0.1, ph_diff = 0.05, mix = 0.5, lag = 2, amp = 1|
	var dry, wet, modulators, numDelays = 12, sig;
	dry = In.ar(in, 2);
	numDelays.reciprocal;
	modulators = Array.fill(numDelays,
		{arg i;
			LFPar.kr(speed.varlag(lag), rrand(0.94, 1.06), ph_diff.varlag(lag) * i, depth.varlag(lag), predelay.varlag(lag));
	});
	wet = DelayC.ar(dry, 0.5, modulators);
	wet = wet.sum;
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag))/12;
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// Ring modulation
SynthDef(\ring, { |in, out, freq = 20, mix = 0.5, lag = 2, amp = 1|
	var dry, wet, carrier, modulator, sig;
	dry = In.ar(in, 2);
	carrier = dry;
	modulator = SinOsc.ar(SinOsc.ar(freq.varlag(lag)));
	wet = carrier * modulator;
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

// Reverb
SynthDef(\reverb, { |in, predelay = 1, revtime = 10, lpf = 500, amp = 1, out=0, mix = 0.7, lag = 2|
	var dry, wet, temp, sig;
	dry = In.ar(in, 2);
	temp = In.ar(in, 2);
	wet = 0;
	temp = DelayN.ar(temp, 0.2, predelay.varlag(lag));
	32.do {temp = AllpassN.ar(temp, 0.05, {Rand(0.001, 0.05)}, revtime.varlag(lag));
		temp = LPF.ar(temp, lpf.varlag(lag));
		wet = wet + temp;
	};
	sig = XFade2.ar(dry, wet, mix.varlag(lag)*2-1, amp.varlag(lag));
	sig = Limiter.ar(sig, -10.dbamp, 0.001);
	Out.ar(out, sig);
}).add;

////////////////////
// Live effects
////////////////////

SynthDef(\mic, {
	arg in0 = 0, in1 = 1, out0 = 0, out1 = 1, out2 = 2;
	var mic0, mic1, sig;
	mic0 = SoundIn.ar(in0) * 0.5;
	mic1 = SoundIn.ar(in1) * 0.5;
	sig = mic0 + mic1;
	Out.ar(out0, sig);
	Out.ar(out1, sig);
	Out.ar(out2, sig);
}).add;

SynthDef(\live_reverb, {
	arg in = 0, mix = 0.3, out = 0, room = 0.8, amp = 1;
	var sig;
	sig = In.ar(in, 1);
	sig = FreeVerb.ar(sig, mix: mix, room: room);
	sig = LPF.ar(sig, 1500);
	sig = sig * amp;
	sig = Pan2.ar(sig);
	Out.ar(out, sig);
}).add;

SynthDef(\live_delay, {
	arg in = 0,mix = 0.3, del = 0.2, out = 0, amp = 1;
	var sig;
	sig = In.ar(in, 1);
	sig = CombC.ar(sig, 1.5, del, 3);
	sig = sig * amp;
	sig = Pan2.ar(sig);
	Out.ar(out, sig);
}).add;

SynthDef(\live_chorus, {
	arg in, out, snip = 0, predelay = 0.08, speed = 0.03, depth = 0.1, ph_diff = 0.05, mix = 0.5, lag = 2, amp = 1;
	var dry, wet, modulators, numDelays = 12, sig;
	dry = In.ar(in, 1);
	numDelays.reciprocal;
	modulators = Array.fill(numDelays,
		{arg i;
			LFPar.kr(speed.varlag(lag), rrand(0.94, 1.06), ph_diff.varlag(lag) * i, depth.varlag(lag), predelay.varlag(lag));
	});
	wet = DelayC.ar(dry, 0.5, modulators);
	wet = wet.sum;
	sig = Limiter.ar(wet, -10.dbamp, 0.001) * amp;
	sig = Pan2.ar(sig);
	Out.ar(out, sig);
}).add;
)