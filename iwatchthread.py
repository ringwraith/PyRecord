# -*- coding: utf-8 -*-

import pyaudio
import wave
import datetime

#define of params
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPRATE = 8000
SAMPLES = 2000
SAMPWIDTH = 2
#record time
TIME = 5

def wavrecord():
	#open the input of wave
	pa = pyaudio.PyAudio()
	stream = pa.open(format = FORMAT, channels = CHANNELS, rate = SAMPRATE,
                         input = True, frames_per_buffer = SAMPLES)
	wavbuffer = []
	count = 0
	while count < TIME*(SAMPRATE/SAMPLES):
		#read NUM_SAMPLES sampling data
		string_audio_data = stream.read(SAMPLES)
		wavbuffer.append(string_audio_data)
		count += 1
		#print '.'

	filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".iwav"
	wf = wave.open(filename, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(pa.get_sample_size(FORMAT))
	wf.setframerate(SAMPRATE)
	wf.writeframes("".join(wavbuffer))
	wf.close()
	print filename, "saved"

def main():
    #while True:
    wavrecord()
	
if __name__ == "__main__":
	main()
