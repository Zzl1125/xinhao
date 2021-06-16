import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import play_wave
from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
from IPython.display import Audio


cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

plt.subplot(2,3,1)
cos_sig.plot()
decorate(xlabel='Time (s)')
plt.title('Cos Signal')
plt.subplot(2,3,2)
sin_sig.plot()
decorate(xlabel='Time (s)')
plt.title('Sin Signal')

mix = sin_sig + cos_sig
plt.subplot(2,3,3)
mix.plot()
decorate(xlabel='Time (s)')
plt.title('Mix Signal')

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
audio = Audio(data=wave.ys, rate=wave.framerate)
print('Number of samples', len(wave.ys))
print('Timestep in ms', 1 / wave.framerate * 1000)

period = mix.period
segment = wave.segment(start=0, duration=period*3)
plt.subplot(2,3,4)
segment.plot()
decorate(xlabel='Time (s)')
plt.title('Segment')

wave.normalize()
wave.apodize()
plt.subplot(2,3,5)
wave.plot()
decorate(xlabel='Time (s)')
plt.title('Out Wave')
wave.write(r"E:\111.wav")
#play_wave(filename='temp.wav')

plt.show()