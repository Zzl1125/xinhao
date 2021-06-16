from matplotlib import pyplot
import thinkdsp
wave=thinkdsp.read_wave(r"E:\folk.wav")
pyplot.subplot(211)
wave.plot()
spectrum=wave.make_spectrum()
pyplot.subplot(212)
spectrum.plot()
pyplot.show()
