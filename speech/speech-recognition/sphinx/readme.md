# Installation
- Install sphinxbase and pocketsphinx (of the same version)
- https://cmusphinx.github.io/wiki/download/

## Install pocketsphinx-python
- Follow install instructions for https://github.com/cmusphinx/sphinxbase
- Follow install instructions for https://github.com/cmusphinx/pocketsphinx
- https://github.com/cmusphinx/pocketsphinx-python
- Install PyAudio
- Download amazing script of Sophie: https://gist.github.com/srli/72c7938230537b4f8a4c

## Usage:
- Run from commandline with mic: pocketsphinx_continuous -nfft 2048 -inmic yes
- Run from commandline with file: pocketsphinx_continuous -nfft 2048 -infile file.wav
- Test in Python: python sphinx.py 
- Test with microphone input in python: python stt.py
