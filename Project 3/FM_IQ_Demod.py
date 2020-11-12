import numpy as np
data = np.fromfile("/home/ksgilll/Desktop/ECE3311/Projects/Project2/Source Code/mystery_FM.dat",dtype="uint8")
x = data[0::2] + 1j*data[1::2]
def fm_demod(y):
	''' 
		This function demodualtes an FM signal. It is assumed that the FM signal 
		is complex (i.e. an IQ signal) centered at DC
	'''
	df=y/abs(y) #normalize the amplitude (i.e. remove amplitude variations)
	fc = 0
	# Remove carrier.
	n = np.arange(len(y))
	rx = y*np.exp(-1j*2*np.pi*fc*n)
	# Extract phase of carrier.
	phi = np.arctan2(np.imag(rx), np.real(rx))
	# Calculate frequency from phase.
	y_FM_demodulated = np.diff(np.unwrap(phi)/(2*np.pi*df))
	return y_FM_demodulated

if __name__ == "__main__":
	fm_decoded = fm_demod(x)
	print(fm_decoded.shape)
	## Write Data To AudioFile	
	fm_decoded*= 1000 / np.max(np.abs(fm_decoded))               # scale so it's audible
	fm_decoded.astype("int16").tofile("/home/ksgilll/Desktop/ECE3311/Projects/Project2/Source Code/recording.raw")

