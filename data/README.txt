Data from Simmons, Prentice, Tkacik, Homann, Yee, Palmer, Nelson, & Balasubramanian (2013).  Transformation of Stimulus Correlations by the Retina.  PLOS Computational Biology.


--------------------
FILE NAMES
--------------------

data_MM_DD_YY_tT.mat: timing of stimulus and recorded spikes
MM = month, DD = date, YY = year, T = trial number

STIMTYPEN_X.mat: stimulus
STIMTYPE = stimulus category (see below), N = number of pixels per side, X = version


--------------------
VARIABLES
--------------------

spikeTimes: cell array, 1 x # of cells
Times (in ms) at which each recorded neuron produced an action potential, relative to the beginning of the trial.  Recordings were made at 10 kHz resolution. Note that times correspond to those in stimTimes.

stimulus: matrix, # of pixels x # of pixels x # of frames, Array of stimulus frames.  For each stimulus file, the range 0-255 was mapped to the full intensity range of the monitor.  Stimulus was updated at 30 Hz, as recorded in stimTimes.  Number of frames varies by trial and stimulus but is often 9000 (5 min) or 18000 (10 min).

stimTimes: struct with variable number of fields corresponding to each stimulus file displayed during the specified trial
stimTimes.STIMNAME: array, 1 x # of frames
Time (in ms) at which each frame in the file STIMNAME.mat was displayed, relative to the beginning of the trial.  Note that times correspond to those in spikeTimes.


--------------------
STIMULUS CATEGORIES
--------------------

white = white noise checkerboard (control for all experiments)

spattempexp = spatio-temporal exponential correlations: 12_16_09_t1, 12_16_09_t5, 12_16_09_t8, 02_18_10_t1, 04_18_13_t2

spatexp = spatial exponential correlations: 03_13_12_t2, 03_13_12_t6, 03_13_12_t10, 03_25_12_t2, 03_25_12_t11, 06_27_12_t8, 06_27_12_t14, 07_06_12_t3, 07_06_12_t12, 08_09_12_t2, 09_27_12_t2, 09_27_12_t11, 03_17_13_t2, 03_17_13_t11, 04_18_13_t2, 05_08_13_t5, 06_11_13_t2, 06_11_13_t5, 06_11_13_t8

tempexp = temporal exponential correlations: 04_18_13_t2, 06_28_13_t2

multiscale = multiscale spatial correlations: 10_21_10_t2, 02_16_12_t2, 02_26_12_t2, 02_26_12_t8, 03_04_12_t2, 03_04_12_t7, 03_04_12_t12, 03_13_12_t2, 03_13_12_t6, 03_13_12_t10, 03_25_12_t2, 03_25_12_t11, 06_27_12_t8, 06_27_12_t14, 07_06_12_t3, 07_06_12_t12, 08_09_12_t2, 09_27_12_t2, 09_27_12_t11, 12_06_12_t6, 03_17_13_t2, 03_17_13_t11, 05_08_13_t5, 05_09_13_t9, 07_10_13_t8

natmov = natural movies: 05_08_13_t12, 05_08_13_t15, 05_09_13_t12, 06_28_13_t6, 06_28_13_t9

scramnat = natural movie pixels scrambled in space and time: 05_08_13_t12, 05_08_13_t15, 05_09_13_t12, 06_28_13_t6, 06_28_13_t9

fullfield = full-field white-noise flicker: 02_16_12_t9, 02_26_12_t2, 02_26_12_t8, 03_04_12_t2, 03_04_12_t7, 03_04_12_t12, 03_13_12_t2, 03_13_12_t6, 03_13_12_t10, 03_25_12_t2, 03_25_12_t11, 06_27_12_t8, 06_27_12_t14, 07_06_12_t3, 07_06_12_t12, 08_09_12_t2, 09_05_12_t5, 09_27_12_t2, 09_27_12_t11, 11_15_12_t2, 03_17_13_t2, 03_17_13_t11, 05_08_13_t5

lowcont_white = white noise checkerboard at 50% contrast: 05_09_13_t9

lowcont_multiscale = multiscale spatial correlations at 50% contrast: 05_09_13_t9


--------------------
EXAMPLE
--------------------
data_02_16_12_t2.mat contains spikeTimes (1 x 42 cell array) and stimTimes (struct with 6 fields).  
We found 42 neurons in this recording.  The first cell listed spiked 2443 times, with the first spike 294 s into the recording.
We displayed alternating white noise and multiscale noise, with 64 x 64 pixels in each.  The first frame, stimulus(:,:,1) in white64_a.mat, was displayed 606.6 ms after we began recording, the next frame at 639 ms, and so on.  After 9000 frames (5 min) of white noise, the first frame in multiscale64_g.mat was displayed 303,983.2 ms into the recording.


