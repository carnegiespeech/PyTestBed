'''
Created on Mar 3, 2015

@author: Leo
'''

import xml.etree.ElementTree as ET
import binascii
from test.test_ssl import NULLBYTECERT
import string

def processWordStress(root):
    resStr = ''
    for wdseg in root.iter('wordSeg'):
        if wdseg.find('pitchInfo') is not None:
            for syl in wdseg.find('pitchInfo').findall('syllable'):
                if syl.get('stress') == "true":
                    resStr += wdseg.find('word').text+":"
                    status = syl.get('status')
                    resStr += status+';'
    if len(resStr)==0:
        resStr = 'None'
    return resStr

def getAudQuality(root):
    for audQuality  in root.iter('audioQuality'):
        comment = ''
        for child in audQuality:
            comment +=child.tag +" " +str(child.attrib)+';'
        #print comment
        
        st = audQuality.get('status')
        print st
        print comment
    for audQuality  in root.iter('audioQuality'):
        for child in audQuality:
            try:
                bgpow = child.get('bgpow')
            except:
                bgpow = ''
    return st,  comment, bgpow
    
def getScore(root):
    for scorechild  in root.iter('score'):        
        overallScore = scorechild.text
    return overallScore

def getSpeakingTime(root):
    for speakingTimeEle in root.iter('speakingTime'):
        speakingTime = speakingTimeEle.text
    return speakingTime

def getWordSummary(root):
    for nRefEle in root.iter('nRef'):
        nRef = nRefEle.text
    for nHypEle in root.iter('nHyp'):
        nHyp = nHypEle.text
    for nCorrEle in root.iter('nCorr'):
        nCorr = nCorrEle.text
    for nErrEle in root.iter('nErr'):
        nErr = nErrEle.text
    for nDelEle in root.iter('nDel'):
        nDel = nDelEle.text
    for nInsEle in root.iter('nIns'):
        nIns = nInsEle.text
    return nRef, nHyp, nCorr, nErr, nDel, nIns

def getPPScore(root):
    try:
        for SRHypEle in root.iter('SRHyp'):
            print SRHypEle
            try:
                ppscore = SRHypEle.get('ppScore')
            except:
                print 'no'
                ppscore = '0'
    except:
        ppscore ='0'
    if ppscore ==None:
        ppscore ='0'
        
    return ppscore
     

def parseAAResult(resFile):
    
    tree = ET.parse(resFile)
    root = tree.getroot()
    
    audioStatus, audQuaComment, bgpow = getAudQuality(root)
    score = getScore(root)
    speakingTime = getSpeakingTime(root)   
    nRef, nHyp, nCorr, nErr, nDel, nIns = getWordSummary(root)
    ppscore = getPPScore(root)
    
    return audioStatus, audQuaComment, bgpow, score, speakingTime, nRef, nHyp, nCorr, nErr, nDel, nIns, ppscore  
    
     
   
    
def getPhCount(resFile):
    tree = ET.parse(resFile)
    root = tree.getroot()
    
    ok_count = 0
    soso_count = 0
    bad_count = 0
    unknow_count = 0
    phoneme_count = 0
    for phoneme  in root.iter('phoneme'):
        phoneme_count = phoneme_count+1
        status = phoneme.get('status')
        if status == 'ok':
            ok_count = ok_count+1
        elif status =='soso':
            soso_count = soso_count+1
        elif status == 'bad':
            bad_count = bad_count+1
        else:
            unknow_count = unknow_count+1
    return phoneme_count, ok_count, soso_count, bad_count,unknow_count
    
    
    


def getWordSummaryFromFile(resFile):
    
    tree = ET.parse(resFile)
    root = tree.getroot()
    
    for nRefEle in root.iter('nRef'):
        nRef = nRefEle.text
    for nHypEle in root.iter('nHyp'):
        nHyp = nHypEle.text
    for nCorrEle in root.iter('nCorr'):
        nCorr = nCorrEle.text
    for nErrEle in root.iter('nErr'):
        nErr = nErrEle.text
    for nDelEle in root.iter('nDel'):
        nDel = nDelEle.text
    for nInsEle in root.iter('nIns'):
        nIns = nInsEle.text
    return nRef, nHyp, nCorr, nErr, nDel, nIns

        
    
        
