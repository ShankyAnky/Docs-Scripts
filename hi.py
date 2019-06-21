#!/usr/bin/python
import sys
from os import path
from datetime import datetime, timedelta
from subprocess import call,Popen

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
def customdatetime(formatd, addday, addhour, addminutes):
    customdate = datetime.now() + timedelta(days = addday, hours = addhour, minutes = addminutes)
    return customdate.strftime(formatd)
#print customdatetime("%Y_%m_%d %H:%M",0,0,0)
################################################################################

##############  Backup scripts  ################################################
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
        print "\n\n#################### ERROR : EXCEPTION ####################\n\n%r\n", exception
    finally:
        quit("\n\n#################### The Script ended ####################\n")
#custombkp(".py/joomla","./bkp","test")
################################################################################
