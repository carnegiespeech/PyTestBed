# PyTestBed
This is a demo system for demonstrating speechServices use

The first script makeTest.py sends the audioFiles to the speech server. 
To run the script you will have to put in your CarnegieSpeech supplied speech service credential.
You will have to modify the following lines to put in your credentials.
<ul>
  <li>requester = "" #Obtain from Carnegie Speech
  <li>secretKey ="" #Obtain from Carnegie Speech
</ul>
The second script collectResultSummary.py checks all the responses and calculates the average number of OK 
(good) pronunciations in the audio files. This average number for each phoneme is then compared to 0.7 to 
determine if the samples indicate good or poor pronunciation. We only have 2 short sentences in this sample, 
so the results aren't really indicative of problem speech. 

A trace of running first makeTest.py followed by collectResultSummary.py is given in the file "run-trace.txt"

To change what the demo system is doing, you change the fileidlist.txt. You can add file names. The default 
extension for the audio is .wav. You can also change what you are requesting speechServices to do for an 
audio-file, by changing the corresponding xml file in the AARequest directory.
