import thinkdsp
from matplotlib import pyplot

wave=thinkdsp.read_wave(r"E:\folk.wav")
spectrum=wave.make_spectrum()
spectrum.high_pass(cutoff=200,factor=0.01)
spectrum.plot()
pyplot.show()
wave=spectrum.make_wave()
wave.write(r"D:\new2.wav")

