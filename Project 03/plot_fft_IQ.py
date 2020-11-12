import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math

#                x  -- input signal
#                fs -- sampling frequency [MHz] 
#                f0 -- center frequency [MHz]
#                n0 -- first sample (start time = n0/fs)
#                nf -- block size for transform (signal duration = nf/fs)
#                title_of_plot--title of plot (string) (optional)

## Import data from file 
data = np.fromfile("/home/ksgilll/Desktop/ECE3311/Projects/Project2/Source Code/mystery_FM.dat",dtype="uint8")
x = data[0::2] + 1j*data[1::2]
def plot_FFT_IQ (x, n0, nf, fs, f0, title_of_plot=None):
	x_segment = x[n0:n0+nf]#-This extracts a segment of x starting at n0, of length nf, and plots the FFT.
	p = scipy.fftpack.fft(x_segment)
	z = 20*np.log10(np.abs(p)/np.max(np.abs(p)))
	Low_freq=(f0-fs/2) #lowest frequency to plot
	High_freq=(f0+fs/2); #highest frequency to plot
	N=len(z) 
	freq=(np.arange(0,N)*fs)/(N+Low_freq) #[0:1:N-1]*(fs)/N+Low_freq
	fig, ax = plt.subplots()
	if title_of_plot == None:
		ax.set_title('Spectrum Center Frequency = ' + str(f0))
	else:
		ax.set_title(title_of_plot+' Center Frequency = ' + str(f0))
	ax.set_ylabel('Relative amplitude [dB down from max]')
	ax.set_xlabel('Freqency [MHz]')
	ax.plot(freq,z)
	plt.show()

if __name__ == "__main__":
	plot_FFT_IQ(x,50000, 90000, 2000000, 91300000)
