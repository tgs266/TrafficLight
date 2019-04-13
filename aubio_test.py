import librosa

from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()

#tl.flash_random(1, 0.1)




y, sr = librosa.load("song.wav")
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
print (tempo)
print (beats)

bs = librosa.frames_to_time(beats, sr=sr)
hz = bs[0]/beats[0]
import sys
import time
import pyaudio
import aubio
import numpy as np
#from pyaudio import PyAudio

win_s = 1024                # fft size
hop_s = 512          # hop size

# parse command line arguments
filename = "song.wav"
samplerate = 0
# create aubio source
a_source = aubio.source(filename, samplerate, hop_s)
samplerate = a_source.samplerate

# create aubio tempo detection
a_tempo = aubio.tempo("default", win_s, hop_s, samplerate)

# create a simple click sound
click = 0.7 * np.sin(2. * np.pi * np.arange(hop_s) / hop_s * samplerate / 3000.)

# pyaudio callback
def pyaudio_callback(_in_data, _frame_count, _time_info, _status):
    #audio_data = np.fromstring(_in_data)
    #print (_in_data)
    samples, read = a_source()
    #print (_time_info)
    is_beat = a_tempo(samples)
    # if is_beat:
    #     samples += click
        #print ('tick') # avoid print in audio callback
    audiobuf = samples.tobytes()
    if read < hop_s:
        return (audiobuf, pyaudio.paComplete)
    return (audiobuf, pyaudio.paContinue)

# create pyaudio stream with frames_per_buffer=hop_s and format=paFloat32
p = pyaudio.PyAudio()
pyaudio_format = pyaudio.paFloat32
frames_per_buffer = 512
n_channels = 1
stream = p.open(format=pyaudio_format, channels=n_channels, rate=44100,
        output=True, frames_per_buffer=frames_per_buffer,
        stream_callback=pyaudio_callback)

# start pyaudio stream
print (bs)
stream.start_stream()
# wait for stream to finish
t = time.time()
frames = 0
RED_active = False
while stream.is_active():
    frames += 1
    time.sleep(hz)
    if frames in beats:
        if RED_active:
            tl.kill(RED)
            RED_active = False 
        else:
            tl.start(RED)
            RED_active = True

# stop pyaudio stream
stream.stop_stream()
stream.close()
# close pyaudio
p.terminate()