import thinkdsp
from matplotlib import pyplot

wave=thinkdsp.read_wave(r"E:\folk.wav")
spectrum=wave.make_spectrum()
spectrum.band_stop(low_cutoff=3000, high_cutoff=100000, factor=0.1)
spectrum.plot()
pyplot.show()
wave=spectrum.make_wave()
wave.write(r"E:\new.7.wav")

