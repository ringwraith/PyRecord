# -*- coding: utf-8 -*-

import numpy as np
from pyaudio import PyAudio,paInt16
from datetime import datetime
import wave

#define of params
NUM_SAMPLES = 2000
framerate = 8000
channels = 1
sampwidth = 2
#record time
TIME = 30

def save_wave_file(filename, data):
	'''save the date to the wav file'''
	wf = wave.open(filename, 'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(sampwidth)
	wf.setframerate(framerate)
	wf.writeframes("".join(data))
	wf.close()

def record_wave():
	#open the input of wave
	pa = PyAudio()
	stream = pa.open(format = paInt16, channels = 1,
					rate = framerate, input = True,
					frames_per_buffer = NUM_SAMPLES)
	save_buffer = []
	count = 0
	while count < TIME*4:
		#read NUM_SAMPLES sampling data
		string_audio_data = stream.read(NUM_SAMPLES)
		save_buffer.append(string_audio_data)
		count += 1
		#print '.'

	filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"
	save_wave_file(filename, save_buffer)
	save_buffer = []
	print filename, "saved"

def main():
        while True:
                record_wave()
	
if __name__ == "__main__":
	main()
