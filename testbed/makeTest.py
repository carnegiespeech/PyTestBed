'''
Created on March 2, 2015

@author: Leo
'''

import os
import glob
import sendTransaction
import socket
import os.path
import random


requester = ""#Obtain from Carnegie Speech
secretKey =""#Obtain from Carnegie Speech

requesterID = "" #Must defined by user
userID= ""#Must defined by user
requesterInfo=""#Must defined by user

listFile = '../fileidlist.txt'#Must be prepared before run the scripts
fid = open(listFile)
lines = fid.readlines()
fid.close()

scene = 'use_wden'
audiotype = '.ogg'
xmlFolder = '../AARequest'  #Must be prepared before run the scripts
audioFolder = '../Audio/'+scene #Must be prepared before run the scripts

resultFolder = '../AAResult/'+scene
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
        




                                                                                      
