# Speech-Recognition-Assistant
<p align="center">Speech Recognition Assistant using Python programming language -Speech recognition, or speech-to-text, is the ability for a machine or program to identify words or commands spoken aloud and convert them into readable text or reponds to the commands.</p>


![demo](https://raw.githubusercontent.com/Vijay24-hub/Speech-Recognition-Assistant/master/cover.gif)
<br>
<br>
## ➤Instructions
About how to convert speech to text using Python. This can be done with the help of the “Speech Recognition” API and “PyAudio” library.
### Installating Libraries
### You can install SpeechRecognition from a terminal with pip:
### ➥pyttsx3 2.90
Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.
```console
pip install pyttsx3
```
### ➥SpeechRecognition 3.8.1
Library for performing speech recognition, with support for several engines and APIs, online and offline.
```console
pip install SpeechRecognition
```
### Once installed, you should verify the installation by opening an interpreter session and typing:
``` console
>>> import speech_recognition as sr
>>> sr.__version__
'3.8.1'
```
#### Note: The version number you get might vary. Version 3.8.1 was the latest at the time of writing.

#### Creating a Recognizer instance is easy. In your current interpreter session, just type:
```console
>>> r = sr.Recognizer()
```
#### recognizing speech from an audio source using various APIs:
!Requires internet connection
»» recognize_google(): Google Web Speech API (I used) You may also use some other APIs.
```console
>>> r.recognize_google()
```

### PyAudio 0.2.11
Bindings for PortAudio v19, the cross-platform audio input/output stream library.
```console
pip install PyAudio
```
#### !!If Error occurs while Installation of Pyaudio
#### kindly check ❝error.txt❞ in main files
### ➠After Installation, enter the code and Finally execute the program  

### Built with 
* [VS code](https://code.visualstudio.com/)

### Author
* **Vijay** - *Coder & Learner*-[Vijay24-hub](https://github.com/Vijay24-hub)
<br>

### 【 I am pretty excited about the change taking shape, and sharing information through this repos is my way of contributing back on what I learnt.Thanks! ☻ 】

