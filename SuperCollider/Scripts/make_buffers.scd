(
s.newBusAllocators;
~live_reverb_bus = Bus.audio(s, 1);
~live_delay_bus = Bus.audio(s, 1);
~live_chorus_bus = Bus.audio(s, 1);
~reverb_bus = Bus.audio(s, 2);
~delay_bus = Bus.audio(s, 2);
~ring_mod_bus = Bus.audio(s, 2);
~chorus_bus = Bus.audio(s, 2);
~pitch_shift_bus = Bus.audio(s, 2);
~ping_pong_bus = Bus.audio(s, 1);
~random_delay_bus = Bus.audio(s, 1);
~comb_bus = Bus.audio(s, 1);
~hi_pass_bus = Bus.audio(s, 1);
~mid_cut_bus = Bus.audio(s, 1);

~region_1_samples = PathName.new(~path ++ "Samples/Scrape").files.scramble.copyFromStart(29);
~region_2_samples = PathName.new(~path ++ "Samples/Perc").files.scramble.copyFromStart(74);
~region_3_samples = PathName.new(~path ++ "Samples/Tamb").files.scramble.copyFromStart(34);
~region_4_samples = PathName.new(~path ++ "Samples/Bartok").files.scramble.copyFromStart(82);

~buff_array_1 = Array.new;
~buff_array_2 = Array.new;
~buff_array_3 = Array.new;
~buff_array_4 = Array.new;

~region_1_samples.do({ |item| ~buff_array_1 = ~buff_array_1.add(Buffer.read(s, item.fullPath)); });
~region_2_samples.do({ |item| ~buff_array_2 = ~buff_array_2.add(Buffer.read(s, item.fullPath)); });
~region_3_samples.do({ |item| ~buff_array_3 = ~buff_array_3.add(Buffer.read(s, item.fullPath)); });
~region_4_samples.do({ |item| ~buff_array_4 = ~buff_array_4.add(Buffer.read(s, item.fullPath)); });
~ppbuf = Buffer.alloc(s, s.sampleRate * 10, 2);
)