#!/usr/bin/python
import sys
import paramiko
import scp
import subprocess
from datetime import datetime, timedelta
from os import path
from scp import SCPClient

#keep the script on the UserDirectory and give relative paths.
#need to seperate tar making over to new method : limitation with cur script : as any tar as IP

def customdatetime(formatd, addday, addhour, addminutes):
    customdate = datetime.now() + timedelta(days = addday, hours = addhour, minutes = addminutes)
    return customdate.strftime(formatd)

def deploy(ip):

    bkpDT = customdatetime("%d%b%Y_%H%M",0,0,0)
    app_path = "%s" %(str(sys.argv[1]))
    bkp_path = "/home/tejora/Downloads/py/tarbkp/%s_Bkp.tar.gz" %(bkpDT)
    filename = path.basename(bkp_path)
    params = "-zcvf"
    SSH_PASSWORD = SSH_USERNAME = "tejora"
    Remote_tar_path = "/home/tejora/dinesh/bkptar"
#    script_path = os.getcwd()

    print "Filename : %r " % (filename)

    if subprocess.call(['tar',params ,bkp_path, app_path])!=True:
        print "\n\n#################### The backup is completed ####################"
    else:
        print "Some error occured while making tar, Terminating the Script"
        quit()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_stdin = ssh_stdout = ssh_stderr = None
    ssh.connect(ip, port=22, username = SSH_USERNAME, password = SSH_PASSWORD)
    scp = SCPClient(ssh.get_transport())
    scp.put(bkp_path, recursive = True, remote_path = Remote_tar_path)
    scp.close()

    RemoteTarExtract = "tar -xvzf" + Remote_tar_path + "/" + filename

    print "RemoteTarCommand : %s " %(RemoteTarExtract)
#    quit()

    try:
        ssh.connect(ip, port=22, username = SSH_USERNAME, password = SSH_PASSWORD)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(RemoteTarExtract)
    except Exception as e:
        print "SSH Connection Error : %r" %(e)

    if ssh_stdout:
        sys.stdout.write(ssh_stdout.read())
    if ssh_stderr:
        sys.stderr.write(ssh_stderr.read())

IPList = ['IP1','IP2'...'IPN']

for IP in IPList:
    deploy(IP)
