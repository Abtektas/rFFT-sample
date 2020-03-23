import struct
import wave
import numpy as np
import csv

def oneChannel(fname, chanIdx):  # Feature extracting for one channel
	f = wave.open(fname, "rb")
	chans = f.getnchannels()
	samps = f.getnframes()
	sampwidth = f.getsampwidth()

	assert sampwidth == 2
	s = f.readframes(samps)
	f.close()
	unpstr = "<{0}h".format(samps * chans)
	x = list(struct.unpack(unpstr, s))
	return x[chanIdx::chans]


firstChannel = oneChannel(
	"location", 0
)  #   change location to path of audio source.
secondChannel = oneChannel(
	"location", 0
)  #   Same as the first one if you have stereo audio.

hammingWindow = np.hamming(
	len(firstChannel)
)  #   Hamming window filtering.
firstChannel = hammingWindow * firstChannel

hammingWindow1 = np.hamming(
	len(secondChannel)
)  #   If you have stereo audio, you have to do same filter again.
secondChannel = hammingWindow1 * secondChannel

A = np.fft.rfft(
	firstChannel, 44100
)  #   Real Fast Fourier transform function for one channel.
A1 = np.abs(A)
A2 = A1[
	:2000
]  #   Slicing from the beginning and in my case it was related only first 2000 values.

B = np.fft.rfft(
	secondChannel, 44100
)  #   Real Fast Fourier transform function for second channel if you have stereo audio.
B1 = np.abs(B)
B2 = B1[
	:2000
]  #   Slicing from the beginning and in my case it was related only first 2000 values.

CSVList0 = []
CSVList1 = []
CSVList2 = []

i = 0
j = 0
k = 0

while i < len(
	A2
):  #   Every index of list will be writing per row so it can be handling easily on .csv
	sliceObject0 = slice(0, 1)
	averageIndexes0 = np.mean(A2[sliceObject0])
	CSVList0.append(averageIndexes0)
	A2 = A2[1:]

while j < len(
	B2
):  #   Every index of list will be writing per row so it can be handling easily on .csv
	sliceObject1 = slice(0, 1)
	averageIndexes1 = np.mean(B2[sliceObject1])
	CSVList1.append(averageIndexes1)
	B2 = B2[1:]

for k in range(0, 2000):
	CSVList2.append("Class-name")  #   Replace your class name.

Columns = zip(CSVList0, CSVList1, CSVList2)

with open(
	"file-location", "w"
) as target:  #   Change file location to where you gonne put.
	writer = csv.writer(target)
	for row in Columns:
		writer.writerow(row)
