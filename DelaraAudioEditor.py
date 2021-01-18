import urllib.request

import matplotlib.pyplot as plt
import numpy as np

from pydub import AudioSegment
import sys
from pydub.playback import play
from glob import glob


if False:
    # Download an audio file
    urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
    # Load into PyDub
    loop = AudioSegment.from_wav("metallic-drums.wav")
    # Play the result
    play(loop)


numFiles = 5
delaraAudioSegs  = [AudioSegment.from_file(m4a_file) for m4a_file in glob("tracks/*.m4a")[0:numFiles]]

mixedSounds = delaraAudioSegs[0][2000:8000]

for segment in delaraAudioSegs[1:]:
    mixedSounds = mixedSounds.append(segment)
    print(segment.duration_seconds)
    samples = (segment.get_array_of_samples())

#sys.exit(1)
samples = (mixedSounds.get_array_of_samples())
plt.figure(1)
plt.plot(samples)
plt.show()

play(mixedSounds)