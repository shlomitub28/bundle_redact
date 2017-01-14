#!/usr/bin/python
import json
import socket
import random
import struct
import mimetypes
import os
import re
def getRandomIPs(ipslist = []):
    flag = True
    while flag:
        ip  = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        if "255" not in ip and ip not in ipslist:
            flag = False
    return ip

def mapHosts (path):
    mapping = {}
    tmpIPS = []
    hostcnt=1
    with open(path+'/cm_deployment.json') as data_file:
       deployment = json.load(data_file)
       for host in deployment["hosts"]:
           mapping[host["hostname"]] = {}
           mapping[host["hostname"]]["originalHost"] =  host["hostname"]
           mapping [host["hostname"]] ["originalIP"] = host["ipAddress"]
           tmpIPS.append(host["ipAddress"])
           mapping[host["hostname"]]["newIP"] = getRandomIPs(tmpIPS)
           mapping[host["hostname"]]["newHost"] = "host"+str(hostcnt)+".new.com"
           hostcnt+=1

    return mapping

def loopOnFiles(path):
    for dirName, subdirList, fileList in os.walk(path):
        for fname in fileList:
            t,mime = mimetypes.guess_type(dirName+fname)
            type=str(t)

            isarchive = re.search(r'\.gz|\.zip|\.tar|\.gzip',fname)

            if not(isarchive):

                print fname + "--"+ dirName

def handleTextFile(fname,dirName):
    return 0
def changeFileName(fname,dirName):
    return 0
def changeFileHosts():
    return 0

