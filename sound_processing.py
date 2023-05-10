import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, rfftfreq
import re
import sys

def find_max_frequency(frequencies, amplitudes):
	max_amplitude = -1;
	max_frequency = -1;
	for index, frame in enumerate(amplitudes):
		if max_amplitude < frame:
			max_amplitude = frame
			max_frequency = frequencies[index]
	return {"max_amplitude": max_amplitude, "max_frequency": max_frequency}

USAGE="usage: [sound fragment]"
HELP = f"{USAGE}\nThis script takes one argument:\nsound fragment: the name of the file that contains the fragment of interest"
if len(sys.argv) > 1 and re.match(r"^(help|h|usage)$", sys.argv[1]) != None:
	print(HELP)
	exit()

if len(sys.argv) < 2:
	print(f"[ERROR]: {USAGE}")
	exit()

fragment_filename=sys.argv[1]
fragment_filename_without_extension = re.sub("\\..*", "", fragment_filename)
if re.match(r".*\.(wav)$", fragment_filename) == None:
	print("[ERROR] file extension not accepted")
	exit()

rate, data = wav.read(fragment_filename)
N = data.shape[0]

fft_out_left_channel = np.abs(rfft(data[:,0]))
fft_out_right_channel = np.abs(rfft(data[:,1]))

frequencies = rfftfreq(N, 1 / rate)

# Find max frequencies
max_frequency_object_left = find_max_frequency(frequencies, fft_out_left_channel)
max_frequency_left = max_frequency_object_left["max_frequency"]
max_frequency_object_right = find_max_frequency(frequencies, fft_out_right_channel)
max_frequency_right = max_frequency_object_right["max_frequency"]

print(f"Max Frequencies: left_channel={max_frequency_left}, right_channel={max_frequency_right}")

# Plotting results
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

max_y = max(max_frequency_object_left["max_amplitude"], max_frequency_object_right["max_amplitude"])
multiple_major = np.power(10,np.floor(np.log10(max_y)))
multiple_minor = np.power(10,np.floor(np.log10(max_y))-1)

max_y_delta_major = round( (max_y/5)/multiple_major)*multiple_major
if max_y_delta_major == 0:
	multiple_major = np.power(10,np.floor(np.log10(max_y))-1)
	max_y_delta_major = round( (max_y/5)/multiple_major)*multiple_major

max_y_delta_minor = round( (max_y/25)/multiple_minor)*multiple_minor
if max_y_delta_minor == 0:
	multiple_minor = np.power(10,np.floor(np.log10(max_y))-2)
	max_y_delta_minor = round( (max_y/25)/multiple_minor)*multiple_minor
max_y_delta_minor = round( (max_y/25)/multiple_minor)*multiple_minor

print(f"max_y_delta_major={max_y_delta_major}, max_y_delta_minor={max_y_delta_minor}")

major_ticks_x = np.arange(0, 25000, 1000)
minor_ticks_x = np.arange(0, 25000, 200)
major_ticks_y = np.arange(0, max_y, max_y_delta_major)
minor_ticks_y = np.arange(0, max_y, max_y_delta_minor)
ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)
ax.grid(which='minor', alpha=0.5, color="#7777FF", linewidth=0.5, linestyle=":")
ax.grid(which='major', alpha=0.5, color="#AAAAAA", linewidth=0.8, linestyle="-")

plt.title(f"Spectrum Analysis of {fragment_filename_without_extension}")
plt.ylabel("Sound amplitude")
plt.xlabel("Frequency, Hz")
plt.plot(frequencies, fft_out_left_channel, label="Left channel")
plt.plot(frequencies, fft_out_right_channel, label="Right channel")
plt.legend(loc=0, frameon=True)
plt.xlim([0, 5000])
plt.show()
