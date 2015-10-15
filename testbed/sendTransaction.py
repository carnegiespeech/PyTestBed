'''
Created on Nov 24, 2014

@author: Leo
'''
import os
import glob
import socket
import struct
import ctypes
import random
import md5
import time
from datetime import datetime, date, time
import datetime
from lib2to3.fixer_util import String
import wave

verID = "SendFileModule_Python_v1.0"

def sendAARequest(socketConnection, requester, requesterID, userID, requesterInfo,requesterSeqNum, TransactionID,audioType, xmlFile, clientSecretKey):
    requestStr = ''
    fid = open(xmlFile)
    temp = fid.readlines()
    fid.close()
    for t in temp:
        requestStr+=t
    headerStr = "<message serviceType='AARequest' transactionID='"+TransactionID+"'>"
    audioStr = "<audio type='"+audioType+"' save='True'/>"
    temp = datetime.datetime.now().__str__().split(' ')[1]
    #print date.today().isoformat()
    #print temp.split('.')
    if len( temp.split('.'))==2:
        dateTimeStamp = date.today().isoformat()+"T"+temp.split('.')[0]+'.'+temp.split('.')[1][0:3]+"-05:00"
    else:
        dateTimeStamp = date.today().isoformat()+"T"+temp.split('.')[0]+'.000'+"-05:00"
    hashTokenInstance = requester + "-" + requesterID + "-" +requesterInfo+"-"+dateTimeStamp + "-" + requesterSeqNum+"-"+clientSecretKey;
    m = md5.new()
    m.update(hashTokenInstance)
    hashString = m.hexdigest()
    #print userID+' '
    validStr = " <validate requester='" + requester + "'\n" + "       requesterID='" + requesterID + "'\n" +"       userID='"+ userID+ "'\n"+"       apiVersion='"+verID+"'\n"+"       requesterInfo='" + requesterInfo + "'\n" +"       requesterSeqNum='" + requesterSeqNum + "'\n" +"       dateTimeStamp='" + dateTimeStamp + "'\n" +"       hashToken='" + hashString + "'/>\n";
    
    messageStr = headerStr+"\n  "+validStr+"\n  "+audioStr+"\n  "+requestStr+"\n</message>"
    
    HdrLen = struct.pack('<i',len(messageStr))
    socketConnection.send(HdrLen[3])
    socketConnection.send(HdrLen[2])
    socketConnection.send(HdrLen[1])
    socketConnection.send(HdrLen[0])
    BdyLen = struct.pack('i', 0)
    socketConnection.send(BdyLen)
    socketConnection.send(messageStr)
    
def sendAudioMessage(socketConnection, TransactionID, audioFile):   
    header_str = "<message serviceType=\'AudioBlock\' transactionID='"+TransactionID+"' final = 'true'>\n  <AudioBlock  AAReqID='"+TransactionID+"'>\n  </AudioBlock>\n</message>"    
    HdrLen = struct.pack('i',len(header_str))
    socketConnection.send(HdrLen[3])
    socketConnection.send(HdrLen[2])
    socketConnection.send(HdrLen[1])
    socketConnection.send(HdrLen[0])
    data = ''
    with open(audioFile, "rb") as f:
        bb = f.read(1)
        data = bb
        while bb != "":
            # Do stuff with byte.
            bb = f.read(1)
            data += bb
    BdyLen = struct.pack('i', len(data))
    socketConnection.send(BdyLen[3])
    socketConnection.send(BdyLen[2])
    socketConnection.send(BdyLen[1])
    socketConnection.send(BdyLen[0])
    socketConnection.send(header_str)
    socketConnection.send(data)

def receiveAAResult(socketConnection,TransactionID, resultFile):
    temp =''
    while True:
        temp +=socketConnection.recv(1)
        if( len(temp) == 4):
            break
    HdrLen = struct.unpack('>i', temp)[0]
    print HdrLen
    temp =''
    while True:
        temp +=socketConnection.recv(1)
        if( len(temp) == 4):
            break
    BdyLen = struct.unpack('>i', temp)[0]
    print BdyLen
    strLen = HdrLen+BdyLen
    
    tt = ''
    try:
        while True:
            tt += socketConnection.recv(1024)
            if(len(tt)==strLen):
                break
        print resultFile
        fid = open(resultFile, 'w')
        fid.write(tt)
        fid.close()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print 'error'
    
  