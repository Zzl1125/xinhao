from matplotlib import pyplot
import thinkdsp

wave=thinkdsp.read_wave(r"E:\folk.wav")
pyplot.subplot(2,2,1)
pyplot.title('wave')
wave.plot()
spectrum=wave.make_spectrum()
pyplot.subplot(2,2,2)
pyplot.title('frequency')
spectrum.plot()
wave.ys *= 2
wave.ts += 1
wave.write(r"E:\new3.wav")
wave=thinkdsp.read_wave(r"E:\new3.wav")
pyplot.subplot(2,2,3)
pyplot.title('wave')
wave.plot()
spectrum=wave.make_spectrum()
pyplot.subplot(2,2,4)
pyplot.title('frequency')
spectrum.plot()
pyplot.show()
