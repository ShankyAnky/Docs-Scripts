#!/usr/bin/python
import sys
from os import path
from datetime import datetime, timedelta
from subprocess import call,Popen
import os
import os.path
from paramiko import SSHClient
from scp import SCPClient

#script,source,dest,bkpfname = sys.argv
#print sys.argv
#quit("wow")

#if path.exists("/home/tejora/Downloads/py"):
    #print "ya"
#
#if path.isfile("/home/tejora/Downloads/py/hi.txt"):
    #print "yo"
#else:
    #print "no"
#
#if path.isdir("/home/tejora/Downloads/py/"):
    #print "true"
#else:
    #print "false"
#
#split = path.split("/home/tejora/Downloads/py/hi.txt")
#for splits in split:
    #print splits
#
#print path.realpath("hi.py") #> /home/tejora/Downloads/py/hi.txt path from root
#print path.abspath("hi.py")

################################################################################
#script returns the Date in given format.... You can even add/subtract Days/Hours/Minutes
#usage customdatetime("datef ormat",DaysToAdd_sub,HoursToAdd_sub,MinutesToAdd_sub)
def customdatetime(formatd, addday, addhour, addminutes):
    customdate = datetime.now() + timedelta(days = addday, hours = addhour, minutes = addminutes)
    return customdate.strftime(formatd)
#print customdatetime("%Y_%m_%d %H:%M",0,0,0)
################################################################################

############## Backup script ################################################
#Takes the backup as Tar.gz
#Usage : custombkp("SourceDir/File","BackupDir",Tarfilename)
def custombkp(source, dest, bkpfname):
    try:
        bkpDT = customdatetime("%d%b%Y_%H:%M",0,0,0)
        app_path = "%s" %(source)
        bkp_path = "%s/%s_%s.tar.gz" %(dest,bkpDT,bkpfname)
        params = "-cvzf"
        if call(['tar',params,bkp_path,app_path])!=True:
            print "\n\n#################### The backup is completed ####################"
            quit()
    except Exception as exception:
        print "\n\n#################### ERROR : EXCEPTION ####################\n%r\n", exception
    finally:
        quit("\n\n#################### The Script ended ####################\n")
#custombkp(".py/joomla","./bkp","test")
################################################################################

################################################################################
#this script returns all the component of a Path mentioned i.e DIR/Filename/seperator
#usagesplitAll("path/to/something")
def splitAll(path):
   parent, name = os.path.split(path)
   if name == '':
       return (parent, )
   else:
       return splitAll(parent) + (name,)

print splitAll('/home/user/Work/text.txt')
################################################################################



################################################################################
import paramiko
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
com="ls ~/desktop"
client.connect('MyIPAddress',MyPortNumber, username='username', password='password')
output=""
stdin, stdout, stderr = client.exec_command(com)

print "ssh succuessful. Closing connection"
stdout=stdout.readlines()
client.close()
print "Connection closed"

print stdout
print com
for line in stdout:
    output=output+line
if output!="":
    print output
else:
    print "There was no output for this command"
################################################################################
