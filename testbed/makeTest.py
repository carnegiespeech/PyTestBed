'''
Copyright 2015 Carnegie Speech LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@author: Leo
'''

import os
import glob
import sendTransaction
import socket
import os.path
import random


requester = "" #Obtain from Carnegie Speech
secretKey ="" #Obtain from Carnegie Speech

requesterID = "Gary" #Must defined by user
userID= "Gary" #Must defined by user
requesterInfo="SessionTest"#Must defined by user

listFile = '../fileidlist.txt'#Must be prepared before run the scripts
fid = open(listFile)
lines = fid.readlines()
fid.close()

#scene = 'use_wden'
audiotype = '.wav'
xmlFolder = '../AARequest'  #Must be prepared before run the scripts
#audioFolder = '../Audio/'+scene #Must be prepared before run the scripts
audioFolder = '../Audio'        #Must be prepared before run the scripts

# resultFolder = '../AAResult/'+scene
resultFolder = '../AAResult'

if not os.path.exists('../AAResult'):
    os.mkdir('../AAResult')
if not os.path.exists(resultFolder):
    os.mkdir(resultFolder)

#Above parameters must be defined and assigned value to continue
###############################################################################3

for ln in lines:
    requesterSeqNum = random.randint(100000,1000000)
    fileid = ln.split('\n')[0]
    trans_id = fileid
    


    audioFile = audioFolder+'/'+fileid+audiotype

    resFile = resultFolder+'/'+fileid+'.xml'
    xmlFile = xmlFolder+'/'+fileid+'.xml'
    print resFile
    serverAdd = 'staging2.carnegiespeech.com'
    portNum = 8084
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverAdd, portNum))
    
    sendTransaction.sendAARequest(s, requester, requesterID, userID, requesterInfo, "123456", trans_id, audiotype, xmlFile, secretKey)
    sendTransaction.sendAudioMessage(s, trans_id, audioFile)
    sendTransaction.receiveAAResult(s,trans_id, resFile)

    if os.path.isfile(resFile):
        pass
    else:
        print audioFile
        




                                                                                      
