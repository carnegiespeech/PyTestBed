'''
Created on Mar 3, 2015

@author: Leo
'''

import os
import glob
import sendTransaction
import socket
import random
import os.path
import processAAResult

listFile = '../fileidlist.txt'

fid = open(listFile)
lines = fid.readlines()
fid.close()



resultFolder = '../AAResult/'

print str(len(lines))+" files in total"
PHONEME_AVG = dict()

PHONEME = list()
OK = list() 
SOSO = list()
BAD = list()
UNKNOW = list()

NREF = list()
NHYP = list()
NCORR = list()
NERR = list()
NDEL = list()
NINS = list()

reFolder = resultFolder;
total_ok = 0
total_soso = 0
total_bad = 0
total_phoneme = 0
total_unknow = 0

total_nRef = 0
total_nHyp = 0
total_nCorr = 0
total_nErr = 0
total_nDel = 0
total_nIns = 0

for ln in lines:
    fileid = ln.split('\n')[0]
    resFile = reFolder+fileid.split('\n')[0]+'.xml'
    print resFile
    phoneme_count, ok_count, soso_count, bad_count,unknow_count = processAAResult.getPhCount(resFile,PHONEME_AVG)
    total_phoneme = total_phoneme + phoneme_count
    total_ok = total_ok + ok_count
    total_soso = total_soso + soso_count
    total_bad = total_bad + bad_count
    total_unknow = total_unknow+ unknow_count
    
    nRef, nHyp, nCorr, nErr, nDel, nIns = processAAResult.getWordSummaryFromFile(resFile);
    total_nRef = total_nRef+int(nRef);
    total_nHyp = total_nHyp+int(nHyp);
    total_nCorr = total_nCorr+int(nCorr);
    total_nErr = total_nErr+int(nErr);
    total_nDel = total_nDel+int(nDel);
    total_nIns = total_nIns+int(nIns);
    
    
    PHONEME.append(total_phoneme) 
    OK.append(total_ok)
    SOSO.append(total_soso)
    BAD.append(total_bad)
    UNKNOW.append(total_unknow)
    
    NREF.append(total_nRef)
    NHYP.append(total_nHyp)
    NCORR.append(total_nCorr)
    NERR.append(total_nErr)
    NDEL.append(total_nDel)
    NINS.append(total_nIns)

print "There are "+str(PHONEME)+ " recognized phonemes" 
print "OK Phonemes: "+str(OK)
print "SOSO phonemes: "+str(SOSO)
print "BAD phonemes: "+str(BAD)
print "UNKNOWN phonemes: "+str(UNKNOW)
print "There are "+str(PHONEME_AVG)
for Key,Value in PHONEME_AVG.iteritems(): 
    percentCorrect = float(Value.count('ok'))/len(Value)
    judgement = "poor"
    if percentCorrect > 0.7:
        judgement = "Good"
    print "  Average correct for Phoneme "+Key +"=" + '%.2f' % percentCorrect + " " + judgement

print "There are "+str(NREF) +" reference words"
print "Hyp Words: "+str(NHYP)
print "Corret Words: "+str(NCORR)
print "Error Words: "+str(NERR)
print "Deletions: "+str(NDEL)
print "Insertions: "+str(NINS)
